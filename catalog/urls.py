"""Catalog URLs."""

# Django
from django.urls import path
from django.contrib.auth.decorators import login_required
# Views
from catalog import views

urlpatterns = [

    path(
        route='',
        view = views.home,
        name='home'
    ),

    #################################################
    ############ MATERIAL BIBLIOGRAFICO #############
    #################################################

    ########## CRUD de Autor ##########
    path(
        route='listar_autor/',
        view=login_required(views.ListadoAutorView.as_view()),
        name='listar_autor'
    ),
    path(
        route='crear_autor/',
        view=login_required(views.CrearAutorView.as_view()),
        name='crear_autor'
    ),
    path(
        route='editar_autor/<int:pk>/',
        view=login_required(views.ActualizarAutorView.as_view()),
        name='editar_autor'
    ),
    path(
        route='eliminar_autor/<int:pk>/',
        view=login_required(views.EliminarAutorView.as_view()),
        name='eliminar_autor'
    ),

    ########## CRUD de Editorial ##########
    path(
        route='listar_editorial/',
        view=login_required(views.ListadoEditorialView.as_view()),
        name='listar_editorial'
    ),
    path(
        route='crear_editorial/',
        view=login_required(views.CrearEditorialView.as_view()),
        name='crear_editorial'
    ),
    path(
        route='editar_editorial/<int:pk>/',
        view=login_required(views.ActualizarEditorialView.as_view()),
        name='editar_editorial'
    ),
    path(
        route='eliminar_editorial/<int:pk>/',
        view=login_required(views.EliminarEditorialView.as_view()),
        name='eliminar_editorial'
    ),

    ########## CRUD de Ubicación ##########
    path(
        route='listar_ubicacion/',
        view=login_required(views.ListadoUbicacionView.as_view()),
        name='listar_ubicacion'
    ),
    path(
        route='crear_ubicacion/',
        view=login_required(views.CrearUbicacionView.as_view()),
        name='crear_ubicacion'
    ),
    path(
        route='editar_ubicacion/<int:pk>/',
        view=login_required(views.ActualizarUbicacionView.as_view()),
        name='editar_ubicacion'
    ),
    path(
        route='eliminar_ubicacion/<int:pk>/',
        view=login_required(views.EliminarUbicacionView.as_view()),
        name='eliminar_ubicacion'
    ),

    ########## CRUD de Libro ##########
    path(
        route='listar_libros/',
        view=login_required(views.ListadoLibrosView.as_view()),
        name='listar_libros'
    ),
    path(
        route='crear_libro/',
        view=login_required(views.CrearLibroView.as_view()),
        name='crear_libro'
    ),
    path(
        route='editar_libro/<int:pk>/',
        view=login_required(views.ActualizarLibroView.as_view()),
        name='editar_libro'
    ),
    path(
        route='eliminar_libro/<int:pk>/',
        view=login_required(views.EliminarLibroView.as_view()),
        name='eliminar_libro'
    ),

    ########## Detalles de Libro ##########
    path(
        route='detalle_libro/<slug:slug>/<int:pk>/',
        view=login_required(views.LibroDetailView.as_view()),
        name='libro_detail'
    ),

    ########## CRUD de Ejemplares ##########
    path(
        route='crear_ejemplar/<int:pk>/',
        view=login_required(views.CrearEjemplarView.as_view()),
        name='crear_ejemplar'
    ),

    #################################################
    ########### MATERIAL NO BIBLIOGRAFICO ###########
    #################################################

    ########## CRUD de Material ##########
    path(
        route='listar_material/',
        view=login_required(views.ListadoMaterialView.as_view()),
        name='listar_material'
    ),
    path(
        route='crear_material/',
        view=login_required(views.CrearMaterialView.as_view()),
        name='crear_material'
    ),
    path(
        route='editar_material/<int:pk>/',
        view=login_required(views.ActualizarMaterialView.as_view()),
        name='editar_material'
    ),
    path(
        route='eliminar_material/<int:pk>/',
        view=login_required(views.EliminarMaterialView.as_view()),
        name='eliminar_material'
    ),

    ########## Detalles de Material ##########
    path(
        route='detalle_material/<slug:slug>/<int:pk>/',
        view=login_required(views.MaterialDetailView.as_view()),
        name='material_detail'
    ),

    ########## CRUD de Ejemplares ##########
    path(
        route='crear_ejemplar_material/<int:pk>/',
        view=login_required(views.CrearEjemplarMaterialView.as_view()),
        name='crear_ejemplar_material'
    ),
]