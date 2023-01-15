from django.db import models

# Create your models here.
class Features(models.Model):
    name= models.CharField(max_length= 100)
    details = models.CharField(max_length= 500)