from django.apps import AppConfig


class BoaAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'boa_app'

    def ready(self):
        from . import signals
