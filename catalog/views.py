from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, UpdateView, DeleteView, DetailView, ListView

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied

from catalog.forms import AutorForm, EditorialForm, UbicacionForm, LibroForm, EjemplarLibroForm, MaterialForm, EjemplarMaterialForm
from catalog.models import Autor, Editorial, Ubicacion, Libro, EjemplarLibro, Material


def home(request):
    return render(request, 'home.html', {})

##############################################
########### MATERIAL BIBLIOGRAFICO ###########
##############################################

########## CRUD de Autores ##########

class ListadoAutorView(PermissionRequiredMixin, ListView):
    permission_required = ['catalog.view_autor']

    model = Autor
    template_name = 'catalog/autor/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(status = True)


class CrearAutorView(PermissionRequiredMixin, CreateView):
    permission_required = ['catalog.view_autor', 'catalog.add_autor']

    template_name = 'catalog/autor/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('catalog:listar_autor')
    extra_context = {'title': 'Registro'}


class ActualizarAutorView(PermissionRequiredMixin, UpdateView):
    permission_required = ['catalog.view_autor', 'catalog.change_autor']

    model = Autor
    form_class = AutorForm
    template_name = 'catalog/autor/crear_autor.html'
    success_url = reverse_lazy('catalog:listar_autor')
    extra_context = {'title': 'Actualización'}


class EliminarAutorView(PermissionRequiredMixin, DeleteView):
    permission_required = ['catalog.view_autor', 'catalog.delete_autor']

    model = Autor
    template_name = 'catalog/autor/autor_confirm_delete.html'

    def post(self,request,pk,*args,**kwargs):
        object = Autor.objects.get(id = pk)
        object.status = False
        object.save()
        return redirect('catalog:listar_autor')


########## CRUD de Editoriales ##########

class ListadoEditorialView(PermissionRequiredMixin, ListView):
    permission_required = ['catalog.view_editorial']

    model = Editorial
    template_name = 'catalog/editorial/listar_editorial.html'
    context_object_name = 'editoriales'
    queryset = Editorial.objects.filter(status = True)


class CrearEditorialView(PermissionRequiredMixin, CreateView):
    permission_required = ['catalog.view_editorial', 'catalog.add_editorial']

    template_name = 'catalog/editorial/crear_editorial.html'
    form_class = EditorialForm
    success_url = reverse_lazy('catalog:listar_editorial')
    extra_context = {'title': 'Registro'}


class ActualizarEditorialView(PermissionRequiredMixin, UpdateView):
    permission_required = ['catalog.view_editorial', 'catalog.change_editorial']

    model = Editorial
    form_class = EditorialForm
    template_name = 'catalog/editorial/crear_editorial.html'
    success_url = reverse_lazy('catalog:listar_editorial')
    extra_context = {'title': 'Actualización'}


class EliminarEditorialView(PermissionRequiredMixin, DeleteView):
    permission_required = ['catalog.view_editorial', 'catalog.delete_editorial']

    model = Editorial
    template_name = 'catalog/editorial/editorial_confirm_delete.html'

    def post(self,request,pk,*args,**kwargs):
        object = Editorial.objects.get(id = pk)
        object.status = False
        object.save()
        return redirect('catalog:listar_editorial')


########## CRUD de Ubicación ##########

class ListadoUbicacionView(PermissionRequiredMixin, ListView):
    permission_required = ['catalog.view_ubicacion']

    model = Ubicacion
    template_name = 'catalog/ubicacion/listar_ubicacion.html'
    context_object_name = 'ubicaciones'
    queryset = Ubicacion.objects.filter(status = True)


class CrearUbicacionView(PermissionRequiredMixin, CreateView):
    permission_required = ['catalog.view_ubicacion', 'catalog.add_ubicacion']

    template_name = 'catalog/ubicacion/crear_ubicacion.html'
    form_class = UbicacionForm
    success_url = reverse_lazy('catalog:listar_ubicacion')
    extra_context = {'title': 'Registro'}


class ActualizarUbicacionView(PermissionRequiredMixin, UpdateView):
    permission_required = ['catalog.view_ubicacion', 'catalog.change_ubicacion']

    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'catalog/ubicacion/crear_ubicacion.html'
    success_url = reverse_lazy('catalog:listar_ubicacion')
    extra_context = {'title': 'Actualización'}


class EliminarUbicacionView(PermissionRequiredMixin, DeleteView):
    permission_required = ['catalog.view_ubicacion', 'catalog.delete_ubicacion']

    model = Ubicacion
    template_name = 'catalog/ubicacion/ubicacion_confirm_delete.html'

    def post(self,request,pk,*args,**kwargs):
        object = Ubicacion.objects.get(id = pk)
        object.status = False
        object.save()
        return redirect('catalog:listar_ubicacion')


