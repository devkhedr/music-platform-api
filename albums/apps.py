import imp
from django.apps import AppConfig


class AlbumsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'albums'

    def ready(self):
        import albums.signals
