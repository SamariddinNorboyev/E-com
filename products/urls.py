from django.contrib import admin
from django.urls import path
from . import views
app_name = 'products'
urlpatterns = [
    path('', views.home, name='home_page'),
    path('moderation/', views.moderation, name='moderation'),
    path('create/', views.create, name='create'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('view/<int:id>', views.view, name='view'),
    path('delete/<int:id>', views.delete, name='delete'),
]