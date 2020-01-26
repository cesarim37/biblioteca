"""Catalog forms."""

# Django
from django import forms

# Models
from catalog.models import Autor, Editorial, Ubicacion, Libro, EjemplarLibro, Material, EjemplarMaterial


##############################################
########### MATERIAL BIBLIOGRAFICO ###########
##############################################

class AutorForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(AutorForm, self).__init__(*args, **kwargs)
        file = []
        for field in self.fields:
            if not (field in file):
                self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:

        model = Autor
        fields = (
            'nombre',
            'apellido',
        )


class EditorialForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(EditorialForm, self).__init__(*args, **kwargs)
        file = []
        for field in self.fields:
            if not (field in file):
                self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:

        model = Editorial
        fields = (
            'editorial',
        )


class UbicacionForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(UbicacionForm, self).__init__(*args, **kwargs)
        file = []
        for field in self.fields:
            if not (field in file):
                self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:

        model = Ubicacion
        fields = (
            'ubicacion',
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
            'ubicacion',
        )

        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }),

            'portada': forms.FileInput(
                attrs={
                    'class': 'custom-file-input',
                    'lang': 'es',
                }),

            'autor': forms.SelectMultiple(
                attrs={
                    'class': 'standardSelect',
                    'data-placeholder': 'Selecciona autor o autores...',
                }),

            'editorial': forms.Select(
                attrs={
                    'class': 'standardSelect',
                    'data-placeholder': 'Selecciona editorial...',
                }),

            'categoria': forms.Select(
                attrs={
                    'class': 'standardSelect',
                    'data-placeholder': 'Selecciona categoria...',
                }),

            'ubicacion': forms.Select(
                attrs={
                    'class': 'standardSelect',
                    'data-placeholder': 'Seleccione ubicación...',
                }),
        }


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


#################################################
########### MATERIAL NO BIBLIOGRAFICO ###########
#################################################

class MaterialForm(forms.ModelForm):

    class Meta:
        model = Material
        
        fields = (
            'material',
            'descripcion',
            'categoria',
        )

        widgets = {
            'material': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }),

            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }),

            'categoria': forms.Select(
                attrs={
                    'class': 'standardSelect',
                    'data-placeholder': 'Selecciona categoria...',
                }),
        }


class EjemplarMaterialForm(forms.ModelForm):

    class Meta:

        model = EjemplarMaterial
        fields = (
            'material',
            'condicion',
            'adquirido',
            'estado',
        )