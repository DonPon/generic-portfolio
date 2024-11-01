# web_apps/index/apps.py
from django.apps import AppConfig

class PersonalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web_apps.portfolio_index'  # Correctly points to the index app