from django.contrib.auth import get_user_model
from django.db import models
from rest_framework_api_key.models import AbstractAPIKey


class UserAPIKey(AbstractAPIKey):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name="api_key"
    )

    class Meta:
        db_table = "user_api_key"
