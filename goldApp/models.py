from django.db import models

# Create your models here.
from django.db import models

class StockData(models.Model):
    Open = models.FloatField()
    High = models.FloatField()
    Low = models.FloatField()
    Volume = models.FloatField()

    def __str__(self):
        return f"StockData - {self.Open}, {self.High}, {self.Low}, {self.Volume}"
