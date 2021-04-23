from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.apps import apps

Car = apps.get_model("cars", "Car")


class HomePage(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.prefetch_related("photos").all()

        return context
