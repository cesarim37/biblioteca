"""Account URLs."""

# Django
from django.urls import path

# Views
from account import views

urlpatterns = [

    path(
        route='crear_estudiante/',
        view=views.CrearEstudianteView.as_view(),
        name='crear_estudiante'
    ),
    path(
        route='crear_personal/',
        view=views.CrearPersonalView.as_view(),
        name='crear_personal'
    ),
    path(
        route='crear_visitante/',
        view=views.CrearVisitanteView.as_view(),
        name='crear_visitante'
    ),
    path(
        route='crear_bibliotecario/',
        view=views.CrearBibliotecarioView.as_view(),
        name='crear_bibliotecario'
    ),

    path(
        route='listar_perfil/',
        view=views.ListadoPerfilView.as_view(),
        name='listar_perfil'
    ),

]