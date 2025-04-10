from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.forms.fields import ImageField
from django.utils import timezone
from datetime import timedelta

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password = None, **extra_fields):
        if not email:
            raise ValidationError('Email field majburiy!')
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValidationError('Super user staff bo\'lishi kerak')
        if extra_fields.get('is_superuser') is not True:
            raise ValidationError('Super super user bolishi kerak')
        return self.create_user(email, password, **extra_fields)

# Create your models here.
class CustomUserModel(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    google_id = models.CharField(unique=True, blank=True, null=True, max_length=255)
    image = models.URLField(blank=True, null=True)
    last_activity = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)


def time_default():
    return timezone.now()+timedelta(seconds = 30)

class Code(models.Model):
    code = models.IntegerField()
    owner = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    expiration_date = models.DateTimeField(default=time_default)
    def __str__(self):
        return str(self.code)



class Gallery(models.Model):
    image = models.ImageField(upload_to='pictures')
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return str(self.user.email)