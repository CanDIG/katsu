from django.apps import AppConfig


class MohpacketsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "chord_metadata_service.mohpackets"

    def ready(self):
        from . import signals  # noqa: F401
