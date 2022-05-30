from django.urls import path

from example.views import UserListView, APIKeyView

urlpatterns = [
    path("users/", UserListView.as_view()),
    path("auth/signin/", APIKeyView.as_view()),
]
