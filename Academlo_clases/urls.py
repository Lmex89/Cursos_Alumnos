"""Academlo_clases URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from Clases.views import Alumnos_view, get_alumno, get_clases_view, get_clases_detalle

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Alumnos/', Alumnos_view),
    path('Alumnos/<pk>', get_alumno),
    path('Clases/', get_clases_view),
    path('Clases/<pk>', get_clases_detalle),

]
