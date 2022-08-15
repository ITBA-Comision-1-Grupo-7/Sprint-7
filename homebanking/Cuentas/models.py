from django.db import models

class Cliente(models.Model):
    apellido:models.CharField(max_length=30)
    nombre:models.CharField(max_length=30)
    balance:models.CharField
    tipoCuenta:models.CharField(max_length=10)
    idCuenta:models.CharField
    dni:models.CharField
    nombreCompleto:models.CharField(max_length=64)
    tarjeta:models.CharField(max_length=16)
    tarjetaUlt:models.CharField(max_length=4)