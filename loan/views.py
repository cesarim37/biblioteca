from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import View, CreateView, UpdateView, DeleteView, DetailView, ListView, FormView

from loan.forms import PrestamoForm, NuevoPrestamoForm, DevolucionForm, PrestamoMaterialForm, DevolucionMaterialForm
from loan.models import Prestamo, PrestamoMaterial
from catalog.models import EjemplarLibro
from account.models import Perfil


##############################################
########### MATERIAL BIBLIOGRAFICO ###########
##############################################

class ListadoPrestamoView(LoginRequiredMixin, ListView):
    model = Prestamo
    template_name = 'loan/listar_prestamos.html'
    context_object_name = 'prestamos'


########### Prestamos/Devolución desde Inicio ###########

class CrearPrestamoView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        prestamo_form = PrestamoForm()

        return render(request, 'loan/crear_prestamo.html', {
            'prestamo_form': prestamo_form,
        })

        
    def post(self, request, *args, **kwargs):

        prestamo_form = PrestamoForm(request.POST)
        
        if prestamo_form.is_valid():
            bibliotecario = self.request.user.perfil_usuario.bibliotecario_perfil
            
            data = prestamo_form.cleaned_data

            cota = data['ejemplar']
            ejemplar = EjemplarLibro.objects.get(cota=cota)

            cedula = data['lector']
            lector = Perfil.objects.get(cedula_identidad=cedula)

            tipo_prestamo = data['tipo_prestamo']
            fecha_devolucion = data['fecha_devolucion']

            now = datetime.now()
            x = now.date()
            fecha_prestamo = x

            prestamo = Prestamo(
                    bibliotecario=bibliotecario,
                    lector=lector,
                    ejemplar=ejemplar,
                    tipo_prestamo=tipo_prestamo,
                    fecha_prestamo=fecha_prestamo,
                    fecha_devolucion=fecha_devolucion,
                )
            prestamo.save()

            ejemplar.estado = 'prestado'
            ejemplar.save()
        else:
            return render(request, 'loan/crear_prestamo.html', {
                'prestamo_form': prestamo_form,
            })

        return redirect('catalog:home')


class DevolucionView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        devolucion_form = DevolucionForm()

        return render(request, 'loan/devolucion.html', {
            'devolucion_form': devolucion_form,
        })

        
    def post(self, request, *args, **kwargs):

        devolucion_form = DevolucionForm(request.POST)
        
        if devolucion_form.is_valid():
            
            bibliotecario = self.request.user.perfil_usuario.bibliotecario_perfil
            
            data = devolucion_form.cleaned_data

            cota = data['ejemplar']
            ejemplar = EjemplarLibro.objects.get(cota=cota)

            devolucion = Prestamo.objects.get(ejemplar=ejemplar, fecha_devuelto=None)

            now = datetime.now()
            x = now.date()

            devolucion.fecha_devuelto = x
            devolucion.save()
            ejemplar.estado = 'disponible'
            ejemplar.save()

        else:
            return render(request, 'loan/crear_prestamo.html', {
                'prestamo_form': prestamo_form,
            })

        return redirect('catalog:home')


########### Prestamos/Devolución desde Usuario ###########

class NuevoPrestamoView(LoginRequiredMixin, View):

    def get(self, request, pk, slug, *args, **kwargs):

        context= {}
        prestamo_form = NuevoPrestamoForm()
        lector = Perfil.objects.get(pk=pk)
        tipo_usuario = lector.tipo_usuario
        print('paso!')
        print(lector)
        print(tipo_usuario)

        if tipo_usuario == 'visitante':
            prestamo_form = NuevoPrestamoForm(initial={'tipo_prestamo': 'sala'})
            context['tipo_usuario']= 'visitante'
        else:
            context['tipo_usuario']= False

        return render(request, 'loan/nuevo_prestamo.html', {
            'prestamo_form': prestamo_form,
            'tipo_usuario': context['tipo_usuario'],
        })

        
    def post(self, request, pk, slug, *args, **kwargs):

        prestamo_form = NuevoPrestamoForm(request.POST)
        
        if prestamo_form.is_valid():
            bibliotecario = self.request.user.perfil_usuario.bibliotecario_perfil
            lector = Perfil.objects.get(pk=pk)
            
            data = prestamo_form.cleaned_data

            ejemplar = data['ejemplar']
            tipo_prestamo = data['tipo_prestamo']
            fecha_prestamo = data['fecha_prestamo']
            fecha_devolucion = data['fecha_devolucion']

            prestamo = Prestamo(
                    bibliotecario=bibliotecario,
                    lector=lector,
                    ejemplar=ejemplar,
                    tipo_prestamo=tipo_prestamo,
                    fecha_prestamo=fecha_prestamo,
                    fecha_devolucion=fecha_devolucion,
                )
            prestamo.save()

            e = EjemplarLibro.objects.get(pk=ejemplar.pk)
            e.estado = 'prestado'
            e.save()
        else:
            return render(request, 'loan/nuevo_prestamo.html', {
                'prestamo_form': prestamo_form,
            })

        return redirect('catalog:home')


