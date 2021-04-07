from django.contrib.auth.models import AbstractUser
from django.db import models

from src.common.models import MyBaseModel
from .choices import \
    FUEL_CHOICES, \
    ENGINE_CHOICES, \
    POSITION_CHOICES, \
    POPULATION_CHOICES, \
    GEAR_CASE_CHOICES, GEAR_CASE_MECHANICAL, \
    ORDER_STATUS_CHOICES, ORDER_STATUS_OPEN, \
    CAR_STATUS_CHOICES, CAR_STATUS_AVAILABLE


class Color(MyBaseModel):
    pass


class Brand(MyBaseModel):
    pass


class Model(MyBaseModel):
    brand_id = models.ForeignKey(
        to=Brand,
        on_delete=models.CASCADE
    )


class Car(models.Model):
    color_id = models.ForeignKey(
        to=Color,
        on_delete=models.SET_NULL,
        null=True
    )
    dealer_id = models.ForeignKey(
        to='dealers.Dealer',
        on_delete=models.CASCADE
    )
    model_id = models.ForeignKey(
        to=Model,
        on_delete=models.CASCADE
    )


class Property(MyBaseModel):
    category = models.CharField(max_length=30)


class CarProperty(models.Model):
    property_id = models.ForeignKey(
        to=Property,
        on_delete=models.CASCADE
    )
    car_id = models.ForeignKey(
        to=Car,
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        null=True
    )
    number = models.SmallIntegerField()
    sitting_place = models.IntegerField(null=True)
    engine_power = models.IntegerField(null=True)
    first_registration_date = models.DateField(null=True)
    doors = models.SmallIntegerField(default=4, null=True)
    fuel_type = models.CharField(
        max_length=1,
        choices=FUEL_CHOICES,
        default=None
    )
    engine_type = models.CharField(
        max_length=1,
        choices=ENGINE_CHOICES,
        default=None
    )
    capacity = models.DecimalField(
        max_digits=3, decimal_places=1,
        null=True,
        default=None
    )
    gear_case = models.CharField(
        max_length=1,
        choices=GEAR_CASE_CHOICES,
        default=GEAR_CASE_MECHANICAL
    )
    status = models.CharField(
        max_length=1,
        choices=CAR_STATUS_CHOICES,
        default=CAR_STATUS_AVAILABLE
    )
    slug = models.CharField(max_length=100, null=True)
    population_type = models.CharField(
        max_length=1,
        choices=POPULATION_CHOICES,
        null=True
    )
    other = models.TextField(max_length=500, null=True)


class Picture(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    url = models.CharField(max_length=80)
    metadata = models.TextField(null=True)
    position = models.CharField(
        max_length=1,
        choices=POSITION_CHOICES,
        null=True
    )


class Order(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=9)
    message = models.TextField(null=True)
    status = models.CharField(
        max_length=1,
        choices=ORDER_STATUS_CHOICES,
        default=ORDER_STATUS_OPEN
    )
