from django.db import models

# Create your models here.

class Business(models.Model):
    BusinessId = models.AutoField(primary_key=True)
    BusinessName = models.CharField(max_length=500)
    BusinessAddress = models.CharField(max_length=500)
    BusinessNIT = models.CharField(max_length=500)
    BusinessPhone = models.CharField(max_length=50)
