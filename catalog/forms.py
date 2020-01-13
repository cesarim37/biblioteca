"""Catalog forms."""

# Django
from django import forms

# Models
from catalog.models import Autor, Libro, EjemplarLibro


class AutorForm(forms.ModelForm):

    class Meta:

        model = Autor
        fields = (
            'nombre',
            'apellido',
        )


class LibroForm(forms.ModelForm):

    class Meta:

        model = Libro
        fields = (
            'titulo',
            'portada',
            'autor',
            'editorial',
            'categoria',
            'genero',
            'ubicacion',
        )


class EjemplarLibroForm(forms.ModelForm):

    class Meta:

        model = EjemplarLibro
        fields = (
            'libro',
            'cota',
            'condicion',
            'adquirido',
            'estado',
        )
