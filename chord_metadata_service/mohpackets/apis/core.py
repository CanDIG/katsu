import logging
import os
import sys

import orjson
from authx.auth import get_opa_datasets, verify_service_token, is_site_admin
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
from chord_metadata_service.mohpackets.apis.ingestion import router as ingest_router
from chord_metadata_service.mohpackets.utils import get_schema_url

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
    class LoginAuth(HttpBearer):
        def authenticate(self, request, bearer_token):
            """
            Authenticates a request using Open Policy Agent (OPA).

            This method gives permission for site admin or read only request.
            If permitted, it fetches the authorized datasets from OPA and attaches them to the request.

            Returns:
                str: The token if the requester has permission, None otherwise.
            """
            try:
                request.has_permission = (
                    request.method in SAFE_METHODS
                    or is_site_admin(request)
                )
                if not request.has_permission:
                    return None
                authorized_datasets = get_opa_datasets(request)
                request.authorized_datasets = authorized_datasets

            except Exception as e:
                logger.exception(f"An error occurred in OPA: {e}")
                raise Exception("Error with OPA authentication.")

            logger.debug(
                "OPA Authentication completed for request '%s' with token: %s. Authorized datasets: %s. Permission: %s",
                request.get_full_path(),
                bearer_token,
                authorized_datasets,
                request.has_permission,
            )
            return bearer_token

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
    class LoginAuth(HttpBearer):
        def authenticate(self, request, bearer_token):
            # permissions in config/settings/local.py
            request.has_permission = request.method in SAFE_METHODS or any(
                d.get("is_admin", False)
                for d in settings.LOCAL_AUTHORIZED_DATASET
                if d["token"] == bearer_token
            )
            if not request.has_permission:
                return None

            authorized_datasets = [
                dataset
                for d in settings.LOCAL_AUTHORIZED_DATASET
                if d["token"] == bearer_token
                for dataset in d["datasets"]
            ]
            request.authorized_datasets = authorized_datasets

            logger.debug(
                "Local Authentication completed for request '%s' with token: %s. "
                "Authorized datasets: %s. Permission: %s",
                request.get_full_path(),
                bearer_token,
                authorized_datasets,
                request.has_permission,
            )

            return bearer_token

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
api.add_router("/ingest/", ingest_router, auth=auth.LoginAuth(), tags=["ingest"])
api.add_router(
    "/authorized/", authorzied_router, auth=auth.LoginAuth(), tags=["authorized"]
)
api.add_router("/discovery/", discovery_router, tags=["discovery"])
api.add_router(
    "/explorer", explorer_router, auth=auth.ServiceTokenAuth(), tags=["explorer"]
)


@api.get("/service-info")
@decorate_view(cache_page(settings.CACHE_DURATION))
def service_info(request):
    schema_url = get_schema_url()

    return JsonResponse(
        {
            "name": "katsu",
            "description": "A CanDIG clinical data service",
            "version": settings.KATSU_VERSION,
            "schema_url": schema_url,
        },
        status=200,
        safe=False,
        json_dumps_params={"indent": 2},
    )
