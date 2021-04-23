from django.contrib.auth.models import AbstractUser
from django.db import models

from src.common.models import MyBaseModel


class Country(MyBaseModel):
    code = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.name}'


class City(MyBaseModel):
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.country_id}'


class Dealer(AbstractUser):
    title = models.CharField(max_length=50)
    city_id = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=25, default='car dealer')

    def __str__(self):
        return f'{self.name} on {self.city_id}'
