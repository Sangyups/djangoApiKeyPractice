from rest_framework.permissions import SAFE_METHODS
from rest_framework_api_key.permissions import HasAPIKey


class HasAPIKeyOrReadOnly(HasAPIKey):
    def has_permission(self, request, view) -> bool:
        key = self.get_key(request)

        if request.method in SAFE_METHODS:
            return True

        if not key:
            return False
        return self.model.objects.is_valid(key)
