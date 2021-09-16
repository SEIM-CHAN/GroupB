from django.contrib import admin
from . import views
from django.urls import path, include

app_name = 'koizumi'
urlpatterns = [
    path('', views.IndexView.as_view(), name='koizumi' ),
]
