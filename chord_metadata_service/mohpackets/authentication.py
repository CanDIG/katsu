import logging

from authx.auth import get_opa_datasets, is_site_admin
from django.conf import settings
from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.plumbing import build_bearer_security_scheme_object
from ninja.security import HttpBearer
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed

logger = logging.getLogger(__name__)


class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if not auth:
            raise AuthenticationFailed("Authorization required")
        else:
            opa_secret = settings.CANDIG_OPA_SECRET
            try:
                authorized_datasets = get_opa_datasets(request, admin_secret=opa_secret)
                # add dataset to request
                logger.debug(f"User is authorized to access {authorized_datasets}")
                request.authorized_datasets = authorized_datasets

            except Exception as e:
                logger.exception(
                    f"An error occurred in OPA get_authorized_datasets: {e}"
                )
                raise AuthenticationFailed("Error retrieving datasets from OPA.")


class LocalAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if not auth:
            raise AuthenticationFailed("Authorization required")
        token = auth[1].decode("utf-8")
        # get authorized datasets from local settings
        authorized_datasets = [
            dataset
            for d in settings.LOCAL_AUTHORIZED_DATASET
            if d["token"] == token
            for dataset in d["datasets"]
        ]

        request.authorized_datasets = authorized_datasets


class TokenScheme(OpenApiAuthenticationExtension):
    target_class = TokenAuthentication
    name = "tokenAuth"
    match_subclasses = True
    priority = -1

    def get_security_definition(self, auto_schema):
        return build_bearer_security_scheme_object(
            header_name="Authorization",
            token_prefix="Bearer",
        )


class LocalAuthScheme(OpenApiAuthenticationExtension):
    target_class = LocalAuthentication
    name = "localAuth"

    def get_security_definition(self, auto_schema):
        return build_bearer_security_scheme_object(
            header_name="Authorization",
            token_prefix="Bearer",
        )


# =========================================================
