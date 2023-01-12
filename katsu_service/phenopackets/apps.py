from django.apps import AppConfig


class PhenopacketsConfig(AppConfig):
    name = 'katsu_service.phenopackets'

    def ready(self):
        import katsu_service.phenopackets.signals  # noqa: F401
