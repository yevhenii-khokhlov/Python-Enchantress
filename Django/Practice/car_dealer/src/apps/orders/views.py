from django.shortcuts import render

from django.views.generic import FormView
from .forms import OrderModelForm


class OrderView(FormView):
    template_name = "pages/order.html"
    form_class = OrderModelForm
