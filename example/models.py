from django.contrib.auth import get_user_model
from django.db import models
from rest_framework_api_key.models import AbstractAPIKey, BaseAPIKeyManager


class CustomAPIKeyManager(BaseAPIKeyManager):
    def get_user_from_key(self, key: str) -> "AbstractAPIKey":
        prefix, _, _ = key.partition(".")
        queryset = self.get_usable_keys()

        try:
            api_key = queryset.select_related("user").get(prefix=prefix)
        except self.model.DoesNotExist:
            raise  # For the sake of being explicit.

        if not api_key.is_valid(key):
            raise self.model.DoesNotExist("Key is not valid.")
        else:
            return api_key.user


class UserAPIKey(AbstractAPIKey):
    objects = CustomAPIKeyManager()

    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name="api_key"
    )

    class Meta:
        db_table = "user_api_key"
