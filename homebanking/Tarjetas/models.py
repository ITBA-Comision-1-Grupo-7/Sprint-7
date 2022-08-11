from django.db import models

# Create your models here.

class Tarjetas(models.Model):
  name= models.CharField(max_length=100)
  email= models.EmailField()
  tarjeta = models.CharField(max_length=100)
  def __str__(self): 
    return self.name