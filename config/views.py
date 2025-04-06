from django.utils.translation import activate
from django.shortcuts import redirect

def set_language(request, language_code):
    activate(language_code)
    return redirect(request.GET.get('next', '/'))