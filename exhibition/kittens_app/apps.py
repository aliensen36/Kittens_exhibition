from django.apps import AppConfig


class KittensAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kittens_app'

    def ready(self):
        import kittens_app.schema

