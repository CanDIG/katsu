import logging
import os
import json

from authx.auth import is_permissible
from django.conf import settings
from rest_framework.permissions import SAFE_METHODS, BasePermission

logger = logging.getLogger(__name__)
"""
    This module contains custom permission classes for the API.
    By default, only allow superusers (site_admin) to make changes, and
    non-superusers to only read.
"""


class CanDIGPermissions(BasePermission):
    """
    The has_permission method determines if the user has permission to perform
    the requested operation.

    If the requested is a safe method (GET, HEAD or OPTIONS), returns True.
    If dev or prod environment, it checks if the user is a site admin.
    Local environment always returns True.
    """

    def has_permission(self, request, view):
        request_object = json.dumps({
            "url": request.path,
            "method": request.method,
            "headers": dict(request.headers),
            "data": request.data
        })
        return is_permissible(request_object)