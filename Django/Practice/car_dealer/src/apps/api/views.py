from django.apps import apps
from rest_framework import viewsets
from rest_framework import generics

from django.contrib.auth import login, logout
from django.db.models import F

from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView

from src.apps.api.serializers.cars import CarAPISerializer
from src.apps.api.serializers.auth import AuthAPISerializer
from src.apps.api.serializers.orders import OrderAPISerializer
from src.apps.api.serializers.dealers_car import \
    (DealersCarAPISerializer, CarPublishSerializer, CarStatisticsSerializer)

Car = apps.get_model("cars", "Car")
Order = apps.get_model("orders", "Order")


class LoginAPIView(APIView):
    def post(self, request):
        serializer = AuthAPISerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request=request, user=user)
        token, created = Token.objects.get_or_create(user=user)
        content = {
            'token': token.key,
        }
        return Response(content)

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            token = Token.objects.get(user=user)
            return Response({'token': token.key})
        return Response({'message': 'set username and password'})


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.is_authenticated:
            token = Token.objects.filter(user=request.user).delete()
            logout(request)
            return Response({'message': 'you are logged out'})
        return Response({'message': 'you are not logged in'})


class OrderAPIView(CreateAPIView):
    serializer_class = OrderAPISerializer
    queryset = Order.objects.all()


class CarsAPIView(ListAPIView):
    serializer_class = CarAPISerializer
    queryset = Car.objects.filter(publish=True)
    filter_backends = [SearchFilter]
    search_fields = ['brand__title', 'model__name']


class CarAPIView(ListAPIView):
    serializer_class = CarAPISerializer
    filter_backends = [SearchFilter]

    def get_queryset(self):
        car_id = self.kwargs['pk']
        Car.objects.filter(id=car_id).update(views=F('views') + 1)
        return Car.objects.filter(id=car_id, publish=True)


class DealerCarsAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DealersCarAPISerializer

    def get_queryset(self):
        dealer_id = self.request.user.id
        queryset = Car.objects.prefetch_related('photos')\
            .filter(dealer_id=dealer_id)
        return queryset


class CarCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DealersCarAPISerializer
    queryset = Car.objects.all()


class CarUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DealersCarAPISerializer

    def get_queryset(self):
        car_id = self.kwargs['pk']
        return Car.objects.filter(id=car_id, dealer=self.request.user)


class CarDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DealersCarAPISerializer

    def get_queryset(self):
        car_id = self.kwargs['pk']
        return Car.objects.filter(id=car_id, dealer=self.request.user)


class CarPublishAPIView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        car_id = self.kwargs['pk']
        return Car.objects.filter(id=car_id, dealer=self.request.user)

    @action(methods=['post'], detail=True)
    def publish(self, request, *args, **kwargs):
        serializer = CarPublishSerializer
        car_id = self.kwargs['pk']
        Car.objects.filter(id=car_id).update(publish=True)
        return Response({'message': f'car with id={car_id} published'})

    @action(methods=['post'], detail=True)
    def unpublish(self, request, *args, **kwargs):
        serializer = CarPublishSerializer
        car_id = self.kwargs['pk']
        Car.objects.filter(id=car_id).update(publish=False)
        return Response({'message': f'car with id={car_id} unpublished'})


class CarStatisticsAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CarStatisticsSerializer

    def get_queryset(self):
        user = self.request.user
        return Car.objects.filter(dealer=user).all()
