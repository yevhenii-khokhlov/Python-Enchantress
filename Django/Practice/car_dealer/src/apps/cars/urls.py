from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from .views import CarDetailView

app_name = 'cars'

urlpatterns = [
    path('car/<int:pk>/detail/', CarDetailView.as_view(template_name="car_detail.html"), name='car-detail')
]
