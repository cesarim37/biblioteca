from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, UpdateView, DeleteView, DetailView, ListView, FormView

from account.forms import EstudianteForm, PersonalForm, VisitanteForm, BibliotecarioForm
from account.models import Perfil

class CrearEstudianteView(FormView):
    """Users sign up view."""

    template_name = 'account/crear_estudiante.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class CrearPersonalView(FormView):
    """Users sign up view."""

    template_name = 'account/crear_personal.html'
    form_class = PersonalForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class CrearVisitanteView(FormView):
    """Users sign up view."""

    template_name = 'account/crear_visitante.html'
    form_class = VisitanteForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class CrearBibliotecarioView(FormView):
    """Users sign up view."""

    template_name = 'account/crear_bibliotecario.html'
    form_class = BibliotecarioForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class ListadoPerfilView(ListView):
    model = Perfil
    template_name = 'account/listar_perfil.html'
    context_object_name = 'perfiles'
    queryset = Perfil.objects.filter(status=True)