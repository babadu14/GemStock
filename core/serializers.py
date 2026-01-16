from rest_framework import serializers
from core.models import Stock, GemStock, PriceData

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['ticker', 'name', 
                  'sector', 'market_cap']