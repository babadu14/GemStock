from django.contrib import admin

# Register your models here.
from .models import PriceData, GemStock, Stock

admin.site.register(PriceData)
admin.site.register(GemStock)
admin.site.register(Stock)