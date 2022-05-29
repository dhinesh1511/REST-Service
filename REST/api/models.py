from django.db import models

# Create your models here.
class branches(models.Model):
    ifsc = models.CharField(max_length=11)
    bank_id = models.CharField(max_length=6)
    branch = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=75)