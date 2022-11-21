from django.apps import AppConfig
AppConfig.default = False
class BertmodelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.bertModel'
