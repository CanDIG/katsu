#############################################################
#                  LOCAL SETTINGS                           #
# Customize configuration specific to the local development #
# environment. Inherit from setting base.py and use:        #
# - localhost                                               #
# - debug toolbar enable                                    #
# - local postgres database                                 #
# - user1 set to authorize SYNTHETIC-1                      #
# - user2 set to authorize SYNTHETIC-1, SYNTHETIC-2         #
# - testing token is token_1 and token_2                    #
#############################################################

import os
import socket
from .base import *

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

# Debug toolbar settings
# ----------------------
INSTALLED_APPS.append("debug_toolbar")
MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")

# ==============================================================================
# DATABASES SETTINGS
# ==============================================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "katsu_local",
        "USER": "admin_local",
        "PASSWORD": "password_local",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# You can change username and datasets to suit your needs
LOCAL_AUTHORIZED_DATASET = [
    {
        "token": "token_1",
        "is_admin": False,
        "datasets": ["SYNTHETIC-1"],
    },
    {
        "token": "token_2",
        "is_admin": True,
        "datasets": ["SYNTHETIC-1", "SYNTHETIC-2"],
    },
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "[%(asctime)s] [%(name)s] %(levelname)s: %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
    },
    "loggers": {
        "": {
            "level": "INFO",
            "handlers": ["console"],
        },
    },
}

# Debug toolbar settings
# ----------------------
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + [
    "127.0.0.1",
    "10.0.2.2",
]
