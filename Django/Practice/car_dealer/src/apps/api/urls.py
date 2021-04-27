from django.urls import path

from .views import (
    LoginAPIView,
    LogoutAPIView,
    CarsAPIView,
    CarAPIView,
    DealerCarsAPIView,
    OrderAPIView,
    CarCreateAPIView,
    CarUpdateAPIView,
    CarDeleteAPIView,
    CarPublishAPIView,
    CarStatisticsAPIView,
)

app_name = 'api'

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login-api'),
    path('logout/', LogoutAPIView.as_view(), name='logout-api'),
    path('cars/', CarsAPIView.as_view(), name='cars-api'),
    path('cars/<int:pk>/', CarAPIView.as_view(), name='car-api'),
    path('mycars/', DealerCarsAPIView.as_view(), name='my-cars-api'),
    path('mycars/create/', CarCreateAPIView.as_view(), name='new-car-api'),
    path('mycars/<int:pk>/update/', CarUpdateAPIView.as_view(), name='car-update-api'),
    path('mycars/<int:pk>/delete/', CarDeleteAPIView.as_view(), name='car-delete-api'),
    path('mycars/<int:pk>/publish/', CarPublishAPIView.as_view({'post': 'publish'}), name='car-publish-api'),
    path('mycars/<int:pk>/unpublish/', CarPublishAPIView.as_view({'post': 'unpublish'}), name='car-unpublish-api'),
    path('mycars/statistics/', CarStatisticsAPIView.as_view(), name='cars-statistics-api'),
    path('order/', OrderAPIView.as_view(), name='order-api'),
]
