from django.contrib.auth.models import AbstractUser
from django.db import models

from src.common.models import MyBaseModel


class Country(MyBaseModel):
    code = models.CharField(max_length=6)


class City(MyBaseModel):
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)


class Dealer(AbstractUser):
    title = models.CharField(max_length=50)
    city_id = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
