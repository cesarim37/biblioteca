from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, UpdateView, DeleteView, DetailView, ListView

from loan.forms import PrestamoForm, NuevoPrestamoForm
from loan.models import Prestamo
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
        
        bibliotecario = self.request.user.perfil_usuario.bibliotecario_perfil
        lector = Perfil.objects.get(pk=pk)
        tipo = lector.tipo_usuario
        print(bibliotecario)
        print(lector)
        print(tipo)

        prestamo_form = NuevoPrestamoForm()

        return render(request, 'loan/nuevo_prestamo.html', {
            'prestamo_form': prestamo_form,
        })