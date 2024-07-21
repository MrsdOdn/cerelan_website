from django.apps import AppConfig


class MinibusConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'minibus'

    def ready(self):
        import minibus.signals
