from django.apps import AppConfig


class VendorsConfig(AppConfig):
    name = 'apps.vendors'
    label = 'vendors'
    verbose_name = "Vendor"
    default_auto_field = "django.db.models.BigAutoField"
