from django.urls import path
from .views import (contactus_view,)

urlpatterns = [
    path('contact-us', contactus_view, name='contactusView'),
]