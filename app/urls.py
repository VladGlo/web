from django.urls import path

from . import views

urlpatterns = [
    path('lab7', views.lab7, name='lab7'),
    path('lab8', views.lab8, name='lab8'),
    path('lab9', views.lab9, name='lab9'),
]