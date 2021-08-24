from rest_framework import serializers
from . models import Specs, Models, Brands
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import ModelsSerializer, SpecsSerializer, BrandsSerializer, BrandModelsSerializer, ModelSpecsSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def BrandsView(request):
    if request.method == 'GET':
        brand = Brands.objects.all()
        serializer = BrandsSerializer(brand, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BrandsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def BrandModelsView(request, pk):
    if request.method == 'GET':
        brandModels = Brands.objects.get(pk=pk)
        serializer = BrandModelsSerializer(brandModels)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BrandModelsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def ModelSpecsView(request, pk):
    modelSpecs = Models.objects.get(pk=pk)
    serializer = ModelSpecsSerializer(modelSpecs)
    return Response(serializer.data)
