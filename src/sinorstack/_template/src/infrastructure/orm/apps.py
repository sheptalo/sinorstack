from django.apps.config import AppConfig


class OrmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'infrastructure.orm'
    label = "orm"

