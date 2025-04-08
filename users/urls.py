
from django.urls import path
from order.urls import app_name
from . import views
app_name = 'users'
urlpatterns = [
    path('login/google/', views.google_loging, name='google_login'),
    path('google/login/callback/', views.google_callback, name='google_callback'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.CreateView.as_view(), name='register'),
    path('reset-password/', views.ResetPasswordView.as_view(), name='reset_password'),
    path('restore-password/', views.RestorePasswordView.as_view(), name='restore_password'),
    path('images/', views.ImageUpdatedView.as_view(), name='images'),
    path('profile', views.profile, name='profile'),
    path('delete_image/<int:id>', views.delete_image, name='delete_image'),
]
