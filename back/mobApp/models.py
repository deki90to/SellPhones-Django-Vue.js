from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import base, reverse
# from django_resized import ResizedImageField
from django.utils import timezone
# Create your models here.


class Brand(models.Model):
    brandName = models.CharField(max_length=100)

    def __str__(self):
        return(f'{ self.brandName }')


class Model(models.Model):
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, null=True)
    modelName = models.CharField(max_length=100)
    createdOn = models.DateField(default=timezone.now)
    warranty = models.BooleanField()
    damaged = models.BooleanField()
    repaired = models.BooleanField()
    firstOwner = models.BooleanField()
    price = models.IntegerField()

    def __str__(self):
        return(f'{ self.brand } { self.modelName } / { self.price }e / Created: { self.createdOn } ')


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
        return(f'{ self.model }')