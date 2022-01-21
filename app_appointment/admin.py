from django.contrib import admin
from .models import Appointment


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'doctor', 'shift', 'turn_number']

    class Meta:
        model = Appointment


admin.site.register(Appointment, AppointmentAdmin)
