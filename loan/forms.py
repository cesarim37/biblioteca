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
        )


class NuevoPrestamoForm(forms.ModelForm):
    ejemplar = forms.ModelChoiceField(
        queryset=EjemplarLibro.objects.filter(estado='disponible'),
        empty_label="Selecciona Ejemplar",
        widget=forms.Select(
            attrs={'class': 'form-control form-control-sm select2'},
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


    def __init__(self, *args, **kwargs):
        super(NuevoPrestamoForm, self).__init__(*args, **kwargs)
        initial = kwargs.get('initial', None)
        self.fields['tipo_prestamo'] = forms.ChoiceField(
            label='Tipo de Prestamo',
            choices=[('', 'sala'),],
            widget=forms.Select(
                attrs={'class': 'form-control form-control-sm'}
            ),
            required=True
        )
