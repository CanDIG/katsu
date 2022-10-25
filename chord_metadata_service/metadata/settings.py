"""
Django settings for metadata project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys
import logging
import json
from os.path import exists

from urllib.parse import quote, urlparse
from dotenv import load_dotenv

from .. import __version__

load_dotenv()

logging.getLogger().setLevel(logging.INFO)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTGRES_PASSWORD_FILE = os.environ.get('POSTGRES_PASSWORD_FILE')
if POSTGRES_PASSWORD_FILE is not None:
    with open(os.environ.get('POSTGRES_PASSWORD_FILE'), "r") as f:
        POSTGRES_PASSWORD_FILE = f.read()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SERVICE_SECRET_KEY", '=p1@hhp5m4v0$c#eba3a+rx!$9-xk^q*7cb9(cd!wn1&_*osyc')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("CHORD_DEBUG", "true").lower() == "true"


# CHORD-specific settings

CHORD_URL = os.environ.get("CHORD_URL")  # Leave None if not specified, for running in other contexts

# SECURITY WARNING: Don't run with CHORD_PERMISSIONS turned off in production,
# unless an alternative permissions system is in place.
CHORD_PERMISSIONS = os.environ.get("CHORD_PERMISSIONS", str(not DEBUG)).lower() == "true"

CHORD_SERVICE_ARTIFACT = "metadata"
CHORD_SERVICE_TYPE_NO_VER = f"ca.c3g.chord:{CHORD_SERVICE_ARTIFACT}"
CHORD_SERVICE_TYPE = f"{CHORD_SERVICE_TYPE_NO_VER}:{__version__}"
CHORD_SERVICE_ID = os.environ.get("SERVICE_ID", CHORD_SERVICE_TYPE_NO_VER)

# SECURITY WARNING: don't run with AUTH_OVERRIDE turned on in production!
AUTH_OVERRIDE = not CHORD_PERMISSIONS

# When Katsu is hosted on a subpath (e.g. http://myportal.com/api/katsu), this
# parameter is used by Django to compute correct URLs in templates (for example
# in DRF API discovery pages, or swagger UI)
FORCE_SCRIPT_NAME = os.getenv("CHORD_METADATA_SUB_PATH", "")

# # Allowed hosts - TODO: Derive from CHORD_URL
# HOST_CONTAINER_NAME = os.environ.get("HOST_CONTAINER_NAME", "")

# CHORD_HOST = urlparse(CHORD_URL or "").netloc
# logging.info(f"Chord debug: {DEBUG}")
# logging.info(f"Chord host: {CHORD_HOST}")
# ALLOWED_HOSTS = [CHORD_HOST or "localhost"]
# if DEBUG:
#     ALLOWED_HOSTS = list(set(ALLOWED_HOSTS + ["localhost", "127.0.0.1", "[::1]"]))
# if HOST_CONTAINER_NAME != "":
#     ALLOWED_HOSTS = list(set(ALLOWED_HOSTS + [HOST_CONTAINER_NAME]))
# logging.info(f"Allowed hosts: {ALLOWED_HOSTS}")
ALLOWED_HOSTS = ["*"]

APPEND_SLASH = False

# Bento misc. settings

SERVICE_TEMP = os.environ.get("SERVICE_TEMP")

#  - DRS URL - by default in Bento Singularity context, use internal NGINX DRS (to avoid auth hassles)
NGINX_INTERNAL_SOCKET = quote(os.environ.get("NGINX_INTERNAL_SOCKET", "/chord/tmp/nginx_internal.sock"), safe="")
DRS_URL = os.environ.get("DRS_URL", f"http+unix://{NGINX_INTERNAL_SOCKET}/api/drs").strip().rstrip("/")

# Candig-specific settings

CANDIG_AUTHORIZATION = os.getenv("CANDIG_AUTHORIZATION", "")
CANDIG_OPA_URL = os.getenv("CANDIG_OPA_URL", "")
CANDIG_OPA_SECRET = os.getenv("CANDIG_OPA_SECRET", "my-secret-beacon-token")
CANDIG_OPA_SITE_ADMIN_KEY = os.getenv("CANDIG_OPA_SITE_ADMIN_KEY", "site-admin")
if exists("/run/secrets/opa-root-token"):
    with open("/run/secrets/opa-root-token", "r") as f:
        CANDIG_OPA_SECRET = f.read()

# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',

    'chord_metadata_service.chord.apps.ChordConfig',
    'chord_metadata_service.experiments.apps.ExperimentsConfig',
    'chord_metadata_service.patients.apps.PatientsConfig',
    'chord_metadata_service.phenopackets.apps.PhenopacketsConfig',
    'chord_metadata_service.mcode.apps.McodeConfig',
    'chord_metadata_service.resources.apps.ResourcesConfig',
    'chord_metadata_service.restapi.apps.RestapiConfig',

    'corsheaders',
    'django_filters',
    'rest_framework',
    'drf_spectacular',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'bento_lib.auth.django_remote_user.BentoRemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# This middlewares are specific to the CANDIG service
if os.getenv('INSIDE_CANDIG', ''):
    MIDDLEWARE.append('chord_metadata_service.restapi.preflight_req_middleware.PreflightRequestMiddleware')
    MIDDLEWARE.append('chord_metadata_service.restapi.candig_authz_middleware.CandigAuthzMiddleware')

CORS_ALLOWED_ORIGINS = []

CORS_PREFLIGHT_MAX_AGE = 0

ROOT_URLCONF = 'chord_metadata_service.metadata.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'chord_metadata_service.metadata.wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['console'],
        },
    },
}

# if we are running the test suite, only log CRITICAL messages
if len(sys.argv) > 1 and sys.argv[1] == 'test':
    logging.disable(logging.CRITICAL)


# function to read postgres password file
def get_secret(path):
    try:
        with open(path) as f:
            return f.readline().strip()
    except BaseException as err:
        logging.error(f"Unexpected {err}, {type(err)}")
        raise


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POSTGRES_DATABASE", 'metadata'),
        'USER': os.environ.get("POSTGRES_USER", 'admin'),
        'PASSWORD': get_secret(
            os.environ["POSTGRES_PASSWORD_FILE"]
        ) if "POSTGRES_PASSWORD_FILE" in os.environ else os.environ.get("POSTGRES_PASSWORD", "admin"),
        # Use sockets if we're inside a CHORD container / as a priority
        'HOST': os.environ.get("POSTGRES_SOCKET_DIR", os.environ.get("POSTGRES_HOST", "localhost")),
        'PORT': os.environ.get("POSTGRES_PORT", "5432"),
    }
}

# Django default cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

FHIR_INDEX_NAME = 'fhir_metadata'

# Set to True to run ES for FHIR index
ELASTICSEARCH = False

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'bento_lib.auth.django_remote_user.BentoRemoteUserAuthentication'
    ],
    'DEFAULT_PARSER_CLASSES': (
        # allows serializers to use snake_case field names, but parse incoming data as camelCase
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
    ),
    'DEFAULT_PERMISSION_CLASSES': ['chord_metadata_service.chord.permissions.OverrideOrSuperUserOnly'],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTHENTICATION_BACKENDS = ['bento_lib.auth.django_remote_user.BentoRemoteUserBackend'] + (
    ['django.contrib.auth.backends.ModelBackend'] if DEBUG else [])

# Models
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# Cache time constant
CACHE_TIME = int(os.getenv('CACHE_TIME', 60 * 60 * 2))

# Settings related to the Public APIs

# Read project specific config.json that contains custom search fields
if os.path.isfile(os.path.join(BASE_DIR, 'config.json')):
    with open(os.path.join(BASE_DIR, 'config.json')) as config_file:
        CONFIG_PUBLIC = json.load(config_file)
else:
    CONFIG_PUBLIC = {}

# Public response when there is no enough data that passes the project-custom threshold
INSUFFICIENT_DATA_AVAILABLE = {"message": "Insufficient data available."}

# Public response when there is no public data available and config file is not provided
NO_PUBLIC_DATA_AVAILABLE = {"message": "No public data available."}

# Public response when public fields are not configured and config file is not provided
NO_PUBLIC_FIELDS_CONFIGURED = {"message": "No public fields configured."}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Metadata Service API',
    'DESCRIPTION': ('Metadata Service provides a phenotypic description of an '
                    'Individual in the context of biomedical research.'),
    'VERSION': __version__,
    'SERVE_INCLUDE_SCHEMA': False,
    # Filter out the url patterns we don't want documented
    'PREPROCESSING_HOOKS': ['chord_metadata_service.metadata.hooks.preprocessing_filter_path'],
    # Split components into request and response parts where appropriate
    'COMPONENT_SPLIT_REQUEST': True,
    # Aid client generator targets that have trouble with read-only properties.
    'COMPONENT_NO_READ_ONLY_REQUIRED': True,
    # Create separate components for PATCH endpoints (without required list)
    'COMPONENT_SPLIT_PATCH': True,
    # Adds "blank" and "null" enum choices where appropriate. disable on client generation issues
    'ENUM_ADD_EXPLICIT_BLANK_NULL_CHOICE': True,
    # Determines if and how free-form 'additionalProperties' should be emitted in the schema. Some
    # code generator targets are sensitive to this. None disables generic 'additionalProperties'.
    # allowed values are 'dict', 'bool', None
    'GENERIC_ADDITIONAL_PROPERTIES': 'dict',
    # Determines whether operation parameters should be sorted alphanumerically or just in
    # the order they arrived. Accepts either True, False, or a callable for sort's key arg.
    'SORT_OPERATION_PARAMETERS': False,
    # modify and override the SwaggerUI template
    'SWAGGER_UI_SETTINGS': {
        'docExpansion': 'none',  # collapse all endpoints by default
        'supportedSubmitMethods': ['get', 'put', 'post', 'delete', 'patch'] if DEBUG else ['get'],  # readonly in prod
    }
}

# SPECTACULAR_SETTINGS['SERVERS'] defines the url to which calls are made when
# testing a request within the swagger UI
if CHORD_URL:
    SPECTACULAR_SETTINGS['SERVERS'] = [{'url': CHORD_URL + FORCE_SCRIPT_NAME}]
