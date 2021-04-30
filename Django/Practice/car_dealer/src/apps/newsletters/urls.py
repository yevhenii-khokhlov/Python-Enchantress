from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from .views import NewsLetterView

app_name = 'newsletters'

urlpatterns = [
    path('new/', NewsLetterView.as_view(), name='newsletters')
]
