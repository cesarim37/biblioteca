"""Account forms."""

# Django
from django import forms
from django.contrib.auth.models import User

# Models
from account.models import Perfil, Estudiante, Personal, Bibliotecario,\
    Visitante


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
        min_length=7,
        max_length=12,
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
        label='Turno',
        max_length=20,
        widget=forms.Select(choices=TURNO),
    )

    def __init__(self, *args, **kwargs):
        super(EstudianteForm, self).__init__(*args, **kwargs)
        inicial = kwargs.get('initial', None)
        if inicial:
            estudiante = inicial['estudiante']

            self.fields['first_name'].initial = estudiante.perfil.usuario.\
                first_name
            self.fields['last_name'].initial = estudiante.perfil.usuario.\
                last_name
            self.fields['cedula_identidad'].initial = estudiante.perfil.\
                cedula_identidad
            self.fields['grado'].initial = estudiante.grado
            self.fields['seccion'].initial = estudiante.seccion
            self.fields['turno'].initial = estudiante.turno
            self.pre_user = estudiante
        else:
            self.pre_user = None

    def clean(self):
        """Cedula debe ser unica."""
        data = super().clean()
        if self.pre_user:
            pre_ci = self.pre_user.perfil.cedula_identidad
            ci = self.cleaned_data['cedula_identidad']

            if pre_ci == ci:
                return data

        cedula_identidad = self.cleaned_data['cedula_identidad']
        cedula_existente = Perfil.objects.filter(
            cedula_identidad=cedula_identidad).exists()
        if cedula_existente:
            raise forms.ValidationError(
                'Tu cédula se encuentra registrada. Verifica los datos')
        return data

    def save(self):
        # Creando usuario y perfil
        data_cleaned = self.cleaned_data
        estudiante = self.pre_user

        if estudiante is not None:
            print(estudiante)
            estudiante.perfil.usuario.username = data_cleaned['cedula_identidad']
            estudiante.perfil.usuario.first_name = data_cleaned['first_name']
            estudiante.perfil.usuario.last_name = data_cleaned['last_name']
            estudiante.perfil.usuario.save()
            estudiante.perfil.cedula_identidad = data_cleaned['cedula_identidad']
            estudiante.perfil.save()
            estudiante.grado = data_cleaned['grado']
            estudiante.seccion = data_cleaned['seccion']
            estudiante.turno = data_cleaned['turno']
            estudiante.save()
        else:
            first_name = data_cleaned['first_name']
            last_name = data_cleaned['last_name']
            cedula_identidad = data_cleaned['cedula_identidad']
            grado = data_cleaned['grado']
            seccion = data_cleaned['seccion']
            turno = data_cleaned['turno']

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
        min_length=7,
        max_length=12,
        required=True
    )

    TIPO = (
        ('docente', 'Docente'),
        ('obrero', 'Obrero'),
        ('administrativo', 'Administrativo'),
    )
    tipo = forms.CharField(
        label='Tipo',
        max_length=20,
        widget=forms.Select(choices=TIPO),
    )

    def __init__(self, *args, **kwargs):
        super(PersonalForm, self).__init__(*args, **kwargs)
        inicial = kwargs.get('initial', None)

        if inicial:
            personal = inicial['personal']

            self.fields['first_name'].initial = personal.perfil.usuario.\
                first_name
            self.fields['last_name'].initial = personal.perfil.usuario.\
                last_name
            self.fields['cedula_identidad'].initial = personal.perfil.\
                cedula_identidad
            self.fields['tipo'].initial = personal.tipo
            self.pre_user = personal
        else:
            self.pre_user = None

    def clean(self):
        """Cedula debe ser unica."""
        data = super().clean()
        if self.pre_user:
            pre_ci = self.pre_user.perfil.cedula_identidad
            ci = self.cleaned_data['cedula_identidad']

            if pre_ci == ci:
                return data

        cedula_identidad = self.cleaned_data['cedula_identidad']
        cedula_existente = Perfil.objects.filter(
            cedula_identidad=cedula_identidad).exists()
        if cedula_existente:
            raise forms.ValidationError(
                'Tu cédula se encuentra registrada. Verifica los datos')
        return data

    def save(self):
        # Creando usuario y perfil

        data_cleaned = self.cleaned_data
        personal = self.pre_user

        if personal is not None:
            personal.perfil.usuario.username = data_cleaned['cedula_identidad']
            personal.perfil.usuario.first_name = data_cleaned['first_name']
            personal.perfil.usuario.last_name = data_cleaned['last_name']
            personal.perfil.usuario.save()
            personal.perfil.cedula_identidad = data_cleaned['cedula_identidad']
            personal.perfil.save()
            personal.tipo = data_cleaned['tipo']
            personal.save()
        else:
            first_name = data_cleaned['first_name']
            last_name = data_cleaned['last_name']
            cedula_identidad = data_cleaned['cedula_identidad']
            tipo = data_cleaned['tipo']

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
        min_length=7,
        max_length=12,
        required=True
    )

    direccion = forms.CharField(
        label='Dirección',
        max_length=200,
        required=True
    )

    telefono = forms.CharField(
        label='Teléfono',
        max_length=20,
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(VisitanteForm, self).__init__(*args, **kwargs)
        inicial = kwargs.get('initial', None)

        if inicial:
            visitante = inicial['visitante']

            self.fields['first_name'].initial = visitante.perfil.usuario.\
                first_name
            self.fields['last_name'].initial = visitante.perfil.usuario.\
                last_name
            self.fields['cedula_identidad'].initial = visitante.perfil.\
                cedula_identidad
            self.fields['direccion'].initial = visitante.direccion
            self.fields['telefono'].initial = visitante.telefono
            self.pre_user = visitante
        else:
            self.pre_user = None

    def clean(self):
        """Cedula debe ser unica."""
        data = super().clean()
        if self.pre_user:
            pre_ci = self.pre_user.perfil.cedula_identidad
            ci = self.cleaned_data['cedula_identidad']

            if pre_ci == ci:
                return data

        cedula_identidad = self.cleaned_data['cedula_identidad']
        cedula_existente = Perfil.objects.filter(
            cedula_identidad=cedula_identidad).exists()
        if cedula_existente:
            raise forms.ValidationError(
                'Tu cédula se encuentra registrada. Verifica los datos')
        return data

    def save(self):
        # Creando usuario y perfil

        data_cleaned = self.cleaned_data
        visitante = self.pre_user

        if visitante is not None:
            visitante.perfil.usuario.username = data_cleaned['cedula_identidad']
            visitante.perfil.usuario.first_name = data_cleaned['first_name']
            visitante.perfil.usuario.last_name = data_cleaned['last_name']
            visitante.perfil.usuario.save()
            visitante.perfil.cedula_identidad = data_cleaned['cedula_identidad']
            visitante.perfil.save()
            visitante.direccion = data_cleaned['direccion']
            visitante.telefono = data_cleaned['telefono']
            visitante.save()
        else:
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
        min_length=7,
        max_length=12,
        required=True
    )

    email = forms.CharField(
        label='E-mail',
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(),
        required=True
    )
    password = forms.CharField(
        label='Contraseña',
        max_length=70,
        widget=forms.PasswordInput(),
        required=True
    )
    password_confirmation = forms.CharField(
        label='Confirmar contraseña',
        max_length=70,
        widget=forms.PasswordInput(),
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
        label='Teléfono',
        max_length=20,
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(BibliotecarioForm, self).__init__(*args, **kwargs)

    def clean(self):
        # Cedula debe ser unica.

        data = super().clean()
        cedula_identidad = self.cleaned_data['cedula_identidad']
        cedula_existente = Perfil.objects.filter(
            cedula_identidad=cedula_identidad).exists()

        if cedula_existente:
            raise forms.ValidationError(
                'Tu cédula se encuentra registrada. Verifica los datos')

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('La contraseña no coincide')
        return data

    def clean_email(self):
        """Email must be unique."""
        email = self.cleaned_data['email']
        email_taken = User.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError(
                'El email ya se encuentra en uso. Prueba otro!')
        return email

    def save(self):
        # Creando usuario y perfil

        data = self.cleaned_data

        first_name = data['first_name']
        last_name = data['last_name']
        cedula_identidad = data['cedula_identidad']
        email = data['email']
        password = data['password']
        imagen = data['imagen']
        direccion = data['direccion']
        telefono = data['telefono']

        user = User.objects.create_user(
            username=cedula_identidad,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
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


class LoginForm(forms.Form):
    cedula = forms.CharField(
        label='Cedula',
        min_length=7,
        max_length=12,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Cedula',
            }
        ))

    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña'
            }
        ))

    def __init__(self, request=None, *args, **kwargs):
        # The 'request' parameter is set for custom auth use by subclasses.
        # The form data comes in via the standard 'data' kwarg.

        self.request = request
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)
