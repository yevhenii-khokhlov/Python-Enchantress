from datetime import datetime

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic import TemplateView

from apps.boards.models import Task


def home_page(request):
    return HttpResponse("<h1>Hello</h1>")


def simple_api(request):
    data = serializers.serialize('json', [request.user])
    return HttpResponse(data)


class HomePage(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['now'] = timezone.now()
        context['user'] = self.request.user
        context['user_json'] = serializers.serialize('json', [self.request.user])
        context['tasks'] = Task.objects.all().order_by('-id')
        return context
