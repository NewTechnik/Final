from django.contrib import admin

# Register your models here.
from .models import Alumno
from .models import Contacto

admin.site.register(Alumno)
admin.site.register(Contacto)