from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import HasAPIKey

from example.serializers import UserSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [HasAPIKey]


class APIKeyView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        try:
            user = queryset.get(username=request.data["username"])
            if not check_password(request.data["password"], user.password):
                raise ValidationError("Invalid password")
        except (User.DoesNotExist, ValidationError):
            return Response(
                {"message": "Invalid username or password"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        if APIKey.objects.filter(name__exact=request.data["username"]).exists():
            APIKey.objects.filter(name__exact=request.data["username"]).delete()

        api_key, key = APIKey.objects.create_key(name=request.data["username"])
        return Response({"api_key": key}, status=status.HTTP_200_OK)
