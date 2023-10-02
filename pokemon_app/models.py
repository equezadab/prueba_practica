from django.db import models

# Create your models here.


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(null=True, blank=True, upload_to="img/")

    def __str__(self):
        return self.nombre


class Region(models.Model):
    idReg = models.IntegerField(primary_key=True)
    nombre_region = models.CharField(max_length=50)


class Tipo(models.Model):
    idTip = models.IntegerField(primary_key=True)
    nombre_tipo = models.CharField(max_length=50)


class RegionPokemon(models.Model):
    idRegTipo = models.IntegerField(primary_key=True)
    nombre_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    nombre = models.ForeignKey(Pokemon, on_delete=models.CASCADE)


class TipoPokemon(models.Model):
    idTipPokemon = models.IntegerField(primary_key=True)
    nombre_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    nombre = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
