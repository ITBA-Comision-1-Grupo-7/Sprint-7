from django.db import models

class Cliente(models.Model):
    apellido:models.CharField(max_length=30)
    nombre:models.CharField(max_length=30)
    balance:models.FloatField
    tipoCuenta:models.CharField(max_length=10)
    idCuenta:models.IntegerField
    dni:models.IntegerField