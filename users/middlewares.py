from django.contrib.auth import logout
from django.utils.timezone import now

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = getattr(request, 'user', None)
        if user and user.is_authenticated:
            last_login = request.user.last_login
            if last_login:
                current_time = now()
                seconds_passed = (current_time - last_login).total_seconds()
                if seconds_passed > 300:
                    logout(request)
                    request.session.flush()
        response = self.get_response(request)
        return response

