from django.core.management.base import BaseCommand
from core.services import fetch_latest_prices
from core.models import Stock, PriceData
from datetime import datetime, timezone
from django.conf import settings
from django.utils.dateparse import parse_datetime


class Command(BaseCommand):
    help = 'fetches stock prices via ticker'
    
    def handle(self, *args, **options):
        stocks = Stock.objects.all()
        for stock in stocks:
            data = fetch_latest_prices(stock.ticker)

            if not data:
                continue
                        
            timestamp = parse_datetime(data["timestamp"])

            if PriceData.objects.filter(stock=stock, timestamp=timestamp).exists():
                continue            

            PriceData.objects.create(
                stock=stock,
                timestamp=timestamp,
                open=data["open"],
                high=data["high"],
                low=data["low"],
                close=data["close"],
                volume=data["volume"],
            )
        print("data fetched successfully")