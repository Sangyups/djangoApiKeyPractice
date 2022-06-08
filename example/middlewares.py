from rest_framework_api_key.permissions import KeyParser

from example.models import UserAPIKey


class CommonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        key = KeyParser.get_from_authorization(KeyParser, request)
        if key:
            request.user = UserAPIKey.objects.get_user_from_key(key)
        response = self.get_response(request)
        return response
