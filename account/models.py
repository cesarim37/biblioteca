from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

from catalog.models import EjemplarLibro


class Perfil(models.Model):
    status = models.BooleanField('Status', default = True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_usuario')
    TIPO_DE_USUARIO = (
        ('bibliotecario', 'Bibliotecario'),
        ('estudiante', 'Estudiante'),
        ('personal', 'Personal'),
        ('visitante', 'Visitante'),
    )
    tipo_usuario = models.CharField('Tipo de Usuario', max_length=20, choices=TIPO_DE_USUARIO, default='estudiante')
    cedula_identidad = models.CharField('Cédula de Identidad', max_length=12, unique=True)

    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de Modificación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return self.usuario.username

    @property
    def slug(self):
        return slugify(self.cedula_identidad)
    

class Bibliotecario(models.Model):

    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, related_name='bibliotecario_perfil')
    imagen = models.ImageField(
        'Imagen de Perfil',
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    direccion = models.CharField('Dirección', max_length=200)
    telefono = models.CharField('Teléfono', max_length=20)
    
    class Meta:
        verbose_name = "Bibliotecario"
        verbose_name_plural = "Bibliotecarios"

    def __str__(self):
        return self.perfil.usuario.username


class Estudiante(models.Model):

    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, related_name='estudiante_perfil')
    grado = models.CharField('Grado', max_length=20)
    seccion = models.CharField('Sección', max_length=20)

    TURNO = (
        ('mañana', 'Mañana'),
        ('tarde', 'Tarde'),
    )
    turno = models.CharField('Turno', max_length=20, choices=TURNO, blank=True, default='mañana')

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return self.perfil.usuario.username


class Personal(models.Model):

    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, related_name='personal_perfil')
    TIPO = (
        ('docente', 'Docente'),
        ('obrero', 'Obrero'),
        ('administrativo', 'Administrativo'),
    )
    tipo = models.CharField('Tipo', max_length=20, choices=TIPO, blank=True, default='docente')

    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personal"

    def __str__(self):
        return self.perfil.usuario.username


class Visitante(models.Model):

    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, related_name='visitante_perfil')
    direccion = models.CharField('Dirección', max_length=200)
    telefono = models.CharField('Teléfono', max_length=20)

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"

    def __str__(self):
        return self.perfil.usuario.username
