from django.contrib.auth.models import User
from rest_framework import generics, mixins
from rest_framework.response import Response

from example.permissions import HasAPIKeyOrReadOnly
from example.serializers import UserSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [HasAPIKeyOrReadOnly]
