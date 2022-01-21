from django.contrib import admin
from .models import (Province,
                     City,
                     Hospital,
                     Specialty,
                     Doctor,
                     )


class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = Province


admin.site.register(Province, ProvinceAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'province']

    class Meta:
        model = City


admin.site.register(City, CityAdmin)


class HospitalAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']

    class Meta:
        model = Hospital


admin.site.register(Hospital, HospitalAdmin)


class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = Specialty


admin.site.register(Specialty, SpecializationAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'specialty', 'hospital']

    class Meta:
        model = Doctor


admin.site.register(Doctor, DoctorAdmin)
