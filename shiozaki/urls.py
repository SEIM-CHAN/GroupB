from django.contrib import admin
from django.urls import path
from . import views

#config/urls.pyにて、path('', include('shiozaki.urls')),を追加
urlpatterns = [
    path('', views.ShiozakiView.as_view(), name='shiozaki'),
]
