from django.urls import path

from example.views import UserListView, LoginView

urlpatterns = [
    path("users/", UserListView.as_view()),
    path("auth/signin/", LoginView.as_view()),
]
