from django.contrib import admin
from django.urls import path
from . import views

app_name = 'hayat'
urlpatterns = [
    path('kimizuka', views.KimizukaView.as_view(), name="kimizuka"),
]