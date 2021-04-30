import factory.fuzzy

from src.apps.cars import models, choices
from .dealers_factory import DealerFactory


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Color

    name = factory.Faker("color")


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Brand

    name = factory.fuzzy.FuzzyText(prefix="Brand_", length=12)


class ModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Model

    name = factory.fuzzy.FuzzyText(prefix="model_", length=15)
    brand_id = factory.SubFactory(BrandFactory)


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Car

    color_id = factory.SubFactory(ColorFactory)
    dealer_id = factory.SubFactory(DealerFactory)
    model_id = factory.SubFactory(ModelFactory)


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Property

    name = factory.fuzzy.FuzzyText(length=10)


class CarPropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.CarProperty

    property_id = factory.SubFactory(PropertyFactory)
    car_id = factory.SubFactory(CarFactory)
    price = factory.fuzzy.FuzzyDecimal(0.0, 100000.0)
    number = factory.fuzzy.FuzzyInteger(1, 9)
    sitting_place = factory.fuzzy.FuzzyInteger()
    engine_power = factory.fuzzy.FuzzyInteger(60, 500)
    first_registration_date = factory.fuzzy.FuzzyDate()
    doors = factory.fuzzy.FuzzyInteger(2, 5)
    fuel_type = factory.fuzzy.FuzzyChoice(choices=choices.FUEL_CHOICES)
    engine_type = factory.fuzzy.FuzzyChoice(choices=choices.ENGINE_CHOICES)
    capacity = factory.fuzzy.FuzzyDecimal(50.0, 100.0)
    gear_case = factory.fuzzy.FuzzyChoice(hoices=choices.GEAR_CASE_CHOICES)
    status = factory.fuzzy.FuzzyChoice(hoices=choices.CAR_STATUS_CHOICES)
    slug = factory.fuzzy.FuzzyText(length=100)
    population_type = factory.fuzzy.FuzzyChoice(choices=choices.POPULATION_CHOICES)
    other = factory.fuzzy.FuzzyText(length=500)


class PictureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Picture

    car_id = factory.SubFactory(CarFactory)
    picture = factory.fuzzy.FuzzyText(prefix="src/media/car_", length=50)
    metadata = factory.fuzzy.FuzzyText(length=100)
    position = factory.fuzzy.FuzzyChoice(choices=choices.POSITION_CHOICES)
