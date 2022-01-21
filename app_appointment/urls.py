from django.urls import path
from .views import set_appointment_view, some_view

urlpatterns = [
    path('set-appointment', set_appointment_view, name='setAppointmentView'),
    path('get-appointment-file/<a>', some_view, name='someView'),
]
