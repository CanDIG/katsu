import logging
import os
import json
import sys
import orjson
from authx.auth import (
    get_opa_datasets,
    verify_service_token,
    is_action_allowed_for_program,
)
from django.conf import settings
from django.http import JsonResponse
from ninja import NinjaAPI, Swagger
from ninja.parser import Parser
from ninja.renderers import BaseRenderer
from ninja.security import APIKeyHeader, HttpBearer

from chord_metadata_service.mohpackets.apis.clinical_data import (
    router as authorzied_router,
)
from chord_metadata_service.mohpackets.apis.discovery import (
    discovery_router as discovery_router,
)
from chord_metadata_service.mohpackets.apis.explorer import (
    explorer_router as explorer_router,
)
from chord_metadata_service.mohpackets.apis.ingestion import (
    router as ingest_router,
    delete_router,
)

from chord_metadata_service.mohpackets.utils import get_schema_version

from django.views.decorators.cache import cache_page
from ninja.decorators import decorate_view

"""
Module with configurations for APIs

Author: Son Chau
"""

logger = logging.getLogger(__name__)
SAFE_METHODS = ("GET", "HEAD", "OPTIONS")


##########################################
#                                        #
#               RENDERER                 #
#                                        #
##########################################
class ORJSONRenderer(BaseRenderer):
    media_type = "application/json"

    def render(self, request, data, *, response_status):
        return orjson.dumps(data)


class ORJSONParser(Parser):
    def parse_body(self, request):
        return orjson.loads(request.body)


##########################################
#                                        #
#             AUTHORIZATION              #
#                                        #
##########################################


class NetworkAuth:
    """
    The built-in authenticate function in Django has been overridden to use custom OPA logic
    to authorize for different types of requests.
    """

    class DeleteAuth(HttpBearer):
        def authenticate(self, request, bearer_token):
            """
            Authenticates a delete request.
            Only site_admin and authorized curators can delete.
            """
            try:
                program_id = request.path.rstrip("/").rsplit("/", 1)[-1]
                write_permission = is_action_allowed_for_program(
                    bearer_token,
                    method=request.method,
                    path=request.path,
                    program=program_id,
                )
                logger.debug(
                    "DELETE request authentication for '%s' with token: %s. Program ID: %s. Write permission: %s.",
                    request.get_full_path(),
                    bearer_token,
                    program_id,
                    write_permission,
                )
                return write_permission

            except Exception as e:
                logger.exception(f"An error occurred in OPA: {e}")
                raise Exception("Error with OPA authentication.")

    class IngestAuth(HttpBearer):
        def authenticate(self, request, bearer_token):
            """
            Authenticates a request for ingest.
            For each program, if the user is listed as a program curator for the program,
            Opa will allow ingest. User must be allowed to ingest into ALL programs
            requested, otherwise it will return false.
            Opa allows site admins to ingest into all programs.
            """
            if not bearer_token:
                return False

            try:
                request_body = request.body.decode("utf-8")
                data = json.loads(request_body)
                program_ids = list(set([item["program_id"] for item in data]))
                write_datasets = all(
                    is_action_allowed_for_program(
                        bearer_token,
                        method=request.method,
                        path=request.path,
                        program=program_id,
                    )
                    for program_id in program_ids
                )

                logger.debug(
                    "INGEST request authentication for '%s' with token: %s and programs: %s. Write datasets: %s.",
                    request.get_full_path(),
                    bearer_token,
                    program_ids,
                    write_datasets,
                )

                return write_datasets

            except Exception as e:
                logger.exception(f"An error occurred in OPA: {e}")
                raise Exception("Error with OPA authentication.")

    class GetAuth(HttpBearer):
        def authenticate(self, request, bearer_token):
            """
            Authenticates a request using the bearer_token then
            fetches the authorized datasets from OPA.

            Args:
                request: The HTTP request object.
                bearer_token: The bearer token for authentication.

            Returns:
                True if the requester has permission (i.e., authorized datasets are found), None otherwise.

            Raises:
                Exception: If an error occurs during OPA authentication.
            """
            if not bearer_token:
                return None

            try:
                read_datasets = get_opa_datasets(request)
                result = True if read_datasets else None
                logger.debug(
                    "OPA Authentication completed for request '%s' with token: %s. "
                    "Read datasets: %s. Result: %s.",
                    request.get_full_path(),
                    bearer_token,
                    read_datasets,
                    result,
                )

                if result:
                    request.read_datasets = read_datasets
                return result

            except Exception as e:
                logger.exception(f"An error occurred in OPA: {e}")
                raise Exception("Error with OPA authentication.")

    class ServiceTokenAuth(APIKeyHeader):
        param_name = "X-Service-Token"

        def authenticate(self, request, service_token):
            if service_token:
                is_valid_token = verify_service_token(
                    service="query", token=service_token
                )
                logger.debug(
                    f"verify_service_token for {request.get_full_path()}: {is_valid_token}."
                    f" X-Service-Token is: {service_token}"
                )
                return is_valid_token

            logger.debug("No X-Service-Token in headers. Not a query service request.")
            return False


