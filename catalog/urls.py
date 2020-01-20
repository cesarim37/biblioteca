"""Catalog URLs."""

# Django
from django.urls import path

# Views
from catalog import views

urlpatterns = [

    path(
        route='',
        view = views.home,
        name='home'
    ),

    path(
        route='nuevo_autor/',
        view=views.NuevoAutorView.as_view(),
        name='nuevo_autor'
    ),
    path(
        route='crear_autor/',
        view=views.CrearAutorView.as_view(),
        name='crear_autor'
    ),
    path(
        route='listar_autor/',
        view=views.ListadoAutorView.as_view(),
        name='listar_autor'
    ),
    path(
        route='editar_autor/<int:pk>/',
        view=views.ActualizarAutorView.as_view(),
        name='editar_autor'
    ),
    path(
        route='eliminar_autor/<int:pk>/',
        view=views.EliminarAutorView.as_view(),
        name='eliminar_autor'
    ),


    path(
        route='crear_libro/',
        view=views.CrearLibroView.as_view(),
        name='crear_libro'
    ),
    path(
        route='listar_libros/',
        view=views.ListadoLibrosView.as_view(),
        name='listar_libros'
    ),
    path(
        route='editar_libro/<int:pk>/',
        view=views.ActualizarLibroView.as_view(),
        name='editar_libro'
    ),
    path(
        route='eliminar_libro/<int:pk>/',
        view=views.EliminarLibroView.as_view(),
        name='eliminar_libro'
    ),


    path(
        route='<slug:slug>/<int:pk>/',
        view= views.LibroDetailView.as_view(),
        name='libro_detail'
    ),
    path(
        route='crear_ejemplar/',
        view=views.CrearEjemplarView.as_view(),
        name='crear_ejemplar'
    ),

]