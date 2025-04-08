from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Gallery
from users.models import CustomUserModel
from .service import file_email_thread

@receiver(post_save, sender=Gallery)
def file_create(sender, instance, created, **kwargs):
    if created:
        file_email_thread(instance.user)
    else:
        print(f'{instance} update qilindi!')