########## CRUD de Libros ##########

class ListadoLibrosView(PermissionRequiredMixin, ListView):
    permission_required = ['catalog.view_libro']

    model = Libro
    template_name = 'catalog/libros/listar_libro.html'
    context_object_name = 'libros'
    queryset = Libro.objects.filter(status = True)


class CrearLibroView(PermissionRequiredMixin, CreateView):
    permission_required = ['catalog.view_libro', 'catalog.add_libro']

    template_name = 'catalog/libros/crear_libro.html'
    form_class = LibroForm
    success_url = reverse_lazy('catalog:listar_libros')
    extra_context = {'title': 'Registro'}


class ActualizarLibroView(PermissionRequiredMixin, UpdateView):
    permission_required = ['catalog.view_libro', 'catalog.change_libro']

    model = Libro
    form_class = LibroForm
    template_name = 'catalog/libros/crear_libro.html'
    success_url = reverse_lazy('catalog:listar_libros')
    extra_context = {'title': 'Actualización'}


class EliminarLibroView(PermissionRequiredMixin, DeleteView):
    permission_required = ['catalog.view_libro', 'catalog.delete_libro']

    model = Libro
    template_name = 'catalog/libros/libro_confirm_delete.html'

    def post(self,request,pk,*args,**kwargs):
        object = Libro.objects.get(id = pk)
        object.status = False
        object.save()
        return redirect('catalog:listar_libros')


########## Detalles de Libro ##########

class LibroDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ['catalog.view_libro']

    model = Libro
    template_name = 'catalog/libros/libro_detail.html'


########## CRUD de Ejemplares ##########

class CrearEjemplarView(PermissionRequiredMixin, CreateView):
    permission_required = ['catalog.view_ejemplarlibro', 'catalog.view_ejemplarlibro']

    template_name = 'catalog/crear_ejemplar.html'
    form_class = EjemplarLibroForm
    success_url = reverse_lazy('catalog:listar_libros')
    extra_context = {'title': 'Registro'}

    def get_initial(self):
        
        initial = super(CrearEjemplarView, self).get_initial()
        print(self.kwargs)
        initial.update({'libro': get_object_or_404(Libro, pk=self.kwargs['pk'])})
        return initial


#################################################
########### MATERIAL NO BIBLIOGRAFICO ###########
#################################################

########## CRUD de Material ##########

class ListadoMaterialView(PermissionRequiredMixin, ListView):
    permission_required = ['catalog.view_material']

    model = Material
    template_name = 'catalog/material/listar_material.html'
    context_object_name = 'materiales'
    queryset = Material.objects.filter(status = True)


class CrearMaterialView(PermissionRequiredMixin, CreateView):
    permission_required = ['catalog.view_material', 'catalog.add_material']
    
    template_name = 'catalog/material/crear_material.html'
    form_class = MaterialForm
    success_url = reverse_lazy('catalog:listar_material')
    extra_context = {'title': 'Registro'}


class ActualizarMaterialView(PermissionRequiredMixin, UpdateView):
    permission_required = ['catalog.view_material', 'catalog.change_material']

    model = Material
    form_class = MaterialForm
    template_name = 'catalog/material/crear_material.html'
    success_url = reverse_lazy('catalog:listar_material')
    extra_context = {'title': 'Actualización'}


class EliminarMaterialView(PermissionRequiredMixin, DeleteView):
    permission_required = ['catalog.view_material', 'catalog.delete_material']

    model = Material
    template_name = 'catalog/material/material_confirm_delete.html'

    def post(self,request,pk,*args,**kwargs):
        object = Material.objects.get(id = pk)
        object.status = False
        object.save()
        return redirect('catalog:listar_material')


########## Detalles de Material ##########

class MaterialDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ['catalog.view_material']

    model = Material
    template_name = 'catalog/material/material_detail.html'


########## CRUD de Ejemplares Material ##########

class CrearEjemplarMaterialView(PermissionRequiredMixin, CreateView):
    permission_required = ['catalog.view_ejemplarmaterial', 'catalog.add_ejemplarmaterial']

    template_name = 'catalog/crear_ejemplar_material.html'
    form_class = EjemplarMaterialForm
    success_url = reverse_lazy('catalog:listar_material')
    extra_context = {'title': 'Registro'}

    def get_initial(self):
        
        initial = super(CrearEjemplarMaterialView, self).get_initial()
        print(self.kwargs)
        initial.update({'material': get_object_or_404(Material, pk=self.kwargs['pk'])})
        return initial