"""
URL configuration for masini project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include #MODIFICARE PENTRU INCLUDE CA SA INCLUDEM URL URILE IN APLICATIE
from masini import settings
from django.conf.urls.static import static #IMPORTAM STATIC UL DIN DJANGO CA SA NU NE MAI ARUNCE EROAREA DE SETTINGS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('masini_app.urls')),# MODIFICARE SA INCLUDEM URL URILE DIN MASINI_APP
    path('', include('django.contrib.auth.urls')),#MODIFICARE SA INCLUDEM URL URILE DIN DJANGO
]


if settings.DEBUG: #VERIFICAM DACA PROIECTUL NOSTRU RULEAZA IN DEBUG
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL) #ADAUGAM URL URILE PENTRU MEDIA