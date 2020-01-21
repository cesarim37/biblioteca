"""Loan forms."""

# Django
from django import forms

# Models
from loan.models import Prestamo
from catalog.models import EjemplarLibro


class PrestamoForm(forms.ModelForm):

    class Meta:

        model = Prestamo
        fields = (
            'bibliotecario',
            'ejemplar',
            'lector',
            'tipo_prestamo',
            'fecha_prestamo',
            'fecha_devolucion',
            'fecha_devuelto',
        )


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

