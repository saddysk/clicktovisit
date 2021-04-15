from django.db import models

# Create your models here.
class contactform(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.CharField(max_length=200)