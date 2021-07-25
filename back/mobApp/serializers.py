from django.db import models
from django.db.models import fields
from . models import Specs, Brand, Model
from rest_framework import serializers

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

        
class ModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'


class SpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specs
        fields = '__all__'