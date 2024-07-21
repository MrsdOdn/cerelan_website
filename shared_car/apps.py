from django.apps import AppConfig


class SharedCarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shared_car'

    def ready(self):
        import shared_car.signals
