from django.contrib import admin
from .models import baterias, filtros, aceites , Comment   #importacion de modelos

model = baterias, filtros, aceites , Comment               #los agregamos a una variable

admin.site.register(model)                                 #registro en nuestro sitio o BD
