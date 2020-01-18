"""Account URLs."""

# Django
from django.urls import path
# from django.contrib.auth import views as auth_views

# Views
from account import views

urlpatterns = [

    path(
        route='crear_estudiante/',
        view=views.CrearEstudianteView.as_view(),
        name='crear_estudiante'
    ),
    # path(
    #     route='editar_usuario/estudiante/<int:pk>/',
    #     view=views.ActualizarEstudianteView.as_view(),
    #     name='editar_estudiante'
    # ),
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
    path(
        route='perfil/<slug:slug>/<int:pk>/',
        view= views.PerfilDetailView.as_view(),
        name='perfil_detail'
    ),

]