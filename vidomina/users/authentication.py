from django.contrib.auth.models import User

class AuthenticationBackendAnonymous:
    def authenticate(self, user=None):
        if not user.get_profile() or not user.get_profile().anonymous:
            user = None
        return user