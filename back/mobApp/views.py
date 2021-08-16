from rest_framework import serializers
from . models import Specs, Models, Brands
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import ModelsSerializer, SpecsSerializer, BrandsSerializer, BrandModelsSerializer, ModelSpecsSerializer
# Create your views here.


@api_view(['GET'])
def BrandsView(request):
    brand = Brands.objects.all()
    serializer = BrandsSerializer(brand, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ModelsView(request, pk):
    model = Models.objects.get(pk=pk)
    serializer = ModelsSerializer(model, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def SpecsView(request, pk):
    specs = Specs.objects.get(pk=pk)
    serializer = SpecsSerializer(specs, many=False)
    return Response(serializer.data)





@api_view(['GET'])
def BrandModelsView(request, pk):
    brandModels = Brands.objects.get(pk=pk)
    serializer = BrandModelsSerializer(brandModels)
    return Response(serializer.data)


@api_view(['GET'])
def ModelSpecsView(request, pk):
    modelSpecs = Models.objects.get(pk=pk)
    serializer = ModelSpecsSerializer(modelSpecs)
    return Response(serializer.data)


