from django.apps import AppConfig

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

class HomeConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
  