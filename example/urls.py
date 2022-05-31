from django.urls import path

from example.views import UserListView, APIKeyView, SessionSignInView, TokenSignInView

urlpatterns = [
    path("users/", UserListView.as_view()),
    path("auth/apikey/", APIKeyView.as_view()),
    path("auth/session/signin/", SessionSignInView.as_view()),
    path("auth/token/signin/", TokenSignInView.as_view()),
]
