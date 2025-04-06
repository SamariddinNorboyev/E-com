import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from config import settings
from .forms import LoginForm, RegistrForm, ResetPasswordForm, RestorePasswordForm
from .models import CustomUserModel
from django.contrib.auth import login, logout
from .service import send_email_in_thread

# Create your views here.
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = CustomUserModel.objects.filter(email = email).first()
            login(request, user)
            return redirect('products:home_page')
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('users:login')

class CreateView(View):
    def get(self, request):
        form = RegistrForm()
        return render(request, 'users/register.html', {'form': form})
    def post(self, request):
        form = RegistrForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
        form = RegistrForm()
        return render(request, 'users/register.html', {'form': form})






def google_loging(request):
    auth_url = (
        f"{settings.GOOGLE_AUTH_URL}"
        f"?client_id={settings.GOOGLE_CLIENT_ID}"
        f"&redirect_uri={settings.GOOGLE_REDIRECT_URI}"
        f"&response_type=code"
        f"&scope=openid email profile"
    )
    return redirect(auth_url)
def google_callback(request):
    code = request.GET.get('code')
    token_data = {
        "code": code,
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    token_response = requests.post(settings.GOOGLE_TOKEN_URL, data=token_data)
    token_json = token_response.json()
    access_token = token_json.get("access_token")
    user_info_response = requests.get(settings.GOOGLE_USER_INFO_URL, headers={"Authorization": f"Bearer {access_token}"})
    user_info = user_info_response.json()
    user, created = CustomUserModel.objects.get_or_create(google_id=user_info.get('id'), email=user_info.get('email'),
                                                          image=user_info.get('picture'),
                                                          first_name=user_info.get('given_name'),
                                                          last_name=user_info.get('family_name'))
    login(request, user)
    return redirect('products:home_page')





class ResetPasswordView(View):
    def get(self, request):
        form = ResetPasswordForm()
        return render(request, 'users/reset-password.html', {'form': form})
    def post(self, request):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            send_email_in_thread(email)
            return redirect('users:restore_password')
        form = ResetPasswordForm()
        return render(request, 'users/reset-password.html', {'form': form})



class RestorePasswordView(View):
    def get(self, request):
        form = RestorePasswordForm()
        return render(request, 'users/restore-password.html', {'form': form})
    def post(self, request):
        form = RestorePasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = CustomUserModel.objects.filter(email = email).first()
            user.set_password(password)
            user.save()
            return redirect('users:login')
        form = RestorePasswordForm()
        return render(request, 'users/restore-password.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    return render(request, 'users/profile.html', {'user': user})