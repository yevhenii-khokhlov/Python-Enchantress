from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from src.apps.home.views import HomePage

app_name = 'home'

urlpatterns = [
    path('', HomePage.as_view(), name='home-page')
]
