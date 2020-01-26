"""Loan URLs."""

# Django
from django.urls import path

# Views
from loan import views

urlpatterns = [
    
    ########### MATERIAL BIBLIOGRAFICO ###########
    path(
        route='listar_prestamos/',
        view=views.ListadoPrestamoView.as_view(),
        name='listar_prestamos'
    ),

    ########### Prestamos/Devolución desde Inicio ###########
    path(
        route='crear_prestamo/',
        view=views.CrearPrestamoView.as_view(),
        name='crear_prestamo'
    ),
    path(
        route='devolucion/',
        view=views.DevolucionView.as_view(),
        name='devolucion'
    ),

    ########### Prestamos/Devolución desde Usuario ###########
    path(
        route='nuevo_prestamo/<int:pk>/<slug:slug>/',
        view=views.NuevoPrestamoView.as_view(),
        name='nuevo_prestamo'
    ),
    path(
        route='devolver_prestamo/<int:pk_ejemplar>/<int:pk_lector>/',
        view=views.DevolverPrestamoView.as_view(),
        name='devolver_prestamo'
    ),

    #################################################
    ########### MATERIAL NO BIBLIOGRAFICO ###########
    path(
        route='listar_prestamos_material/',
        view=views.ListadoPrestamoMaterialView.as_view(),
        name='listar_prestamos_material'
    ),

    ########### Prestamos/Devolución de Material ###########
    path(
        route='crear_prestamo_material/',
        view=views.CrearPrestamoMaterialView.as_view(),
        name='crear_prestamo_material'
    ),
    path(
        route='devolucion_material/',
        view=views.DevolucionMaterialView.as_view(),
        name='devolucion_material'
    ),

]