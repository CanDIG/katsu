#####################################################################
#                   PRODUCTION SETTINGS                             #
# Inherit from setting base.py. Contain only necessary settings to  #
# make the project run. Following:                                  #
# https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/ #
#####################################################################

import os
from os.path import exists

from .base import *

required_env_vars = [
    "HOST_CONTAINER_NAME",
    "EXTERNAL_URL",
    "CANDIG_INTERNAL_DOMAIN",
    "AGGREGATE_COUNT_THRESHOLD",
    "OPA_URL",
    "POSTGRES_DATABASE",
    "POSTGRES_USER",
    "POSTGRES_PASSWORD_FILE",
    "POSTGRES_HOST",
    "POSTGRES_PORT",
    "REDIS_PASSWORD_FILE",
    "CACHE_DURATION",
]

missing_vars = [var for var in required_env_vars if not os.getenv(var)]
if missing_vars:
    raise EnvironmentError(
        f"Missing required environment variables: {', '.join(missing_vars)}"
    )

ALLOWED_HOSTS = [
    os.environ["HOST_CONTAINER_NAME"],
    os.environ["EXTERNAL_URL"],
    os.environ["CANDIG_INTERNAL_DOMAIN"],
    "127.0.0.1",
    "query",
]
AGGREGATE_COUNT_THRESHOLD = os.environ["AGGREGATE_COUNT_THRESHOLD"]

# Whitenoise
# ----------
MIDDLEWARE.append("whitenoise.middleware.WhiteNoiseMiddleware")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# CANDIG SETTINGS
# ---------------
CACHE_DURATION = int(os.environ["CACHE_DURATION"])


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
        "NAME": os.environ["POSTGRES_DATABASE"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": get_secret(os.environ["POSTGRES_PASSWORD_FILE"]),
        "HOST": os.environ["POSTGRES_HOST"],
        "PORT": os.environ["POSTGRES_PORT"],
    }
}
CONN_MAX_AGE = 300
CONN_HEALTH_CHECKS = True

# Cache
# -----
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f"redis://:{get_secret(os.environ['REDIS_PASSWORD_FILE'])}@{os.environ['EXTERNAL_URL']}:6379/1",
        "TIMEOUT": CACHE_DURATION,
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
            "filename": os.path.join(BASE_DIR, "logs", "django"),
            "formatter": "file",
            "maxBytes": 1024 * 1024 * 5,
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
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 60 * 60 * 24 * 30  # one month
