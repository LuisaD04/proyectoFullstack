from django.contrib import admin
from .models import Voluntarios,Delegados,Proyectos,Categorias,Seguimiento,ZonasRecuperadas

# Register your models here.
admin.site.register(Voluntarios)
admin.site.register(Delegados)
admin.site.register(Proyectos)
admin.site.register(Categorias)
admin.site.register(Seguimiento)
admin.site.register(ZonasRecuperadas)