from rest_framework import generics
from .models import Posts
from .serializers import PostsSerializer
from rest_framework import permissions


class PostsCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class PostsList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class PostsDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class PostsUpdate(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class PostsDelete(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
