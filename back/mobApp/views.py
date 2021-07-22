from . models import Specs, Brand, Model
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import SpecsSerializer, BrandSerializer, ModelSerializer
# Create your views here.

@api_view(['GET'])
def BrandView(request):
    brand = Brand.objects.all()
    serializer = BrandSerializer(brand, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ModelView(request):
    model = Model.objects.all()
    serializer = ModelSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def SpecsView(request, pk):
    specs = Specs.objects.get(pk=pk)
    serializer = SpecsSerializer(specs, many=False)
    return Response(serializer.data)

