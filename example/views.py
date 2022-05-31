from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from example.models import UserAPIKey
from example.serializers import UserSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class APIKeyView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user

        if hasattr(user, "api_key"):
            user.api_key.delete()

        api_key, key = UserAPIKey.objects.create_key(name=user.username, user=user)

        return Response({"api_key": key}, status=status.HTTP_200_OK)


class SessionSignInView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]

    def post(self, request, *args, **kwargs):
        username = request.data["username"]
        password = request.data["password"]

        user = authenticate(request, username=username, password=password)
        login(request, user)
        return Response(self.get_serializer(user).data, status=status.HTTP_201_CREATED)


class TokenSignInView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        username = request.data["username"]
        password = request.data["password"]

        user = authenticate(request, username=username, password=password)
        token = Token.objects.get_or_create(user=user)

        return Response({"token": str(token[0])}, status=status.HTTP_201_CREATED)