class LocalAuth:
    class DeleteAuth(HttpBearer):
        def authenticate(self, request, bearer_token):
            program_id = request.path.rstrip("/").rsplit("/", 1)[-1]
            token_data = settings.LOCAL_OPA_DATASET[bearer_token]

            if token_data:
                if token_data["is_admin"] or program_id in token_data.get(
                    "write_datasets", []
                ):
                    return True

            return False

    class IngestAuth(HttpBearer):
        def authenticate(self, request, bearer_token):
            if bearer_token in settings.LOCAL_OPA_DATASET:
                opa_data = settings.LOCAL_OPA_DATASET[bearer_token]
                is_admin = opa_data["is_admin"]
                write_datasets = opa_data["write_datasets"]

                if is_admin:
                    return True

                request_body = request.body.decode("utf-8")
                data = json.loads(request_body)
                program_ids = [item["program_id"] for item in data]
                authorized = all(
                    program_id in write_datasets for program_id in program_ids
                )

                if authorized:
                    return True

            return False

    class GetAuth(HttpBearer):
        def authenticate(self, request, bearer_token):
            if bearer_token in settings.LOCAL_OPA_DATASET:
                opa_data = settings.LOCAL_OPA_DATASET[bearer_token]
                request.read_datasets = opa_data["read_datasets"]
                return True

    class ServiceTokenAuth(APIKeyHeader):
        param_name = "X-Service-Token"

        def authenticate(self, request, service_token):
            if service_token:
                return service_token == settings.QUERY_SERVICE_TOKEN
            return False


##########################################
#                                        #
#               SETTINGS                 #
#                                        #
##########################################

settings_module = os.environ.get("DJANGO_SETTINGS_MODULE")
# Use OPA in prod/dev environment
if "dev" in settings_module or "prod" in settings_module:
    auth = NetworkAuth()
else:
    auth = LocalAuth()

if "test" in sys.argv:
    auth = LocalAuth()

api = NinjaAPI(
    renderer=ORJSONRenderer(),
    parser=ORJSONParser(),
    docs=Swagger(
        settings={"docExpansion": "none"}
    ),  # collapse all endpoints by default
    title="MoH Service API",
    version=settings.KATSU_VERSION,
    description="This is the RESTful API for the MoH Service.",
)
api.add_router("/discovery/", discovery_router, tags=["discovery"])
api.add_router("/ingest/", ingest_router, auth=auth.IngestAuth(), tags=["ingest"])
api.add_router("/ingest/", delete_router, auth=auth.DeleteAuth(), tags=["delete"])
api.add_router(
    "/authorized/", authorzied_router, auth=auth.GetAuth(), tags=["authorized"]
)
api.add_router(
    "/explorer", explorer_router, auth=auth.ServiceTokenAuth(), tags=["explorer"]
)


@api.get("/service-info")
@decorate_view(cache_page(settings.CACHE_DURATION))
def service_info(request):
    return JsonResponse(
        {
            "name": "katsu",
            "description": "A CanDIG clinical data service",
            "version": settings.KATSU_VERSION,
            "schema_version": get_schema_version(),
        },
        status=200,
        safe=False,
        json_dumps_params={"indent": 2},
    )
