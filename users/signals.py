from django.db.models.signals import post_save
from django.dispatch import receiver

from profiles.models import Profile
from .models import Gallery
from users.models import CustomUserModel
from .service import file_email_thread

@receiver(post_save, sender=Gallery)
def file_create(sender, instance, created, **kwargs):
    if created:
        file_email_thread(instance.user)
    else:
        print(f'{instance} update qilindi!')


@receiver(post_save, sender=CustomUserModel)
def my_signal(sender, instance, created, **kwargs):
    if created:
        print(f'Yangi {sender} yaratildi: {instance}')
        #User create bo'lganda Profile model yaratamiz
        Profile.objects.create(user = instance)
    else:
        print(f'{instance} update qilindi!')