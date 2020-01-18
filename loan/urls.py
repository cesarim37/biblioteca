"""Loan URLs."""

# Django
from django.urls import path

# Views
from loan import views

urlpatterns = [

    path(
        route='crear_prestamo/',
        view=views.CrearPrestamoView.as_view(),
        name='crear_prestamo'
    ),

    path(
        route='nuevo_prestamo/<int:pk>/<slug:slug>/',
        view=views.NuevoPrestamoView.as_view(),
        name='nuevo_prestamo'
    ),

    path(
        route='listar_prestamos/',
        view=views.ListadoPrestamoView.as_view(),
        name='listar_prestamos'
    ),

]