from django.contrib.auth import logout
from django.http import JsonResponse
from django.utils.timezone import now

from users.models import Gallery
from django.utils import timezone

class LastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            # Optional: avoid writing too often
            now = timezone.now()
            last_activity = request.user.last_activity
            if not last_activity or (now - last_activity).seconds > 60:
                request.user.last_activity = now
                request.user.save(update_fields=['last_activity'])
        return response

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = getattr(request, 'user', None)
        if user and user.is_authenticated:
            last_login = request.user.last_activity
            print(last_login)
            # if last_login:
            #     current_time = now()
            #     seconds_passed = (current_time - last_login).total_seconds()
            #     if seconds_passed > 300:
            #         logout(request)
        response = self.get_response(request)
        return response

class Max5Images:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user:
            images = Gallery.objects.filter(user = user.id)
            if len(images)>5:
                raise ValueError('You can\'t create more than 5 file')
        response = self.get_response(request)
        return response


