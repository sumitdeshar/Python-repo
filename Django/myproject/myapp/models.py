from django.db import models

# Create your models here.
class Features(models.Model):
    name= models.CharField(max_length= 100)
    details = models.CharField(max_length= 500)
    def __str__(self):
        return self.name
    
class AllowedIP(models.Model):
    ip_address = models.GenericIPAddressField(null=True)
    # def __str__(self):
    #     return self.ip
    
    