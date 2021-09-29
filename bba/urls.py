from django.urls import path
from . import views

app_name = 'bba'
urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('thread/', views.ThreadListView.as_view(), name='thread'),
    path('thread_create/',views.ThreadCreateView.as_view(), name="thread_create"),
    path('comment/<int:pk>/', views.CommentListView.as_view(), name='comment'),
    path('comment_create/', views.CommentCreateView.as_view(), name='comment_create'),
    # path('bba-detail/<int:pk>', views.BbaListView.as_view(), name='bba_detail'),
    # path('bba-create/', views.BbaListView.as_view(), name='bba_create'),
]
