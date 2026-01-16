from django.db import models

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(unique=True)
    name = models.CharField(max_length=255)
    sector = models.TextField(max_length=255)
    market_cap = models.PositiveIntegerField(null=True)
    pe_ratio = models.FloatField(null=True)
    dividend_yield = models.FloatField(null=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class PriceData(models.Model):
    stock = models.ForeignKey("core.Stock", related_name='prices', on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.BigIntegerField()
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.stock}"

class GemStock(models.Model):
    stock = models.ForeignKey("core.Stock", on_delete=models.CASCADE, related_name='Gems')
    score = models.FloatField(null=True)
    reason = models.TextField(null=True)