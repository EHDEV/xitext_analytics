from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "xitext_analytics.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import xitext_analytics.users.signals  # noqa F401
        except ImportError:
            pass
