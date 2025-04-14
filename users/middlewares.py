from .models import Gallery
from django.contrib.auth import logout
from django.utils import timezone
from django.utils.timezone import now
from django.http import HttpResponseForbidden

class LastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
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
            last_activity = user.last_activity
            print(f"Last activity: {last_activity}")
            if last_activity:
                current_time = now()
                seconds_passed = (current_time - last_activity).total_seconds()
                if seconds_passed > 300:
                    logout(request)
        response = self.get_response(request)
        return response

class Max5Images:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user

        if user.is_authenticated:
            print(user.groups.filter(name='Premium').exists())
            if user.groups.filter(name='Premium').exists():
                return self.get_response(request)
            image_count = Gallery.objects.filter(user=user).count()
            if image_count >= 5 and request.method == 'POST':
                return HttpResponseForbidden("You can't upload more than 5 files.")
        return self.get_response(request)