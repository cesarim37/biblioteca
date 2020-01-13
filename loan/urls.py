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

]