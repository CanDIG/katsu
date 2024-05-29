import logging.config
import os

bind = "0.0.0.0"
workers = int(os.getenv("KATSU_WORKERS", 2))
threads = int(os.getenv("KATSU_THREADS", 4))
worker_class = "uvicorn.workers.UvicornWorker"
user = "candig"
group = "candig"
worker_tmp_dir = "/dev/shm"

# For logging
access_log_format = (
    "%(h)s "  # remote address
    "%(l)s "  # '-'
    "%(u)s "  # user
    "%(t)s "  # date of the request
    "%(r)s "  # status line (e.g. GET / HTTP/1.1)
    "%(m)s "  # request method
    "%(U)s "  # URL path without query string
    "%(q)s "  # query string
    "%(H)s "  # protocol
    "%(s)s "  # status
    "%(B)s "  # response length
    "%(f)s "  # referer
    "%(a)s "  # user agent
    "%(T)s "  # request time in seconds
    "%(p)s "  # process ID
    "%({authorization}i)s"  # auth header
)
log_directory = "/app/chord_metadata_service/logs"
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "file": {
            "format": "[%(asctime)s] [%(name)s] %(levelname)s: %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
    },
    "handlers": {
        "error_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "file",
            "filename": os.path.join(log_directory, "gunicorn.error"),
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
        },
        "access_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "file",
            "filename": os.path.join(log_directory, "gunicorn.access"),
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
        },
    },
    "loggers": {
        "gunicorn.error": {
            "level": "INFO",
            "handlers": ["error_file_handler"],
        },
        "gunicorn.access": {"level": "INFO", "handlers": ["access_file_handler"]},
    },
}
logging.config.dictConfig(logging_config)
