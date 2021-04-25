import factory
from factory import fuzzy

from src.apps.dealers import models


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Country

    name = factory.Sequence(lambda n: 'Ukraine%s' % n)
    code = fuzzy.FuzzyText(prefix='+', chars='1234567890', length=4)


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.City

    name = fuzzy.FuzzyText(suffix='-city', length=15)


class DealerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Dealer

    title = factory.fuzzy.FuzzyText(length=50)
    city_id = factory.SubFactory(CityFactory)
    name = factory.fuzzy.FuzzyText(prefix="Dealer_", length=15)
