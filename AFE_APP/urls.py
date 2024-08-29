from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('reports', views.reports, name='reports'),
    path('resources', views.resources, name='resources'),
    path('resources-detail', views.resources_detail, name='resources_detail'),
  
]