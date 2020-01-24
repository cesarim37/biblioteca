from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, UpdateView, DeleteView, DetailView, ListView

from catalog.forms import AutorForm, EditorialForm, UbicacionForm, LibroForm, EjemplarLibroForm
from catalog.models import Autor, Editorial, Ubicacion, Libro, EjemplarLibro

def home(request):
    return render(request, 'home.html', {})


########## CRUD de Autores ##########

class ListadoAutorView(LoginRequiredMixin, ListView):
    model = Autor
    template_name = 'catalog/autor/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(status = True)


class CrearAutorView(LoginRequiredMixin, CreateView):

    template_name = 'catalog/autor/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('catalog:listar_autor')


class ActualizarAutorView(LoginRequiredMixin, UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'catalog/autor/crear_autor.html'
    success_url = reverse_lazy('catalog:listar_autor')


class EliminarAutorView(LoginRequiredMixin, DeleteView):
    model = Autor
    template_name = 'catalog/autor/autor_confirm_delete.html'

    def post(self,request,pk,*args,**kwargs):
        object = Autor.objects.get(id = pk)
        object.status = False
        object.save()
        return redirect('catalog:listar_autor')


########## CRUD de Editoriales ##########

class ListadoEditorialView(LoginRequiredMixin, ListView):
    model = Editorial
    template_name = 'catalog/editorial/listar_editorial.html'
    context_object_name = 'editoriales'
    queryset = Editorial.objects.filter(status = True)


class CrearEditorialView(LoginRequiredMixin, CreateView):

    template_name = 'catalog/editorial/crear_editorial.html'
    form_class = EditorialForm
    success_url = reverse_lazy('catalog:listar_editorial')


class ActualizarEditorialView(LoginRequiredMixin, UpdateView):
    model = Editorial
    form_class = EditorialForm
    template_name = 'catalog/editorial/crear_editorial.html'
    success_url = reverse_lazy('catalog:listar_editorial')


class EliminarEditorialView(LoginRequiredMixin, DeleteView):
    model = Editorial
    template_name = 'catalog/editorial/editorial_confirm_delete.html'

    def post(self,request,pk,*args,**kwargs):
        object = Editorial.objects.get(id = pk)
        object.status = False
        object.save()
        return redirect('catalog:listar_editorial')


########## CRUD de Ubicación ##########

class ListadoUbicacionView(LoginRequiredMixin, ListView):
    model = Ubicacion
    template_name = 'catalog/ubicacion/listar_ubicacion.html'
    context_object_name = 'ubicaciones'
    queryset = Ubicacion.objects.filter(status = True)


class CrearUbicacionView(LoginRequiredMixin, CreateView):

    template_name = 'catalog/ubicacion/crear_ubicacion.html'
    form_class = UbicacionForm
    success_url = reverse_lazy('catalog:listar_ubicacion')


class ActualizarUbicacionView(LoginRequiredMixin, UpdateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'catalog/ubicacion/crear_ubicacion.html'
    success_url = reverse_lazy('catalog:listar_ubicacion')


class EliminarUbicacionView(LoginRequiredMixin, DeleteView):
    model = Ubicacion
    template_name = 'catalog/ubicacion/ubicacion_confirm_delete.html'

    def post(self,request,pk,*args,**kwargs):
        object = Ubicacion.objects.get(id = pk)
        object.status = False
        object.save()
        return redirect('catalog:listar_ubicacion')


########## CRUD de Libros ##########

class ListadoLibrosView(LoginRequiredMixin, ListView):
    model = Libro
    template_name = 'catalog/libros/listar_libro.html'
    context_object_name = 'libros'
    queryset = Libro.objects.filter(status = True)


class CrearLibroView(LoginRequiredMixin, CreateView):
    
    template_name = 'catalog/libros/crear_libro.html'
    form_class = LibroForm
    success_url = reverse_lazy('catalog:listar_libros')


class ActualizarLibroView(LoginRequiredMixin, UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'catalog/libros/crear_libro.html'
    success_url = reverse_lazy('catalog:listar_libros')


class EliminarLibroView(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = 'catalog/libros/libro_confirm_delete.html'

    def post(self,request,pk,*args,**kwargs):
        object = Libro.objects.get(id = pk)
        object.status = False
        object.save()
        return redirect('catalog:listar_libros')


########## Detalles de Libro ##########

class LibroDetailView(LoginRequiredMixin, DetailView):
    model = Libro
    template_name = 'catalog/libros/libro_detail.html'


########## CRUD de Ejemplares ##########

class CrearEjemplarView(LoginRequiredMixin, CreateView):
    
    template_name = 'catalog/crear_ejemplar.html'
    form_class = EjemplarLibroForm
    success_url = reverse_lazy('catalog:listar_libros')
    

########## CRUD de Material no Bibliografico ##########

# class ListadoLibrosView(LoginRequiredMixin, ListView):
#     model = Libro
#     template_name = 'catalog/listar_libro.html'
#     context_object_name = 'libros'
#     queryset = Libro.objects.filter(status = True)

# class CrearMaterialView(LoginRequiredMixin, CreateView):
    
#     template_name = 'catalog/crear_material.html'
#     form_class = MaterialForm
#     success_url = reverse_lazy('catalog:listar_libros')

# class ActualizarLibroView(LoginRequiredMixin, UpdateView):
#     model = Libro
#     form_class = LibroForm
#     template_name = 'catalog/crear_libro.html'
#     success_url = reverse_lazy('catalog:listar_libros')


# class EliminarLibroView(LoginRequiredMixin, DeleteView):
#     model = Libro

#     def post(self,request,pk,*args,**kwargs):
#         object = Libro.objects.get(id = pk)
#         object.status = False
#         object.save()
#         return redirect('catalog:listar_libros')

