from django.db import models
from datetime import datetime

# Create your models here.
#Room database
class Room(models.Model):
    name = models.CharField(max_length= 1000, default='test')
    
#to store all the messages
class Message(models.Model):
    value = models.CharField(max_length=100000)
    date = models.DateTimeField(default = datetime.now, blank= True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)