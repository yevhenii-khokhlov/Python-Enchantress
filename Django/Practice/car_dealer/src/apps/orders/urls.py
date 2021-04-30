from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from .views import OrderView

app_name = 'orders'

urlpatterns = [
    path('new/', OrderView.as_view(), name='new-order')
]
