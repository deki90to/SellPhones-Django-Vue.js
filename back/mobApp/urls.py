from django.urls import path
from . import views

urlpatterns = [
    path('', views.BrandsView),
    path('models/<pk>/', views.ModelsView),
    path('specs/<pk>/', views.SpecsView),
    path('brandModels/<pk>/', views.BrandModelsView),
    path('modelSpecs/<pk>/', views.ModelSpecsView),
]
