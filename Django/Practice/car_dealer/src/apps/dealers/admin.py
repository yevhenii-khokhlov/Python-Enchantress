from django.contrib import admin

from .models import Dealer, Country, City

admin.site.register(City)
admin.site.register(Country)
admin.site.register(Dealer)
