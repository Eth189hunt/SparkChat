import os

from .settings import *

TESTING = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": "db",
        "PORT": 5432,
    }
}

ALLOWED_HOSTS = [
    # "langplanet.org",
]


# Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = ""
# EMAIL_PORT = "25"
# SERVER_EMAIL = os.environ.get("SERVER_EMAIL", "root@suu.edu")

# CSRF trusted origins
# CSRF_TRUSTED_ORIGINS = ['https://*.langplanet.org']

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "verbose": {
#             "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
#         },
#         "simple": {
#             "format": "%(asctime)s %(levelname)s [%(name)s:%(lineno)s]: %(message)s",
#             "datefmt": "%Y-%m-%dT%H:%M:%S",  # 2015-02-23T05:12:17+00:00
#         },
#     },
#     "handlers": {
#         "syslog": {
#             "level": "INFO",
#             "class": "logging.handlers.SysLogHandler",
#             "formatter": "simple",
#             "address": ("logrelay.suu.edu", 514),
#         },
#         "invalid_host_header": {
#             "level": "ERROR",
#             "class": "logging.FileHandler",
#             "filename": "/var/log/mysuu/invalid_host_header.log",
#         },
#         "local_mysuu_portal": {
#             "level": "INFO",
#             "class": "logging.FileHandler",
#             "filename": "/var/log/mysuu/local_mysuu_portal.log",
#         },
#     },
#     "loggers": {
#         "django.security.DisallowedHost": {
#             "handlers": ["invalid_host_header"],
#             "level": "ERROR",
#             "propagate": False,
#         },
#         "django.request": {
#             "handlers": ["syslog"],
#             "level": "ERROR",
#             "propagate": True,
#         },
#         "django.db.backends": {
#             "handlers": ["syslog"],
#             # Switching this to DEBUG will spit the SQL to the log file only
#             # if DEBUG = True in this file
#             "level": "ERROR",
#         },
#         "portal.approve": {"handlers": ["syslog"], "level": "INFO"},
#         "portal.paperless": {"handlers": ["syslog"], "level": "INFO"},
#         "banner": {"handlers": ["syslog"], "level": "INFO"},
#         "portal.nodeping": {"handlers": ["syslog"], "level": "INFO"},
#     },
# }
