# Models to get model from DB
from .models import Lunch, Orders

# Import generic views from django
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Messages and redirect page's
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Import's to set form_class in views
from .forms import CreateMenuForm, UpdateMenuForm, DeleteMenuForm, OrderMenuForm

from datetime import datetime, date

from django.contrib.auth.decorators import login_required


class ListLunch(SuccessMessageMixin, ListView):

    model = Lunch

    def get_queryset(self):
        queryset = super(ListLunch, self).get_queryset()
        fecha = date.today()
        if self.request.GET.get("add_time"):
            fecha_str = self.request.GET.get("add_time")
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        return queryset.filter(add_time=fecha, is_active=True)


class DetailLunch(DetailView):
    model = Lunch


class CreateLunch(SuccessMessageMixin, CreateView):
    model = Lunch
    form_class = CreateMenuForm
    success_message = "Almuerzo Creado Correctamente !"

    # Redirect to Homepage
    def get_success_url(self):
        return reverse("list")


class UpdateLunch(SuccessMessageMixin, UpdateView):
    model = Lunch
    form_class = UpdateMenuForm
    success_message = "Almuerzo Actualizado Correctamente !"

    # Redirect to Homepage
    def get_success_url(self):
        return reverse("list")


class DeleteLunch(SuccessMessageMixin, DeleteView):
    model = Lunch
    form_class = DeleteMenuForm

    # Redirect to Homepage and send message
    def get_success_url(self):
        success_message = "Almuerzo Eliminado Correctamente !"
        messages.success(self.request, (success_message))
        return reverse("list")


class OrderLunch(SuccessMessageMixin, CreateView):
    model = Orders
    form_class = OrderMenuForm
    success_message = "Almuerzo Solicitado Correctamente !"

    # Get user data
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    # Redirect to Homepage
    def get_success_url(self):
        return reverse("list")


class MyOrdersLunch(ListView):
    model = Orders
    context_object_name = "orders_list"

    def get_queryset(self):
        queryset = super(MyOrdersLunch, self).get_queryset()
        user_id = self.request.GET.get("user_id")
        return queryset.filter(user=user_id)
