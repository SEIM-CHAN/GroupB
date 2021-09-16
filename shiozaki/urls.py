from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('shiozaki/', views.ShiozakiView.as_view(), name='shiozaki'),
]
