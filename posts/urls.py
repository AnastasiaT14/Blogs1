from django.urls import path
from . import views

urlpatterns = [
    path('posts/create/', views.PostsCreate.as_view(), name='posts-create'),
    path('posts/', views.PostsList.as_view(), name='posts-list'),
    path('posts/<int:pk>/', views.PostsDetail.as_view(), name='posts-detail'),
    path('posts/<int:pk>/update/', views.PostsUpdate.as_view(), name='posts-update'),
    path('posts/<int:pk>/delete/', views.PostsDelete.as_view(), name='posts-delete'),
]
