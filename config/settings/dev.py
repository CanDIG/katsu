#############################################################
#                  DEV SETTINGS                             #
# Customize configuration specific to the dev environment   #
# Inherit from setting prod.py and use:                     #
# - candig.docker.internal                                  #
# - debug toolbar enable                                    #
# - docker postgres database                                #
# - user and datasets permission from OPA                   #
# - testing token obtain from keycloak                      #
#############################################################

from .prod import *

DEBUG = True
ALLOWED_HOSTS.extend(["localhost", "127.0.0.1"])

# Debug toolbar settings
# ----------------------
INSTALLED_APPS.append("debug_toolbar")
MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
INTERNAL_IPS = type("c", (), {"__contains__": lambda *a: True})()
DEBUG_TOOLBAR_CONFIG = {
    "RENDER_PANELS": False,
    "RESULTS_CACHE_SIZE": 100,
}

# Logging
# -------
LOGGING["handlers"]["console"]["level"] = "DEBUG"
LOGGING["handlers"]["file"]["level"] = "DEBUG"
LOGGING["loggers"][""]["level"] = "DEBUG"

# Additional loggers specific to the development environment
LOGGING["loggers"].update(
    {
        "factory": {
            "level": "ERROR",
        },
        "faker": {
            "level": "ERROR",
        },
    }
)