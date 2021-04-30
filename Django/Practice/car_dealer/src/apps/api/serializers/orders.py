from rest_framework import serializers
from django.apps import apps

Car = apps.get_model("cars", "Car")
Order = apps.get_model("orders", "Order")


class OrderAPISerializer(serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=50)
    phone = serializers.CharField(max_length=9)
    message = serializers.CharField(max_length=500)

    class Meta:
        model = Order
        fields = ['car', 'first_name', 'last_name', 'email', 'phone', 'message', ]

    def validate(self, attrs):
        car = attrs.get('car')
        email = attrs.get('email')
        order = Order.objects.filter(car=car, email=email)
        if order:
            raise serializers.ValidationError('order for you already exists')
        return attrs
