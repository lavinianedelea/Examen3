from django.db import models

# Create your models here.
class buyerdata(models.Model):
    first_name = models.CharField(max_length=300, unique=False)
    last_name = models.CharField(max_length=300, unique=False)
    address = models.CharField(max_length=300, unique=False)
