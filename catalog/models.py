from django.db import models
from django.template.defaultfilters import slugify


class ModeloBase(models.Model):
    status = models.BooleanField('Status', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de Modificación', auto_now=True, auto_now_add=False)
    
    class Meta:
        abstract = True


##############################################
########### MATERIAL BIBLIOGRAFICO ###########
##############################################

class Autor(ModeloBase):

    nombre = models.CharField('Nombres', max_length=100)
    apellido = models.CharField('Apellidos', max_length=100)

    class Meta:
        verbose_name='Autor'
        verbose_name_plural='Autores'

    def __str__(self):
        return '%s, %s' % (self.apellido, self.nombre)


class Editorial(ModeloBase):

    editorial = models.CharField('Editorial', max_length=100, unique=True)

    class Meta:
        verbose_name='Editorial'
        verbose_name_plural='Editoriales'

    def __str__(self):
        return self.editorial


class Ubicacion(ModeloBase):

    ubicacion = models.CharField('Ubicación', max_length=100, unique=True)

    class Meta:
        verbose_name='Ubicacion'
        verbose_name_plural='Ubicacion'

    def __str__(self):
        return self.ubicacion


class Libro(ModeloBase):

    titulo = models.CharField('Título del Libro', max_length=150)
    portada = models.ImageField(
        'Portada del Libro',
        upload_to='catalog/portadas',
        blank=True,
        null=True
    )

    autor = models.ManyToManyField(Autor, related_name='libro_autor')
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name='libro_editorial')
    
    CATEGORIA = (
        ('referencia', 'Referencia'),
        ('complementarios', 'Complementarios'),
        ('recreativos', 'Recreativos'),
        ('textos', 'Textos'),
        ('pedagogicos', 'Pedagógicos'),
        ('publicaciones periodicas', 'Publicaciones Periódicas'),
        ('seccion docentes', 'Sección Docentes'),
    )

    categoria = models.CharField(max_length=20, choices=CATEGORIA, blank=True, help_text='Clasificación Dewey')
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, related_name='libro_ubicacion')

    class Meta:
        verbose_name='Libro'
        verbose_name_plural='Libros'

    def __str__(self):
        return self.titulo

    @property
    def slug(self):
        return slugify(self.titulo)


class EjemplarLibro(ModeloBase):

    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='ejemplar_libro')

    cota = models.CharField('Cota', max_length=100, unique=True)
    
    CONDICION = (
        ('excelente', 'Excelente'),
        ('regular', 'Regular'),
        ('dañado', 'Dañado'),
    )
    condicion = models.CharField(max_length=20, choices=CONDICION, blank=True, help_text='Condicion del ejemplar')

    ADQUIRIDO = (
        ('donacion', 'Donacion'),
        ('comprado', 'Comprado'),
    )
    adquirido = models.CharField(max_length=20, choices=ADQUIRIDO, blank=True, help_text='Como fue adquirido el ejemplar')

    ESTADO = (
        ('disponible', 'Disponible'),
        ('prestado', 'Prestado'),
    )
    estado = models.CharField(max_length=20, choices=ESTADO, blank=True, default='disponible', help_text='Disponibilidad del ejemplar')

    class Meta:
        verbose_name='Ejemplar'
        verbose_name_plural='Ejemplares'

    def __str__(self):
        return '%s, ejemplar: %s' % (self.libro.titulo, self.cota)


#################################################
########### MATERIAL NO BIBLIOGRAFICO ###########
#################################################

class Material(ModeloBase):

    material = models.CharField('Material', max_length=100)
    descripcion = models.CharField('Descripción', max_length=200, blank=True, null=True)

    imagen = models.ImageField(
        'Imagen de Referencia',
        upload_to='catalog/materiales',
        blank=True,
        null=True
    )
    
    CATEGORIA = (
        ('mapas', 'Mapas'),
        ('meni', 'Material Educativo no Impreso'),
        ('juegos', 'Juegos Didácticos'),
        ('otros', 'Otros'),
    )
    categoria = models.CharField(max_length=20, choices=CATEGORIA, blank=True)

    class Meta:
        verbose_name='Material no Bibliografico'
        verbose_name_plural='Material no Bibliografico'

    def __str__(self):
        return self.material

    @property
    def slug(self):
        return slugify(self.material)

class EjemplarMaterial(ModeloBase):

    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='ejemplar_material')
    
    CONDICION = (
        ('excelente', 'Excelente'),
        ('regular', 'Regular'),
        ('dañado', 'Dañado'),
    )
    condicion = models.CharField(max_length=20, choices=CONDICION, blank=True, help_text='Condicion del ejemplar')

    ADQUIRIDO = (
        ('donacion', 'Donacion'),
        ('comprado', 'Comprado'),
    )
    adquirido = models.CharField(max_length=20, choices=ADQUIRIDO, blank=True, help_text='Como fue adquirido el ejemplar')

    ESTADO = (
        ('disponible', 'Disponible'),
        ('prestado', 'Prestado'),
    )
    estado = models.CharField(max_length=20, choices=ESTADO, blank=True, default='disponible', help_text='Disponibilidad del ejemplar')

    class Meta:
        verbose_name='Ejemplar no Bibliografico'
        verbose_name_plural='Ejemplares no Bibliograficos'

    def __str__(self):
        return '%s, ejemplar: %s' % (self.material.material, self.pk)