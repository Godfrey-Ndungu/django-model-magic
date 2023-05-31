from django.apps import AppConfig


class ModelMagicConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "model_magic"
