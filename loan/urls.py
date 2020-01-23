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
        route='<int:pk_ejemplar>/<int:pk_lector>/devolver_prestamo/',
        view=views.DevolverPrestamoView.as_view(),
        name='devolver_prestamo'
    ),

    path(
        route='listar_prestamos/',
        view=views.ListadoPrestamoView.as_view(),
        name='listar_prestamos'
    ),

    path(
        route='devolucion/',
        view=views.DevolucionView.as_view(),
        name='devolucion'
    ),

]