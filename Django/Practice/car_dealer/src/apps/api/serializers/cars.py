from rest_framework import serializers
from django.apps import apps

Car = apps.get_model("cars", "Car")


class CarAPISerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='model.brand.name')
    model = serializers.CharField(source='model.name')
    color = serializers.CharField(source='color.name')
    dealer = serializers.CharField(source='dealer.title')

    class Meta:
        model = Car
        exclude = ['publish', 'views']
