
from django.urls import path
from . import views
app_name = 'profiles'
urlpatterns = [
    path('profiles/', views.ProfileUpdateView.as_view(), name='profiles'),
]
