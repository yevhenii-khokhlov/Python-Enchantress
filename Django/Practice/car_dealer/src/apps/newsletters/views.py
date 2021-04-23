from django.shortcuts import render
from django.views.generic import FormView

from .forms import NewsLetterModelForm


class NewsLetterView(FormView):
    template_name = "newsletter.html"
    form_class = NewsLetterModelForm
    success_url = '/'
