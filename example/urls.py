from django.urls import path

from example.views import UserListView

urlpatterns = [path("users/", UserListView.as_view())]
