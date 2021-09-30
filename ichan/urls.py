from django.urls import path
from . import views

app_name = 'ichan'
urlpatterns = [
    path('', views.IndexViews.as_view(), name='index'),
    path('thread/', views.ThreadListView.as_view(), name='thread_list'),
    path('thread-list/<int:pk>/', views.ThreadDetailView.as_view(), name='post'),
    path('thread-create/', views.ThreadCreateView.as_view(), name="thread_create"),
    # path('thread/<int:pk>', views.CommentListView.as_view(), name="comment"),
    path('comment/<int:pk>/', views.CommentListView.as_view(), name="comment_list"),
    path('comment-create/<int:pk>/', views.CommentCreateView.as_view(), name="comment_create"),

    path('thread-delete/<int:pk>/', views.ThreadDeleteView.as_view(), name="thread_delete"),
]
