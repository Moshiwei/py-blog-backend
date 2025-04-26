from django.urls import path
from .views import BlogPostsViewSet

urlpatterns = [
    path('posts/', BlogPostsViewSet.as_view(), name='blog-posts'),
]