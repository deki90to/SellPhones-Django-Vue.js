from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import base, reverse
# from django_resized import ResizedImageField
# Create your models here.

class Brand(models.Model):
    brand = models.CharField(max_length=100)

    def __str__(self):
        return(f'{self.brand}')

class Model(models.Model):
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    modelName = models.CharField(max_length=100)

    def __str__(self):
        return(f'{self.brand} {self.modelName}')

class Specs(models.Model):
    model = models.ForeignKey('Model', on_delete=models.CASCADE, null=True)
    dimensions = models.CharField(max_length=50)
    weight = models.CharField(max_length=10)
    screen = models.CharField(max_length=200)
    cpu = models.CharField(max_length=100)
    gpu = models.CharField(max_length=100)
    mainCam = models.CharField(max_length=50)
    selfieCam = models.CharField(max_length=50)
    video = models.CharField(max_length=100)
    battery = models.CharField(max_length=10)
    fastCharging = models.BooleanField()

    def __str__(self):
        return(f'{self.model}')