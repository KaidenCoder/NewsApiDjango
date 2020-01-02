from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('searchtopic/', views.search, name="search_topic"),
    path('newssources/', views.sources, name="sources"),
]
