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

    ########## CRUD de Autor ##########
    path(
        route='listar_autor/',
        view=views.ListadoAutorView.as_view(),
        name='listar_autor'
    ),
    path(
        route='crear_autor/',
        view=views.CrearAutorView.as_view(),
        name='crear_autor'
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

    ########## CRUD de Editorial ##########
    path(
        route='listar_editorial/',
        view=views.ListadoEditorialView.as_view(),
        name='listar_editorial'
    ),
    path(
        route='crear_editorial/',
        view=views.CrearEditorialView.as_view(),
        name='crear_editorial'
    ),
    path(
        route='editar_editorial/<int:pk>/',
        view=views.ActualizarEditorialView.as_view(),
        name='editar_editorial'
    ),
    path(
        route='eliminar_editorial/<int:pk>/',
        view=views.EliminarEditorialView.as_view(),
        name='eliminar_editorial'
    ),

    ########## CRUD de Ubicación ##########
    path(
        route='listar_ubicacion/',
        view=views.ListadoUbicacionView.as_view(),
        name='listar_ubicacion'
    ),
    path(
        route='crear_ubicacion/',
        view=views.CrearUbicacionView.as_view(),
        name='crear_ubicacion'
    ),
    path(
        route='editar_ubicacion/<int:pk>/',
        view=views.ActualizarUbicacionView.as_view(),
        name='editar_ubicacion'
    ),
    path(
        route='eliminar_ubicacion/<int:pk>/',
        view=views.EliminarUbicacionView.as_view(),
        name='eliminar_ubicacion'
    ),

    ########## CRUD de Libro ##########
    path(
        route='listar_libros/',
        view=views.ListadoLibrosView.as_view(),
        name='listar_libros'
    ),
    path(
        route='crear_libro/',
        view=views.CrearLibroView.as_view(),
        name='crear_libro'
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

    ########## Detalles de Libro ##########
    path(
        route='<slug:slug>/<int:pk>/',
        view= views.LibroDetailView.as_view(),
        name='libro_detail'
    ),

    ########## CRUD de Ejemplares ##########
    path(
        route='crear_ejemplar/',
        view=views.CrearEjemplarView.as_view(),
        name='crear_ejemplar'
    ),

]