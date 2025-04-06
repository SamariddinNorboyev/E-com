from django.core.mail import send_mail
import threading
from .utils import code_generate
from .models import Code, CustomUserModel


def send_simple_email(to):
    code = code_generate()
    user = CustomUserModel.objects.filter(email = to).first()
    print(to)
    code = Code.objects.create(code = code, owner = user)
    send_mail(
        subject="Sizga kod jo'natildi bu kodni 30 sekund ichida ishlatsa bo'ladi",
        message=f"""
            <b>{user}</b>
        
            {code.code}
            
            Agar hech nima qilmagan bo'lsangiz hech narsa qilmang!
        """,
        from_email="samariddin.grex@gmail.com",
        recipient_list=[to],
        fail_silently=False,
    )

def send_email_in_thread(to):
    thread = threading.Thread(target=send_simple_email, args=(to,))
    thread.start()