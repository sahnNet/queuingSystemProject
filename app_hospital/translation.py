from modeltranslation.translator import translator, TranslationOptions
from .models import (Province,
                     City,
                     Hospital,
                     Specialty,
                     Doctor,
                     )


class ProvinceTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Province, ProvinceTranslationOptions)


class CityTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(City, CityTranslationOptions)


class HospitalTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Hospital, HospitalTranslationOptions)


class SpecialtyTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Specialty, SpecialtyTranslationOptions)


class DoctorTranslationOptions(TranslationOptions):
    fields = ('full_name',)


translator.register(Doctor, DoctorTranslationOptions)
