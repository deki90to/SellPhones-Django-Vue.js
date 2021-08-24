from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import base, reverse
# from django_resized import ResizedImageField
from django.utils import timezone
# Create your models here.

class Brands(models.Model):
    brand = models.CharField(max_length=20)

    def __str__(self):
        return(f'{ self.brand }')

class Models(models.Model):
    brand = models.ForeignKey('Brands', on_delete=models.CASCADE, null=True)
    model = models.CharField(max_length=100, blank=True)
    createdOn = models.DateField(default=timezone.now, blank=True)
    warranty = models.BooleanField(blank=True)
    damaged = models.BooleanField(blank=True)
    repaired = models.BooleanField(blank=True)
    firstOwner = models.BooleanField(blank=True)
    price = models.IntegerField(blank=True)

    def __str__(self):
        return(f'{ self.brand } - { self.model } / { self.price }e / Created: { self.createdOn }')


class Specs(models.Model):
    model = models.ForeignKey('Models', on_delete=models.CASCADE, null=True)
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