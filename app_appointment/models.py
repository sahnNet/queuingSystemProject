from django.db import models
from jalali_date import date2jalali

from app_hospital.models import Doctor
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'))
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name=_('Doctor'))
    turn_number = models.IntegerField(verbose_name=_('Turn number'))
    shift = models.CharField(max_length=30, verbose_name=_('Shift'))
    visiting_hours = models.CharField(max_length=10, verbose_name=_('Visiting hours'))
    date = models.DateField(verbose_name=_('Date'))

    class Meta:
        verbose_name = _('Appointment')
        verbose_name_plural = _('Appointments')

    def __str__(self):
        return f'{self.id}'

    def get_date_en(self):
        date_en = self.date.strftime('%A %d %B %Y')
        return f"{date_en}"

    def get_date_fa(self):
        date_fa = date2jalali(self.date).strftime('%A %d %B %Y')
        return f"{date_fa}"
