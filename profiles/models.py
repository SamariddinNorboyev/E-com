from django.db import models

from users.models import CustomUserModel


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='pictures', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.email