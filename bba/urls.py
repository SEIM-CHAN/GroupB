from django.urls import path
from . import views

app_name = 'bba'
urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    # path('bba-list/', views.BbaListView.as_view(), name='bba_list'),
    # path('bba-detail/<int:pk>', views.BbaListView.as_view(), name='bba_detail'),
    # path('bba-create/', views.BbaListView.as_view(), name='bba_create'),
]
