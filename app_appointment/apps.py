from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppQueuingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_appointment'
    verbose_name = _('Appointments module')
