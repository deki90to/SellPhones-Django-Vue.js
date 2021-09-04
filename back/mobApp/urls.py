from django.urls import path
from . import views

urlpatterns = [
    path('', views.BrandsView),
    path('brandModels/<pk>/', views.BrandModelsView),
    path('modelSpecs/<pk>/', views.ModelSpecsView),
    path('brandDelete/<pk>/', views.BrandsDeleteView),
]
