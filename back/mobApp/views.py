from rest_framework import serializers
from . models import Specs, Models, Brands
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import ModelsSerializer, SpecsSerializer, BrandsSerializer, BrandModelsSerializer, ModelSpecsSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
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
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def BrandModelsView(request, pk):
    brandModels = Brands.objects.get(pk=pk)
    serializer = BrandModelsSerializer(brandModels)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def ModelSpecsView(request, pk):
    modelSpecs = Models.objects.get(pk=pk)
    serializer = ModelSpecsSerializer(modelSpecs)
    return Response(serializer.data)
