from django.apps import AppConfig


class PatientsConfig(AppConfig):
    name = 'katsu_service.patients'

    def ready(self):
        import katsu_service.patients.signals  # noqa: F401
