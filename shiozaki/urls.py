from django.contrib import admin
from django.urls import path
from . import views

app_name = 'shiozaki'
urlpatterns = [
    path('', views.ShiozakiView.as_view(), name='shiozaki'),
]
