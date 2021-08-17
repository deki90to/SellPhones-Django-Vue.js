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

    # elif request.method == 'POST':
    #     tutorial_serializer = BrandsSerializer(data=request.data)
    #     if tutorial_serializer.is_valid():
    #         tutorial_serializer.save()
    #         return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 

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

@api_view(['GET', 'POST'])
def CreateBrandView(request):
    # tutorial_data = JSONParser().parse(request)
    # tutorial_serializer = BrandsSerializer(data=tutorial_data)
    tutorial_serializer = BrandsSerializer(data=request.data)

    if tutorial_serializer.is_valid():
        tutorial_serializer.save()
        return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
    # return Response(tutorial_serializer.data)


    # serializer = BrandsSerializer(brands, many=True)
    # return Response(serializer.data)