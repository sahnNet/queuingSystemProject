"""queuingSystemProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from .views import (home_view,
                    header_view,
                    footer_view,
                    )

urlpatterns = [path('i18n/', include('django.conf.urls.i18n')), ]
urlpatterns += i18n_patterns(
    path('', include('app_account.urls')),
    path('', include('app_contact.urls')),
    path('', include('app_hospital.urls')),
    path('', include('app_appointment.urls')),
    path('', home_view, name='homeView'),
    path('header', header_view, name='headerView'),
    path('footer', footer_view, name='footerView'),
    path('admin/', admin.site.urls),
    prefix_default_language=True,
)

if settings.DEBUG:
    # add root static files
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add root static files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
