from django.urls import path
from . import views

name = 'ichan'
urlpatterns = [
    path('', views.IndexViews.as_view(), name='index'),
]
