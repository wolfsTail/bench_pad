from django.apps import AppConfig


class DjAppAccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dj_app_accounts'

    def ready(self):
        import dj_app_accounts.signals
