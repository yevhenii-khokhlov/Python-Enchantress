import factory
from factory import fuzzy

from src.apps.newsletters import models


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.NewsLetter

    email = factory.fuzzy.FuzzyText(length=25, suffix="@fake.com.ua")
