"""Loan URLs."""

# Django
from django.urls import path
from django.contrib.auth.decorators import login_required
# Views
from loan import views

urlpatterns = [
    
    ########### MATERIAL BIBLIOGRAFICO ###########
    path(
        route='listar_prestamos/',
        view=login_required(views.ListadoPrestamoView.as_view()),
        name='listar_prestamos'
    ),

    ########### Prestamos/Devolución desde Inicio ###########
    path(
        route='crear_prestamo/',
        view=login_required(views.CrearPrestamoView.as_view()),
        name='crear_prestamo'
    ),
    path(
        route='devolucion/',
        view=login_required(views.DevolucionView.as_view()),
        name='devolucion'
    ),

    ########### Prestamos/Devolución desde Usuario ###########
    path(
        route='nuevo_prestamo/<int:pk>/<slug:slug>/',
        view=login_required(views.NuevoPrestamoView.as_view()),
        name='nuevo_prestamo'
    ),
    path(
        route='devolver_prestamo/<int:pk_ejemplar>/<int:pk_lector>/',
        view=login_required(views.DevolverPrestamoView.as_view()),
        name='devolver_prestamo'
    ),

    #################################################
    ########### MATERIAL NO BIBLIOGRAFICO ###########
    path(
        route='listar_prestamos_material/',
        view=login_required(views.ListadoPrestamoMaterialView.as_view()),
        name='listar_prestamos_material'
    ),

    ########### Prestamos/Devolución de Material ###########
    path(
        route='crear_prestamo_material/',
        view=login_required(views.CrearPrestamoMaterialView.as_view()),
        name='crear_prestamo_material'
    ),
    path(
        route='devolucion_material/',
        view=login_required(views.DevolucionMaterialView.as_view()),
        name='devolucion_material'
    ),

]