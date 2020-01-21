from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, views as auth_views, login as auth_login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, UpdateView, DeleteView, DetailView, ListView, FormView

from account.forms import EstudianteForm, PersonalForm, VisitanteForm, BibliotecarioForm, LoginForm
from account.models import Perfil, Estudiante


class CrearEstudianteView(FormView):
    """Users sign up view."""

    template_name = 'account/crear_estudiante.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class ActualizarEstudianteView(UpdateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'account/crear_estudiante.html'
    success_url = reverse_lazy('account:listar_perfil')


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


class PerfilDetailView(DetailView):
    model = Perfil


class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'registration/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        """Security check complete. Log the user in."""

        cedula = form.cleaned_data.get('cedula')
        password = form.cleaned_data.get('password')

        try:
            username = User.objects.get(username=cedula).username
        except User.DoesNotExist:
            username = None
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(self.request, user)
            else:
                error_messages.append('usuario no activo')
        else:
            ValidationError(_('Invalid value'), code='invalid')

        return HttpResponseRedirect(self.get_success_url())


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""

    template_name = 'registration/logout.html'