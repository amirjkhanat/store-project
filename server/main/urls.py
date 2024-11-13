from itertools import product

from django.urls import path
from main.views import (
    main, contacts
)
from products.views.categories import ProductListView
from products.views.products import product_detail
from products.views.categories import CategoryList
from products import views
from cart.views import CartDetailView


app_name = 'main'

urlpatterns = [
    path('', main, name='main'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', CategoryList.as_view(), name='category_list'),

    path('products/', ProductListView.as_view(), name='product_list'),
    path('cart/', CartDetailView.as_view(), name='cart_detail'),
    path('products/<int:id>/', product_detail, name='product_detail'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category_list'),


]
