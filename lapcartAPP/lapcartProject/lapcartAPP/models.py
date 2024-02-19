
from django.db import models


class Laptop(models.Model):
    company = models.CharField(max_length=30)
    model = models.CharField(max_length=20)
    processor = models.CharField(max_length=20)
    rom = models.IntegerField()
    ram = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)
