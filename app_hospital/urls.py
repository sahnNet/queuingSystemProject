from django.urls import path
from .views import appointment_view, doctor_page_view

urlpatterns = [
    path('appointment', appointment_view, name='appointmentView'),
    path('doctor-page/<d>', doctor_page_view, name='doctorPageView'),
]
