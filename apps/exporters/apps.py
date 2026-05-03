from django.apps import AppConfig


class ExportersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'apps.exporters'
    label = 'exporters'
    verbose_name = "Exporter"
