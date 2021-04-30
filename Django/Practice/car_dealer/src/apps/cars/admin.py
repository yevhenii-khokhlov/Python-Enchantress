from django.contrib import admin

from .models import \
    (Car, Color, Brand, Model, Picture, Property, CarProperty)

admin.site.register(Car)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Picture)
admin.site.register(Property)
admin.site.register(CarProperty)
