from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import BlogsSerializer, UserSerializer, GroupSerializer
from .models import Blogs


class BlogPostsViewSet(APIView):
    """
    API endpoint that allows blog posts to be viewed or edited.
    """
    serializer_class = BlogsSerializer

    def get_queryset(self):
        return Blogs.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        blogs = self.get_queryset()
        serializer = self.serializer_class(blogs, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]