from django.urls import path
from . import views

urlpatterns = [
    path('', views.BrandView),
    path('model/', views.ModelView),
    path('model/specs/<pk>/', views.SpecsView)
]
