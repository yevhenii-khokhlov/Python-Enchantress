import factory
from factory import fuzzy

from src.apps.orders import models, choices
from .cars_factory import CarFactory


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Order

    car_id = factory.SubFactory(CarFactory)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.fuzzy.FuzzyText(length=25, suffix="@.fake.com")
    phone = factory.fuzzy.FuzzyText(length=9, chars="1234567890", prefix='+')
    message = factory.fuzzy.FuzzyText(length=90)
    status = factory.fuzzy.FuzzyChoice(choices=choices.ORDER_STATUS_CHOICES)
