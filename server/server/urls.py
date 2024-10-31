"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSet, CategoryViewSet
from cart.views import AddToCartView
from cart.views import CartDetailView

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('categories/', include('products.urls.categories')),
    path('accounts/', include('accounts.urls')),
    path('', include('main.urls')),
path('add-to-cart/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
path('cart/', CartDetailView.as_view(), name='cart_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
