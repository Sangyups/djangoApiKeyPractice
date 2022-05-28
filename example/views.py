from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response

from example.serializers import UserSerializer


class UserListView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
