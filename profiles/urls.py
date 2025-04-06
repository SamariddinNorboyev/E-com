
from django.urls import path
from order.urls import app_name
from . import views
app_name = 'profiles'
urlpatterns = [
    path('profiles/', views.ProfileUpdateView.as_view(), name='profiles'),
]
