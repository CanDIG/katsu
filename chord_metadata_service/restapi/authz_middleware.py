from django.conf import settings
from django.http import HttpResponseServerError
import requests
import json
import re

REQUEST_PATHS_TO_AUTHZ_PATHS = {"/api/phenopackets": "api/phenopackets",
                                "/api/individuals": "api/ga4gh/individuals"}

AUTHZ_PATHS = ["^/api/phenopackets/?.*", "^/api/datasets/?.*", "^/api/diagnoses/?.*", "^/api/diseases/?.*",
               "^/api/genes/?.*", "^/api/genomicinterpretations/?.*", "^/api/htsfiles/?.*", "^/api/individuals/?.*",
               "^/api/interpretations/?.*", "^/api/metadata/?.*", "^/api/phenopackets/?.*",
               "^/api/phenotypicfeatures/?.*", "^/api/procedures/?.*", "^/api/variants/?.*",
               "^/api/biosamples/?.*", "/api/overview"]


class AuthzMiddleware:
    """
    Middleware for dataset-level authorization.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # auth for current dycons
        if settings.CANDIG_OPA_VERSION == "dycons" and \
                request.path in REQUEST_PATHS_TO_AUTHZ_PATHS and request.method == "GET":
            tokens = {}
            for header in request.headers:
                header_all_caps = header.upper()
                if header_all_caps.startswith(("X-CANDIG-LOCAL-", "X-CANDIG-DAC-", "X-CANDIG-FED-", "X-CANDIG-EXT-")):
                    tokens[header] = json.loads(request.headers[header])

            request_body = {
                "input": {
                    "headers": tokens,
                    "body": {
                        "path": REQUEST_PATHS_TO_AUTHZ_PATHS[request.path],
                        "method": request.method
                    }
                }
            }
            allowed_datasets = get_allowed_datasets(request_body)
            if allowed_datasets is not None:
                if isinstance(allowed_datasets, tuple):
                    return allowed_datasets[1]
                request.allowed_datasets = allowed_datasets
        # auth for rego_dev_playground repo
        elif (settings.CANDIG_OPA_VERSION == "rego_dev_playground" and
              any(re.match(path_re, request.path) for path_re in AUTHZ_PATHS) and
              request.method == "GET"):
            tokens = {}
            for header in request.headers:
                header_all_caps = header.upper()
                if header_all_caps.startswith(("X-CANDIG-LOCAL-", "X-CANDIG-DAC-", "X-CANDIG-FED-", "X-CANDIG-EXT-")):
                    tokens[header] = json.loads(request.headers[header])

            request_body = {
                "input": {
                    "headers": tokens,
                    "body": {
                        "path": request.path,
                        "method": request.method
                    }
                }
            }

            allowed_datasets = get_allowed_datasets(request_body)
            if allowed_datasets is not None:
                request.allowed_datasets = allowed_datasets
                if isinstance(allowed_datasets, tuple):
                    return allowed_datasets[1]
            request_body["input"]["body"]["query_type"] = "counts"
            allowed_datasets_for_counts = get_allowed_datasets(request_body)
            if allowed_datasets_for_counts is not None:
                request.allowed_datasets_for_counts = allowed_datasets_for_counts
                if isinstance(allowed_datasets, tuple):
                    return allowed_datasets[1]

        response = self.get_response(request)
        return response


def get_allowed_datasets(request_body):
    if settings.CANDIG_OPA_URL:
        try:
            if settings.CANDIG_OPA_VERSION == "dycons":
                response = requests.post(settings.CANDIG_OPA_URL +
                                         "/v1/data/ga4ghPassport/tokenControlledAccessREMS",
                                         json=request_body)
            else:
                response = requests.post(settings.CANDIG_OPA_URL +
                                         "/v1/data/permissions/datasets",
                                         headers={"Authorization": f"Bearer {settings.PERMISSIONS_SECRET}"},
                                         json=request_body,
                                         verify=settings.ROOT_CA)
            response.raise_for_status()
        except requests.exceptions.RequestException:
            error_response = {
                "error": "error getting response from authorization service"
            }
            response = HttpResponseServerError(json.dumps(error_response))
            response["Content-Type"] = "application/json"
            return ("error", response)

        allowed_datasets = response.json()["result"]
        return allowed_datasets
    else:
        return None
