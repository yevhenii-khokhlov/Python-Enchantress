from django.shortcuts import render
from django.views.generic import FormView

from .forms import NewsLetterModelForm


class NewsLetterView(FormView):
    template_name = "newsletter.html"
    form_class = NewsLetterModelForm
    success_url = '/'

    def form_valid(self, form):
        form.save_email()
        return super().form_valid(form=form)
