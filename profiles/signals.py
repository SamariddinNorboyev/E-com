from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from users.models import CustomUserModel


@receiver(post_save, sender=CustomUserModel)
def my_signal(sender, instance, created, **kwargs):
    if created:
        print(f'Yangi {sender} yaratildi: {instance}')
        #User create bo'lganda Profile model yaratamiz
        Profile.objects.create(user = instance)
    else:
        print(f'{instance} update qilindi!')