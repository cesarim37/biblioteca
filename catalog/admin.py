from django.contrib import admin
from .models import *


########### MATERIAL BIBLIOGRAFICO ###########

class EjemplarLibroInline(admin.StackedInline):
    model = EjemplarLibro
    extra = 0
    verbose_name_plural = 'Ejemplares'


class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria')
    inlines = (EjemplarLibroInline,)
    filter_horizontal = ('autor',)


########### MATERIAL NO BIBLIOGRAFICO ###########

class EjemplarMaterialInline(admin.StackedInline):
    model = EjemplarMaterial
    extra = 0
    verbose_name_plural = 'Ejemplar Material'


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('material', 'categoria')
    inlines = (EjemplarMaterialInline,)


########### MATERIAL BIBLIOGRAFICO ###########
admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Ubicacion)
admin.site.register(Libro, LibroAdmin)
admin.site.register(EjemplarLibro)
########### MATERIAL NO BIBLIOGRAFICO ###########
admin.site.register(Material, MaterialAdmin)
admin.site.register(EjemplarMaterial)
