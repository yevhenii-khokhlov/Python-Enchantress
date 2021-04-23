from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Car


class CarDetailView(TemplateView):
    template_name = "car_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car"] = Car.objects.prefetch_related("photos")

        return context
