from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, UpdateView, DeleteView, DetailView, ListView

from loan.forms import PrestamoForm, NuevoPrestamoForm
from loan.models import Prestamo
from catalog.models import EjemplarLibro
from account.models import Perfil


class CrearPrestamoView(LoginRequiredMixin, CreateView):

    template_name = 'loan/crear_prestamo.html'
    form_class = PrestamoForm
    success_url = reverse_lazy('catalog:home')


class ListadoPrestamoView(ListView):
    model = Prestamo
    template_name = 'loan/listar_prestamos.html'
    context_object_name = 'prestamos'


class NuevoPrestamoView(View):

    def get(self, request, pk, slug, *args, **kwargs):

        prestamo_form = NuevoPrestamoForm()
        lector = Perfil.objects.get(pk=pk)
        tipo_usuario = lector.tipo_usuario

        if tipo_usuario == 'visitante':
            prestamo_form = NuevoPrestamoForm(initial={'tipo_prestamo': 'sala'})

        return render(request, 'loan/nuevo_prestamo.html', {
            'prestamo_form': prestamo_form,
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

        return render(request, 'loan/nuevo_prestamo.html', {
            'prestamo_form': prestamo_form,
        })
