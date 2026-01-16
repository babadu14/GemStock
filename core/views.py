from django.shortcuts import render
from rest_framework import mixins, viewsets
from core.models import Stock
from core.serializers import StockSerializer
from core.services import fetch_latest_prices

# Create your views here.
class StockListViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = "ticker"