from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import View, CreateView, UpdateView, DeleteView, DetailView, ListView, FormView

from loan.forms import PrestamoForm, NuevoPrestamoForm, DevolucionForm
from loan.models import Prestamo
from catalog.models import EjemplarLibro
from account.models import Perfil


# class CrearPrestamoView(LoginRequiredMixin, FormView):

#     template_name = 'loan/crear_prestamo.html'
#     form_class = PrestamoForm
#     success_url = reverse_lazy('catalog:home')

#     def form_valid(self, form):
#         """Save form data."""
#         form.save()
#         return super().form_valid(form)


class CrearPrestamoView(View):

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
            fecha_prestamo = data['fecha_prestamo']
            fecha_devolucion = data['fecha_devolucion']

            print(data)

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


class ListadoPrestamoView(ListView):
    model = Prestamo
    template_name = 'loan/listar_prestamos.html'
    context_object_name = 'prestamos'


class NuevoPrestamoView(View):

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


class DevolverPrestamoView(View):

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


class DevolucionView(View):

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
            devolucion = Prestamo.objects.get(ejemplar=ejemplar)

            now = datetime.now()
            x = now.date()

            devolucion.fecha_devuelto = x
            devolucion.save()
            ejemplar.estado = 'disponible'
            ejemplar.save()

            print(data)
            print(devolucion.bibliotecario)
            print(devolucion.lector)
            print(devolucion.ejemplar)
            print(devolucion.tipo_prestamo)
            print(devolucion.fecha_prestamo)
            print(devolucion.fecha_devolucion)
            print(devolucion.fecha_devuelto)

            # prestamo = Prestamo(
            #         bibliotecario=bibliotecario,
            #         lector=lector,
            #         ejemplar=ejemplar,
            #         tipo_prestamo=tipo_prestamo,
            #         fecha_prestamo=fecha_prestamo,
            #         fecha_devolucion=fecha_devolucion,
            #     )
            # prestamo.save()

            # ejemplar.estado = 'prestado'
            # ejemplar.save()
        else:
            return render(request, 'loan/crear_prestamo.html', {
                'prestamo_form': prestamo_form,
            })

        return redirect('catalog:home')