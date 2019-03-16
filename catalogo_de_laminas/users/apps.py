from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "catalogo_de_laminas.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
