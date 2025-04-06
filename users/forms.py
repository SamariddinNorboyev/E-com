from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from users.models import CustomUserModel, Code
from django.utils import timezone

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = authenticate(email = email, password = password)
        if not user:
            raise ValidationError('Email yoki Password xato!')
        return cleaned_data

class RegistrForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ['email', 'password', 'first_name', 'last_name']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        pass
    def save(self):
        user = CustomUserModel.objects.create_user(**self.cleaned_data)
        return user



class ResetPasswordForm(forms.Form):
    email = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        user = CustomUserModel.objects.filter(email = email).first()
        if not user:
            raise ValidationError('Bunday email yoq!')
        return cleaned_data



class RestorePasswordForm(forms.Form):
    email = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    code = forms.CharField(max_length=4, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    re_password = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        code = cleaned_data.get('code')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')
        if password != re_password:
            return ValidationError('Password va re password bir xil emas')
        user = CustomUserModel.objects.filter(email = email).first()
        if not Code.objects.filter(code = code, owner = user, expiration_date__gt=timezone.now()):
            raise ValidationError(f'code topilmadi {timezone.now()}')
        return cleaned_data