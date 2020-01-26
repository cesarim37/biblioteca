"""Loan forms."""

from datetime import datetime
# Django
from django import forms

# Models
from account.models import Perfil
from loan.models import Prestamo
from catalog.models import EjemplarLibro, EjemplarMaterial


now = datetime.now()
x = now.date()

##############################################
########### MATERIAL BIBLIOGRAFICO ###########
##############################################

class PrestamoForm(forms.Form):

    ejemplar = forms.CharField(
        label='Cota del Ejemplar',
        min_length=2,
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                    'class': 'form-control',
                }
        ),
    )

    lector = forms.CharField(
        label='Cedula del Lector',
        min_length=2,
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                    'class': 'form-control',
                }
        ),
    )

    TIPO_PRESTAMO = (
        ('aula', 'Aula'),
        ('sala', 'Sala'),
        ('hogar', 'Hogar'),
    )
    tipo_prestamo = forms.CharField(
        label='Tipo de prestamo',
        max_length=20, 
        widget=forms.Select(
            choices=TIPO_PRESTAMO,
            attrs={
                    'class': 'form-control standardSelect',
                    'data-placeholder': 'Selecciona tipo de prestamo...',
                }
        ),
    )

    fecha_devolucion = forms.DateField(
        label= 'Fecha de Devolución',
        widget=forms.DateInput(
            attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'min': x,
                }
        ),
    )


    def __init__(self, *args, **kwargs):
        super(PrestamoForm, self).__init__(*args, **kwargs)


    def clean(self):
        """Cedula debe ser unica."""
        data = super().clean()

        lector = self.cleaned_data['lector']
        try:
            perfil = Perfil.objects.get(cedula_identidad=lector)
            prestamos = perfil.prestamo_user.filter(fecha_devuelto=None)
        except:
            raise forms.ValidationError('El usuario no existe, verifique la cedula')

        if perfil.tipo_usuario == 'estudiante' and len(prestamos)>0:
            raise forms.ValidationError('El usuario tiene libros pendientes')

        if perfil.tipo_usuario == 'personal' and len(prestamos)>3:
            raise forms.ValidationError('El usuario tiene libros pendientes')

        tipo_prestamo = self.cleaned_data['tipo_prestamo']
        if perfil.tipo_usuario == 'visitante' and tipo_prestamo != 'sala' :
            raise forms.ValidationError('Usuario Visitante, prestamo restringido a sala')

        ejemplar = self.cleaned_data['ejemplar']
        try:
            e = EjemplarLibro.objects.get(cota=ejemplar)
        except:
            raise forms.ValidationError('El ejemplar no existe, verifique la cota')

        if e.estado == 'prestado' or e.condicion == 'dañado':
            raise forms.ValidationError('Este ejemplar no se encuentra disponible')

        return data


class DevolucionForm(forms.Form):

    ejemplar = forms.CharField(
        label='Cota del Ejemplar',
        min_length=2,
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                    'class': 'form-control',
                }
        ),
    )

    def __init__(self, *args, **kwargs):
        super(DevolucionForm, self).__init__(*args, **kwargs)


class NuevoPrestamoForm(forms.ModelForm):
    ejemplar = forms.ModelChoiceField(
        queryset=EjemplarLibro.objects.filter(estado='disponible'),
        empty_label="Selecciona Ejemplar",
        widget=forms.Select(
            attrs={'class': 'form-control standardSelect'},
        ),
        required=True
    )


    class Meta:

        model = Prestamo
        fields = (
            'tipo_prestamo',
            'fecha_prestamo',
            'fecha_devolucion',
        )

        widgets = {
            'tipo_prestamo': forms.Select(
                attrs={
                    'class': 'form-control standardSelect',
                    'data-placeholder': 'Selecciona tipo de prestamo...',
                }),

            'fecha_prestamo': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }),

            'fecha_devolucion': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }),
        }


#################################################
########### MATERIAL NO BIBLIOGRAFICO ###########
#################################################

class PrestamoMaterialForm(forms.Form):

    ejemplar_material = forms.ModelChoiceField(
        queryset=EjemplarMaterial.objects.filter(estado='disponible'),
        empty_label="Selecciona Ejemplar",
        widget=forms.Select(
            attrs={'class': 'form-control standardSelect'},
        ),
        required=True
    )

    lector = forms.CharField(
        label='Cedula del Usuario',
        min_length=2,
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                    'class': 'form-control',
                }
        ),
    )

    TIPO_PRESTAMO = (
        ('aula', 'Aula'),
        ('sala', 'Sala'),
        ('hogar', 'Hogar'),
    )
    tipo_prestamo = forms.CharField(
        label='Tipo de prestamo',
        max_length=20, 
        widget=forms.Select(
            choices=TIPO_PRESTAMO,
            attrs={
                    'class': 'form-control standardSelect',
                    'data-placeholder': 'Selecciona tipo de prestamo...',
                }
        ),
    )

    fecha_devolucion = forms.DateField(
        label= 'Fecha de Devolución',
        widget=forms.DateInput(
            attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'min': x,
                }
        ),
    )


    def __init__(self, *args, **kwargs):
        super(PrestamoMaterialForm, self).__init__(*args, **kwargs)


    def clean(self):
        """Cedula debe ser unica."""
        data = super().clean()

        lector = self.cleaned_data['lector']
        try:
            perfil = Perfil.objects.get(cedula_identidad=lector)
            prestamos = perfil.prestamo_user.filter(fecha_devuelto=None)
        except:
            raise forms.ValidationError('El usuario no existe, verifique la cedula')

        if perfil.tipo_usuario == 'estudiante' and len(prestamos)>0:
            raise forms.ValidationError('El usuario tiene libros pendientes')

        if perfil.tipo_usuario == 'personal' and len(prestamos)>3:
            raise forms.ValidationError('El usuario tiene libros pendientes')

        tipo_prestamo = self.cleaned_data['tipo_prestamo']
        if perfil.tipo_usuario == 'visitante' and tipo_prestamo != 'sala' :
            raise forms.ValidationError('Usuario Visitante, prestamo restringido a sala')

        ejemplar_material = self.cleaned_data['ejemplar_material']
        if ejemplar_material.condicion == 'dañado':
            raise forms.ValidationError('Este ejemplar no se encuentra disponible')

        return data


class DevolucionMaterialForm(forms.Form):

    ejemplar_material = forms.ModelChoiceField(
        queryset=EjemplarMaterial.objects.filter(estado='prestado'),
        empty_label="Selecciona Ejemplar",
        widget=forms.Select(
            attrs={'class': 'form-control standardSelect'},
        ),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(DevolucionMaterialForm, self).__init__(*args, **kwargs)