from django import forms

from .models import NewsLetter


class NewsLetterModelForm(forms.ModelForm):

    class Meta:
        model = NewsLetter
        fields = ['email']

    # def save(self, commit=True):
    #     self.save()
