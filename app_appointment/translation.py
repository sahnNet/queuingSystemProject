from modeltranslation.translator import translator, TranslationOptions
from .models import Appointment


class AppointmentTranslationOptions(TranslationOptions):
    fields = ('shift',)


translator.register(Appointment, AppointmentTranslationOptions)
