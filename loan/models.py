from django.db import models
from django.contrib.auth.models import User

from account.models import Perfil, Bibliotecario
from catalog.models import EjemplarLibro


class ModeloBase(models.Model):
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de Modificación', auto_now=True, auto_now_add=False)
    
    class Meta:
        abstract = True


class Prestamo(ModeloBase):

    bibliotecario = models.ForeignKey(Bibliotecario, on_delete=models.CASCADE, related_name='prestamo_bibliotecario')
    ejemplar = models.ForeignKey(EjemplarLibro, on_delete=models.CASCADE, related_name='prestamo_ejemplar')
    lector = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='prestamo_user')

    TIPO_PRESTAMO = (
        ('aula', 'Aula'),
        ('Sala', 'Sala'),
        ('hogar', 'Hogar'),
    )
    tipo_prestamo = models.CharField(max_length=20, choices=TIPO_PRESTAMO, blank=True, default='sala', help_text='Tipo de Prestamo')
    
    fecha_prestamo = models.DateField('Fecha de Prestamo')
    fecha_devolucion = models.DateField('Fecha de Devolución')
    fecha_devuelto = models.DateField('Devuelto', blank=True, null=True)

    class Meta:
        verbose_name='Prestamo'
        verbose_name_plural='Prestamos'

    def __str__(self):
        return '%s, %s' % (self.ejemplar, self.lector)
