from django.urls import path
from . import views

name = 'ichan'
urlpatterns = [
    path('', views.IndexViews.as_view(), name='index'),
    path('thread/', views.ThreadListView.as_view(), name='thread_list'),
    path('thread-list/<int:pk>/', views.ThreadDetailView.as_view(), name='post'),
    path('thread-create/', views.ThreadCreateView.as_view(), name="thread_create"),
    path('thread/<int:pk>', views.CommentListView.as_view(), name="comment"),
    path('thread/<int:pk>/create', views.CommentCreateView.as_view(), name="comment_create"),
]
