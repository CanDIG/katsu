#####################################################################
#                   PRODUCTION SETTINGS                             #
# Inherit from setting base.py. Contain only necessary settings to  #
# make the project run. Following:                                  #
# https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/ #
#####################################################################

import os
from os.path import exists

from .base import *

ALLOWED_HOSTS = [
    os.environ.get("HOST_CONTAINER_NAME"),
    os.environ.get("EXTERNAL_URL"),
]

# Whitenoise
# ----------
MIDDLEWARE.append("whitenoise.middleware.WhiteNoiseMiddleware")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# CANDIG SETTINGS
# ---------------
KATSU_AUTHORIZATION = os.getenv("KATSU_AUTHORIZATION")
CANDIG_OPA_URL = os.getenv("OPA_URL")
CONN_MAX_AGE = int(os.getenv("CONN_MAX_AGE", 0))
if exists("/run/secrets/opa-service-token"):
    with open("/run/secrets/opa-service-token", "r") as f:
        CANDIG_OPA_SECRET = f.read()
if exists("/run/secrets/katsu_secret"):
    with open("/run/secrets/katsu_secret", "r") as f:
        SECRET_KEY = f.read()


# function to read docker secret password file
def get_secret(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.readline().strip()
    except (FileNotFoundError, PermissionError) as err:
        print("Error reading secret file: %s" % err)
        raise


# ==============================================================================
# DATABASES SETTINGS
# ==============================================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DATABASE"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": get_secret(os.environ.get("POSTGRES_PASSWORD_FILE")),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
}

# Logging
# -------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "[%(asctime)s] [%(name)s] %(levelname)s: %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
        "file": {
            "format": "[%(asctime)s] [%(name)s] %(levelname)s: %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console",
            "level": "ERROR",  # Set the log level for the console handler
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs", "logs.txt"),
            "formatter": "file",
            "maxBytes": 1024 * 1024,
            "backupCount": 5,
            "level": "ERROR",  # Set the log level for the file handler
        },
    },
    "loggers": {
        "": {
            "level": "ERROR",  # Set the root logger level
            "handlers": ["console", "file"],
        },
        "psycopg": {
            "level": "ERROR",
        },
    },
}

# ==============================================================================
# SECURITY SETTINGS
# ==============================================================================
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_SSL_REDIRECT = True # need port 443
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 60  # Once confirm that all assets are served securely(i.e. HSTS didn’t break anything), increase this value
# SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
