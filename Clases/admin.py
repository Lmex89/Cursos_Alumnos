from Clases.models import Alumnos
from django.contrib import admin

# Register your models here.

from Clases.models import Clases, Alumnos

admin.site.register(Clases)
admin.site.register(Alumnos)
