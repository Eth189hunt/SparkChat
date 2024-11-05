from .settings import *

# Hosts
ALLOWED_HOSTS = [
    "0.0.0.0",
    "localhost",
]

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",
        "PORT": 5432,
    }
}

# Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# the VS Code debugger will not work if these apps and middleware are enabled
# USE_DEBUGGER = os.environ.get("USE_DEBUGGER") == "true"
USE_DEBUG_TOOLBAR = True
if USE_DEBUG_TOOLBAR:
    INSTALLED_APPS += ("debug_toolbar",)

    MIDDLEWARE = MIDDLEWARE + ["debug_toolbar.middleware.DebugToolbarMiddleware"]

    TEMPLATES[0]["OPTIONS"]["context_processors"] += ("django.template.context_processors.debug",)

    # Enable all panels except LoggingPanel so django-channels
    # will properly log tracebacks.
    # Taken from https://bit.ly/2MYoZGn and https://bit.ly/3p6l47C
    DEBUG_TOOLBAR_PANELS = [
        "debug_toolbar.panels.cache.CachePanel",
        "debug_toolbar.panels.headers.HeadersPanel",
        "debug_toolbar.panels.history.HistoryPanel",
        "debug_toolbar.panels.profiling.ProfilingPanel",
        "debug_toolbar.panels.redirects.RedirectsPanel",
        "debug_toolbar.panels.request.RequestPanel",
        "debug_toolbar.panels.settings.SettingsPanel",
        "debug_toolbar.panels.signals.SignalsPanel",
        "debug_toolbar.panels.sql.SQLPanel",
        "debug_toolbar.panels.staticfiles.StaticFilesPanel",
        "debug_toolbar.panels.templates.TemplatesPanel",
        "debug_toolbar.panels.timer.TimerPanel",
        "debug_toolbar.panels.versions.VersionsPanel",
        # 'debug_toolbar.panels.logging.LoggingPanel',
        # Disabling this fixes django-channels traceback logging
    ]

    if DEBUG:
        import socket

        hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
        INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "console": {
#             "class": "rich.logging.RichHandler",
#             "formatter": "rich",
#             "level": "DEBUG",
#             "rich_tracebacks": True,
#             "tracebacks_show_locals": True,
#         },
#     },
#     "formatters": {"rich": {"datefmt": "[%Y-%m-%d %X]"}},
#     # Set 'propagate' to False to prevent duplicate logging
#     "loggers": {
#         "django.request": {
#             "handlers": ["console"],
#             "level": "ERROR",
#             "propagate": False,
#         },
#         "django.db": {
#             "handlers": ["console"],
#             "level": "ERROR",
#             "propagate": False,
#         },
#         "django": {
#             "handlers": ["console"],
#             "level": "INFO",
#             "propagate": False,
#         },
#         "langsite": {
#             "handlers": ["console"],
#             "level": "DEBUG",
#             "propagate": False,
#         },
#     },
# }
