from django.contrib.auth import authenticate, views as auth_views,\
    login as auth_login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, DetailView, ListView, FormView, DeleteView

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied

from account.forms import EstudianteForm, PersonalForm, VisitanteForm,\
    BibliotecarioForm, LoginForm
from account.models import Perfil, Estudiante, Personal, Visitante


class ListadoPerfilView(PermissionRequiredMixin, ListView):
    permission_required = ['account.view_perfil']
    
    model = Perfil
    template_name = 'account/listar_perfil.html'
    context_object_name = 'perfiles'
    queryset = Perfil.objects.filter(status=True).exclude(tipo_usuario='bibliotecario')


class CrearEstudianteView(PermissionRequiredMixin, FormView):
    permission_required = ['account.view_estudiante', 'account.add_estudiante']

    template_name = 'account/crear_estudiante.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('account:listar_perfil')
    extra_context = {'title': 'Registro'}

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class ActualizarEstudianteView(PermissionRequiredMixin, FormView):
    permission_required = ['account.view_estudiante', 'account.change_estudiante']

    template_name = 'account/crear_estudiante.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('account:listar_perfil')
    extra_context = {'title': 'Actualización'}

    def get_initial(self):
        
        initial = super(ActualizarEstudianteView, self).get_initial()
        print(self.kwargs)
        initial.update({'estudiante': get_object_or_404(Estudiante, pk=self.kwargs['pk'])})
        return initial

    def form_valid(self, form):

        form.save()
        return super().form_valid(form)


# class ActualizarEstudianteView(PermissionRequiredMixin, View):
#     permission_required = ['account.view_estudiante']

#     def get(self, request, pk, *args, **kwargs):
#         estudiante_form = EstudianteForm(initial={
#             'estudiante': get_object_or_404(Estudiante, pk=pk),
#             'update': False
#         })

#         return render(request, 'account/crear_estudiante.html', {
#             'form': estudiante_form,
#         })

#     def post(self, request, pk, *args, **kwargs):
#         permission_required = ['account.add_estudiante', 'account.change_estudiante']

#         estudiante_form = EstudianteForm(request.POST, initial={
#             'estudiante': get_object_or_404(Estudiante, pk=pk),
#             'update': True
#         })

#         if estudiante_form.is_valid():
#             estudiante_form.save()
#         else:
#             return render(request, 'account/crear_estudiante.html', {
#                 'form': estudiante_form,
#             })

#         return redirect('catalog:home')


class CrearPersonalView(PermissionRequiredMixin, FormView):
    permission_required = ['account.view_personal', 'account.add_personal']

    template_name = 'account/crear_personal.html'
    form_class = PersonalForm
    success_url = reverse_lazy('account:listar_perfil')
    extra_context = {'title': 'Registro'}

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class ActualizarPersonalView(PermissionRequiredMixin, FormView):

    template_name = 'account/crear_personal.html'
    form_class = PersonalForm
    success_url = reverse_lazy('account:listar_perfil')
    extra_context = {'title': 'Actualización'}

    def get_initial(self):
        
        initial = super(ActualizarPersonalView, self).get_initial()
        print(self.kwargs)
        initial.update({'personal': get_object_or_404(Personal, pk=self.kwargs['pk'])})
        return initial

    def form_valid(self, form):

        form.save()
        return super().form_valid(form)


class CrearVisitanteView(PermissionRequiredMixin, FormView):
    permission_required = ['account.view_visitante', 'account.add_visitante']

    template_name = 'account/crear_visitante.html'
    form_class = VisitanteForm
    success_url = reverse_lazy('account:listar_perfil')
    extra_context = {'title': 'Registro'}

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class ActualizarVisitanteView(PermissionRequiredMixin, FormView):

    template_name = 'account/crear_visitante.html'
    form_class = VisitanteForm
    success_url = reverse_lazy('account:listar_perfil')
    extra_context = {'title': 'Actualización'}

    def get_initial(self):
        
        initial = super(ActualizarVisitanteView, self).get_initial()
        print(self.kwargs)
        initial.update({'visitante': get_object_or_404(Visitante, pk=self.kwargs['pk'])})
        return initial

    def form_valid(self, form):

        form.save()
        return super().form_valid(form)


class ListadoBibliotecarioView(PermissionRequiredMixin, ListView):
    permission_required = ['account.view_bibliotecario']
    
    model = Perfil
    template_name = 'account/listar_bibliotecario.html'
    context_object_name = 'perfiles'
    queryset = Perfil.objects.filter(status=True,tipo_usuario='bibliotecario')


class CrearBibliotecarioView(PermissionRequiredMixin, FormView):
    permission_required = ['account.view_bibliotecario', 'account.add_bibliotecario']

    template_name = 'account/crear_bibliotecario.html'
    form_class = BibliotecarioForm
    success_url = reverse_lazy('account:listar_perfil')
    extra_context = {'title': 'Registro'}

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class EliminarPerfilView(PermissionRequiredMixin, DeleteView):
    permission_required = ['account.view_perfil', 'account.delete_perfil']

    model = Perfil
    template_name = 'account/perfil_confirm_delete.html'

    def post(self,request,pk,*args,**kwargs):
        object = Perfil.objects.get(id=pk)
        object.status = False
        object.save()
        return redirect('account:listar_perfil')


class PerfilDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ['account.view_perfil']

    model = Perfil


class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'registration/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        # Security check complete. Log the user in.

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
                pass
                # error_messages.append('usuario no activo')
        else:
            pass
            # ValidationError(_('Invalid value'), code='invalid')

        return HttpResponseRedirect(self.get_success_url())


class LogoutView(auth_views.LogoutView):
    """Logout view."""

    template_name = 'registration/logout.html'
