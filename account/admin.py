from django.contrib import admin
from .models import *


class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo_usuario', 'cedula_identidad')
    filter_horizontal = ('libros',)


admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Bibliotecario)
admin.site.register(Estudiante)
admin.site.register(Personal)
admin.site.register(Visitante)
