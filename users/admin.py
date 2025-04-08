from django.contrib import admin

from users.models import CustomUserModel, Code, Gallery
# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(Code)
admin.site.register(Gallery)