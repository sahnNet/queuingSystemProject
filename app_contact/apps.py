from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppContactConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_contact'
    verbose_name = _('Calls module')
