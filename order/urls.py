from django.urls import path
from . import views
app_name = 'order'
urlpatterns = [
    path('', views.order_home, name='order_home'),
    path('add_to_order/<int:id>', views.add_to_order, name='add_to_order'),
    path('substract_to_order/<int:id>', views.substract_to_order, name='substract_to_order'),
    path('view_order/', views.view_order, name='view_order'),

    path('addorder/<int:id>', views.addorder, name='addorder'),
    path('substractorder/<int:id>', views.substractorder, name='substractorder'),
]