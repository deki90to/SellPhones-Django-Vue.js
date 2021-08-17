from django.db import models
from django.db.models import fields
from . models import Specs, Models, Brands
from rest_framework import serializers


class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = '__all__'
        
class ModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Models
        fields = '__all__'

class SpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specs
        fields = '__all__'



class BrandModelsSerializer(serializers.ModelSerializer):
    models = ModelsSerializer(source="models_set", many=True)
    class Meta:
        model = Brands
        fields = ['models']

class ModelSpecsSerializer(serializers.ModelSerializer):
    specs = SpecsSerializer(source="specs_set", many=True)
    class Meta:
        model = Models
        fields = ['specs']
