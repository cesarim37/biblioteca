from django.contrib import admin
from .models import *


class EjemplarLibroInline(admin.StackedInline):
    model = EjemplarLibro
    extra = 0
    verbose_name_plural = 'Ejemplares'


class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria')
    inlines = (EjemplarLibroInline,)
    filter_horizontal = ('autor',)


admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Ubicacion)
admin.site.register(Libro, LibroAdmin)
admin.site.register(EjemplarLibro)