class DevolverPrestamoView(LoginRequiredMixin, View):

    def get(self, request, pk_ejemplar, pk_lector, *args, **kwargs):

        lector = Perfil.objects.get(pk=pk_lector)
        ejemplar = EjemplarLibro.objects.get(pk=pk_ejemplar)
        pendiente = lector.prestamo_user.get(fecha_devuelto=None, ejemplar=ejemplar)
        
        now = datetime.now()
        x = now.date()

        devolucion = Prestamo.objects.get(pk=pendiente.pk)
        devolucion.fecha_devuelto = x
        devolucion.save()
        ejemplar.estado = 'disponible'
        ejemplar.save()

        return redirect(reverse_lazy('account:perfil_detail', kwargs={'slug': lector.slug, 'pk': lector.pk}))


#################################################
########### MATERIAL NO BIBLIOGRAFICO ###########
#################################################

class ListadoPrestamoMaterialView(LoginRequiredMixin, ListView):
    model = PrestamoMaterial
    template_name = 'loan/material/listar_prestamos_material.html'
    context_object_name = 'prestamos_material'


########### Prestamos/Devolución desde Material ###########

class CrearPrestamoMaterialView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        prestamo_form = PrestamoMaterialForm()

        return render(request, 'loan/material/crear_prestamo_material.html', {
            'prestamo_form': prestamo_form,
        })

        
    def post(self, request, *args, **kwargs):

        prestamo_form = PrestamoMaterialForm(request.POST)
        
        if prestamo_form.is_valid():
            bibliotecario = self.request.user.perfil_usuario.bibliotecario_perfil
            
            data = prestamo_form.cleaned_data

            ejemplar_material = data['ejemplar_material']

            cedula = data['lector']
            lector = Perfil.objects.get(cedula_identidad=cedula)

            tipo_prestamo = data['tipo_prestamo']
            fecha_devolucion = data['fecha_devolucion']

            now = datetime.now()
            x = now.date()
            fecha_prestamo = x

            prestamo = PrestamoMaterial(
                    bibliotecario=bibliotecario,
                    lector=lector,
                    ejemplar_material=ejemplar_material,
                    tipo_prestamo=tipo_prestamo,
                    fecha_prestamo=fecha_prestamo,
                    fecha_devolucion=fecha_devolucion,
                )
            prestamo.save()

            ejemplar_material.estado = 'prestado'
            ejemplar_material.save()
        else:
            return render(request, 'loan/material/crear_prestamo_material.html', {
                'prestamo_form': prestamo_form,
            })

        return redirect('catalog:home')


class DevolucionMaterialView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        devolucion_form = DevolucionMaterialForm()

        return render(request, 'loan/material/devolucion_material.html', {
            'devolucion_form': devolucion_form,
        })

        
    def post(self, request, *args, **kwargs):

        devolucion_form = DevolucionMaterialForm(request.POST)
        
        if devolucion_form.is_valid():
            
            bibliotecario = self.request.user.perfil_usuario.bibliotecario_perfil
            
            data = devolucion_form.cleaned_data

            ejemplar_material = data['ejemplar_material']

            devolucion = PrestamoMaterial.objects.get(ejemplar_material=ejemplar_material, fecha_devuelto=None)

            now = datetime.now()
            x = now.date()

            devolucion.fecha_devuelto = x
            devolucion.save()
            ejemplar_material.estado = 'disponible'
            ejemplar_material.save()

        else:
            return render(request, 'loan/material/crear_prestamo_material.html', {
                'prestamo_form': prestamo_form,
            })

        return redirect('catalog:home')