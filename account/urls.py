"""Account URLs."""

# Django
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

# Views
from account import views

urlpatterns = [

    path(
        route='listar_perfil/',
        view=login_required(views.ListadoPerfilView.as_view()),
        name='listar_perfil'
    ),

    path(
        route='crear_estudiante/',
        view=login_required(views.CrearEstudianteView.as_view()),
        name='crear_estudiante'
    ),
    path(
        route='editar_perfil/estudiante/<int:pk>/',
        view=login_required(views.ActualizarEstudianteView.as_view()),
        name='editar_estudiante'
    ),

    path(
        route='crear_personal/',
        view=login_required(views.CrearPersonalView.as_view()),
        name='crear_personal'
    ),
    path(
        route='editar_perfil/personal/<int:pk>/',
        view=login_required(views.ActualizarPersonalView.as_view()),
        name='editar_personal'
    ),

    path(
        route='crear_visitante/',
        view=login_required(views.CrearVisitanteView.as_view()),
        name='crear_visitante'
    ),
    path(
        route='editar_perfil/visitante/<int:pk>/',
        view=login_required(views.ActualizarVisitanteView.as_view()),
        name='editar_visitante'
    ),

    path(
        route='crear_bibliotecario/',
        view=login_required(views.CrearBibliotecarioView.as_view()),
        name='crear_bibliotecario'
    ),
    path(
        route='listar_bibliotecario/',
        view=login_required(views.ListadoBibliotecarioView.as_view()),
        name='listar_bibliotecario'
    ),

    
    path(
        route='eliminar_perfil/<int:pk>/',
        view=login_required(views.EliminarPerfilView.as_view()),
        name='eliminar_perfil'
    ),
    path(
        route='perfil/<slug:slug>/<int:pk>/',
        view=login_required( views.PerfilDetailView.as_view()),
        name='perfil_detail'
    ),


    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=login_required(views.LogoutView.as_view()),
        name='logout'
    ),
]