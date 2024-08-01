#############################################################
#                  LOCAL SETTINGS                           #
# Customize configuration specific to the local development #
# environment. Inherit from setting base.py and use:        #
# - localhost                                               #
# - debug toolbar enable                                    #
# - local postgres database                                 #
# - user1 set to authorize SYNTHETIC-1                      #
# - user2 set to authorize SYNTHETIC-1, SYNTHETIC-2         #
# - testing user token is "user_1" and "user_2"             #
# - testing query token is "query"                          #
#############################################################

import socket
from .base import *

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]
AGGREGATE_COUNT_THRESHOLD = 5

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

# Cache
# https://docs.djangoproject.com/en/4.1/topics/cache/
CACHE_DURATION = 30  # set to 0 to disable cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "TIMEOUT": CACHE_DURATION,
    }
}

# user_1 is a normal user
# user_2 is a curator
# site_admin is admin
LOCAL_OPA_DATASET = {
    "user_1": {
        "is_admin": False,
        "write_datasets": [],
        "read_datasets": ["PROGRAM_01", "PROGRAM_02"],
    },
    "user_2": {
        "is_admin": False,
        "write_datasets": ["PROGRAM_03", "PROGRAM_04"],
        "read_datasets": ["PROGRAM_03", "PROGRAM_04"],
    },
    "site_admin": {
        "is_admin": True,
        "write_datasets": ["PROGRAM_01", "PROGRAM_02", "PROGRAM_03", "PROGRAM_04"],
        "read_datasets": ["PROGRAM_01", "PROGRAM_02", "PROGRAM_03", "PROGRAM_04"],
    },
}

QUERY_SERVICE_TOKEN = "query"

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
