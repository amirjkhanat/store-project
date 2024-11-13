from django.urls import path
from cart.views import AddToCartView, RemoveFromCartView, RemoveSingleView
from accounts.views import AccountLogin, AccountLogout, AccountRegister, user_delete

app_name = 'accounts'

urlpatterns = [
    path('login/', AccountLogin.as_view(), name='login'),
    path('logout/', AccountLogout.as_view(), name='logout'),
    path('delete/', user_delete, name='delete'),
    path('register/', AccountRegister.as_view(), name='register'),
    path('add-to-cart/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('remove-single-from-cart/<int:product_id>/', RemoveSingleView.as_view(), name='remove_single_from_cart'),
]