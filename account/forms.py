"""Account forms."""

# Django
from django import forms
from django.contrib.auth.models import User

# Models
from account.models import *


class EstudianteForm(forms.Form):

    first_name = forms.CharField(
        label='Nombre',
        min_length=2,
        max_length=50,
        required=True
    )

    last_name = forms.CharField(
        label='Apellido',
        min_length=2,
        max_length=50,
        required=True
    )

    cedula_identidad = forms.CharField(
        label='Cédula de Identidad',
        min_length=2,
        max_length=20,
        required=True
    )

    grado = forms.CharField(
        label='Grado',
        max_length=20,
        required=True
    )

    seccion = forms.CharField(
        label='Sección',
        max_length=20,
        required=True
    )

    TURNO = (
        ('mañana', 'Mañana'),
        ('tarde', 'Tarde'),
    )
    turno = forms.CharField(
        label= 'Turno',
        max_length=20, 
        widget=forms.Select(choices=TURNO),
    )


    def __init__(self, *args, **kwargs):
        super(EstudianteForm, self).__init__(*args, **kwargs)


    def clean(self):
        """Cedula debe ser unica."""
        data = super().clean()

        cedula_identidad = self.cleaned_data['cedula_identidad']
        cedula_existente = Perfil.objects.filter(cedula_identidad=cedula_identidad).exists()

        if cedula_existente:
            raise forms.ValidationError('Tu cedula se encuentra registrada. Verifica los datos')
        return data


    def save(self):
        """Creando usuario y perfil"""

        data = self.cleaned_data

        first_name = data['first_name']
        last_name = data['last_name']
        cedula_identidad = data['cedula_identidad']
        grado = data['grado']
        seccion = data['seccion']
        turno = data['turno']
        
        user = User.objects.create_user(
            username=cedula_identidad,
            first_name=first_name,
            last_name=last_name
        )

        perfil = Perfil(
            usuario=user,
            tipo_usuario='estudiante',
            cedula_identidad=cedula_identidad
            )
        perfil.save()

        estudiante = Estudiante(
            perfil=perfil,
            grado=grado,
            seccion=seccion,
            turno=turno
        )
        estudiante.save()


class PersonalForm(forms.Form):

    first_name = forms.CharField(
        label='Nombre',
        min_length=2,
        max_length=50,
        required=True
    )

    last_name = forms.CharField(
        label='Apellido',
        min_length=2,
        max_length=50,
        required=True
    )

    cedula_identidad = forms.CharField(
        label='Cédula de Identidad',
        min_length=2,
        max_length=20,
        required=True
    )

    TIPO = (
        ('docente', 'Docente'),
        ('obrero', 'Obrero'),
        ('administrativo', 'Administrativo'),
    )
    tipo = forms.CharField(
        label= 'Tipo',
        max_length=20, 
        widget=forms.Select(choices=TIPO),
    )


    def __init__(self, *args, **kwargs):
        super(PersonalForm, self).__init__(*args, **kwargs)


    def clean(self):
        """Cedula debe ser unica."""
        data = super().clean()

        cedula_identidad = self.cleaned_data['cedula_identidad']
        cedula_existente = Perfil.objects.filter(cedula_identidad=cedula_identidad).exists()

        if cedula_existente:
            raise forms.ValidationError('Tu cedula se encuentra registrada. Verifica los datos')
        return data


    def save(self):
        """Creando usuario y perfil"""

        data = self.cleaned_data

        first_name = data['first_name']
        last_name = data['last_name']
        cedula_identidad = data['cedula_identidad']
        tipo = data['tipo']
        
        user = User.objects.create_user(
            username=cedula_identidad,
            first_name=first_name,
            last_name=last_name
        )

        perfil = Perfil(
            usuario=user,
            tipo_usuario='personal',
            cedula_identidad=cedula_identidad
            )
        perfil.save()

        personal = Personal(
            perfil=perfil,
            tipo=tipo
        )
        personal.save()


class VisitanteForm(forms.Form):

    first_name = forms.CharField(
        label='Nombre',
        min_length=2,
        max_length=50,
        required=True
    )

    last_name = forms.CharField(
        label='Apellido',
        min_length=2,
        max_length=50,
        required=True
    )

    cedula_identidad = forms.CharField(
        label='Cédula de Identidad',
        min_length=2,
        max_length=20,
        required=True
    )

    direccion = forms.CharField(
        label='Dirección',
        max_length=200,
        required=True
    )

    telefono = forms.CharField(
        label='Telefono',
        max_length=20,
        required=True
    )


    def __init__(self, *args, **kwargs):
        super(VisitanteForm, self).__init__(*args, **kwargs)


    def clean(self):
        """Cedula debe ser unica."""
        data = super().clean()

        cedula_identidad = self.cleaned_data['cedula_identidad']
        cedula_existente = Perfil.objects.filter(cedula_identidad=cedula_identidad).exists()

        if cedula_existente:
            raise forms.ValidationError('Tu cedula se encuentra registrada. Verifica los datos')
        return data


    def save(self):
        """Creando usuario y perfil"""

        data = self.cleaned_data

        first_name = data['first_name']
        last_name = data['last_name']
        cedula_identidad = data['cedula_identidad']
        direccion = data['direccion']
        telefono = data['telefono']
        
        user = User.objects.create_user(
            username=cedula_identidad,
            first_name=first_name,
            last_name=last_name
        )

        perfil = Perfil(
            usuario=user,
            tipo_usuario='visitante',
            cedula_identidad=cedula_identidad
            )
        perfil.save()

        visitante = Visitante(
            perfil=perfil,
            direccion=direccion,
            telefono=telefono
        )
        visitante.save()


class BibliotecarioForm(forms.Form):

    first_name = forms.CharField(
        label='Nombre',
        min_length=2,
        max_length=50,
        required=True
    )

    last_name = forms.CharField(
        label='Apellido',
        min_length=2,
        max_length=50,
        required=True
    )

    cedula_identidad = forms.CharField(
        label='Cédula de Identidad',
        min_length=2,
        max_length=20,
        required=True
    )

    imagen = forms.ImageField(
        label='Imagen de Perfil',
        required=False
    )

    direccion = forms.CharField(
        label='Dirección',
        max_length=200,
        required=True
    )

    telefono = forms.CharField(
        label='Telefono',
        max_length=20,
        required=True
    )


    def __init__(self, *args, **kwargs):
        super(BibliotecarioForm, self).__init__(*args, **kwargs)


    def clean(self):
        """Cedula debe ser unica."""
        data = super().clean()

        cedula_identidad = self.cleaned_data['cedula_identidad']
        cedula_existente = Perfil.objects.filter(cedula_identidad=cedula_identidad).exists()

        if cedula_existente:
            raise forms.ValidationError('Tu cedula se encuentra registrada. Verifica los datos')
        return data


    def save(self):
        """Creando usuario y perfil"""

        data = self.cleaned_data

        first_name = data['first_name']
        last_name = data['last_name']
        cedula_identidad = data['cedula_identidad']
        imagen = data['imagen']
        direccion = data['direccion']
        telefono = data['telefono']
        
        user = User.objects.create_user(
            username=cedula_identidad,
            first_name=first_name,
            last_name=last_name
        )

        perfil = Perfil(
            usuario=user,
            tipo_usuario='bibliotecario',
            cedula_identidad=cedula_identidad
            )
        perfil.save()

        bibliotecario = Bibliotecario(
            perfil=perfil,
            imagen=imagen,
            direccion=direccion,
            telefono=telefono
        )
        bibliotecario.save()
