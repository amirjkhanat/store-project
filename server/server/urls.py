# server/urls.py
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSet, CategoryViewSet
from cart.views import AddToCartView, CartDetailView
from products.views.products import product_detail

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('products/', include('products.urls.categories')),
    path('accounts/', include('accounts.urls')),
    path('', include('main.urls')),
    path('add-to-cart/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartDetailView.as_view(), name='cart_detail'),
    path('order/', include('cart.urls')),
    path('products/<int:id>/', product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)