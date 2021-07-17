from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.BrandView),
    path('models/', views.ModelView),
    path('specs/<pk>/', views.SpecsView)
]
