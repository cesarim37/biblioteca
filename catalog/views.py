from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, UpdateView, DeleteView, DetailView, ListView

from catalog.forms import AutorForm, LibroForm, EjemplarLibroForm
from catalog.models import Autor, Libro, EjemplarLibro

def home(request):
    return render(request, 'home.html', {})


class CrearAutorView(LoginRequiredMixin, CreateView):

    template_name = 'catalog/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('catalog:listar_autor')


class ListadoAutorView(ListView):
    model = Autor
    template_name = 'catalog/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(status = True)


class ActualizarAutorView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'catalog/crear_autor.html'
    success_url = reverse_lazy('catalog:listar_autor')


class EliminarAutorView(DeleteView):
    model = Autor

    def post(self,request,pk,*args,**kwargs):
        object = Autor.objects.get(id = pk)
        object.status = False
        object.save()
        return redirect('catalog:listar_autor')


class CrearLibroView(CreateView):
    
    template_name = 'catalog/crear_libro.html'
    form_class = LibroForm
    success_url = reverse_lazy('catalog:listar_libros')


class ListadoLibrosView(ListView):
    model = Libro
    template_name = 'catalog/listar_libro.html'
    context_object_name = 'libros'
    queryset = Libro.objects.filter(status = True)


class ActualizarLibroView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'catalog/crear_libro.html'
    success_url = reverse_lazy('catalog:listar_libros')


class EliminarLibroView(DeleteView):
    model = Libro

    def post(self,request,pk,*args,**kwargs):
        object = Libro.objects.get(id = pk)
        object.status = False
        object.save()
        return redirect('catalog:listar_libros')


class LibroDetailView(DetailView):
    model = Libro


class CrearEjemplarView(CreateView):
    
    template_name = 'catalog/crear_ejemplar.html'
    form_class = EjemplarLibroForm
    success_url = reverse_lazy('catalog:listar_libros')
    

class NuevoAutorView(View):

    def get(self, request, *args, **kwargs):

        autor_form = AutorForm()

        return render(request, 'catalog/nuevo_autor.html', {
            'autor_form': autor_form,
        })

        
    def post(self, request, *args, **kwargs):

        autor_form = AutorForm(request.POST)
        
        if autor_form.is_valid():
            
            data = autor_form.cleaned_data

            autor = Autor(**data)
            autor.save()

        return render(request, 'catalog/nuevo_autor.html', {
            'autor_form': autor_form,
        })
