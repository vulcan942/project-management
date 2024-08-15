from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"

    def ready(self) -> None:
        from .projects import signals as ProjectSignals
        from .tasks import signals as TaskSignals
        return super().ready()
