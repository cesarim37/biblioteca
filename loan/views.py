from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, UpdateView, DeleteView, DetailView, ListView

from loan.forms import PrestamoForm


class CrearPrestamoView(LoginRequiredMixin, CreateView):

    template_name = 'loan/crear_prestamo.html'
    form_class = PrestamoForm
    success_url = reverse_lazy('catalog:home')