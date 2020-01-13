"""Loan forms."""

# Django
from django import forms

# Models
from loan.models import Prestamo


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
        )