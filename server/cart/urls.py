# cart/urls.py
from django.urls import path
from . import views
from .views import OrderView

app_name = 'cart'
urlpatterns = [
    path('', OrderView.as_view(), name='place_order'),
    path('success/', views.order_success, name='order_success'),
]