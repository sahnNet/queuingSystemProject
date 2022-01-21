import os

from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date


def get_file_name_ext(file_path):
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, file_path):
    name, ext = get_file_name_ext(file_path)
    final_name = f"{instance.hospital.name_en}-{instance.specialty.name_en}-{instance.full_name_en}{ext}"
    return f"doctors/{final_name}"


def upload_location_path(instance, file_path):
    name, ext = get_file_name_ext(file_path)
    final_name = f"{instance.name_en}{ext}"
    return f"hospitals/locations/{final_name}"


def get_count_shift(doctor, shift):
    # Date tomorrow
    today = date.today()
    try:
        tomorrow = date(today.year, today.month, today.day + 1)
    except:
        if today.month < 12:
            tomorrow = date(today.year, today.month + 1, 1)
        else:
            tomorrow = date(today.year + 1, 1, 1)
    # /Date tomorrow

    return doctor.appointment_set.filter(date=tomorrow, shift=shift).count()


class Province(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=25)

    class Meta:
        verbose_name = _('Province')
        verbose_name_plural = _('Provinces')

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=25)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name=_('Province'))

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        return self.name


class Hospital(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    telephone_number = models.IntegerField(verbose_name=_('Telephone number'), blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name=_('City'))
    location = models.ImageField(upload_to=upload_location_path, null=True, blank=True, verbose_name=_('Location'))

    class Meta:
        verbose_name = _('Hospital')
        verbose_name_plural = _('Hospitals')

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=25)

    class Meta:
        verbose_name = _('Specialty')
        verbose_name_plural = _('Specialties')

    def __str__(self):
        return self.name


class Doctor(models.Model):
    full_name = models.CharField(verbose_name=_('Full name'), max_length=25)
    email = models.IntegerField(verbose_name=_('Email'), null=True, blank=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name=_('Image'))
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, verbose_name=_('Specialty'))
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, verbose_name=_('Hospital'))
    is_morning_shift = models.BooleanField(default=True, verbose_name=_('Morning shift'))
    is_evening_shift = models.BooleanField(default=True, verbose_name=_('Evening shift'))
    is_night_shift = models.BooleanField(default=True, verbose_name=_('Night shift'))

    class Meta:
        verbose_name = _('Doctor')
        verbose_name_plural = _('Doctors')

    def __str__(self):
        return self.full_name

    def is_full_morning_turn(self, ):
        count = get_count_shift(self, 'morning')

        return count >= 24

    def is_full_evening_turn(self, ):
        count = get_count_shift(self, 'evening')

        return count >= 24

    def is_full_night_turn(self, ):
        count = get_count_shift(self, 'night')

        return count >= 24
