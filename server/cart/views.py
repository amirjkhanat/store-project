from django.shortcuts import render, redirect
from django.views import View
from carton.cart import Cart
from django.urls import reverse
from products.models import Product
from django.views.decorators.csrf import csrf_protect
from .models import Order, OrderItem
from django.http import HttpResponse
from products.models import ProductCategory

class CartDetailView(View):
    def get(self, request):
        cart = Cart(request.session)
        return render(
            request, 'cart/cart_detail.html',
            {
                'cart': cart,
                'title': 'Корзина',
                'link_list': ['main/css/contacts.css'],
                'menu': ProductCategory.objects.all()
            }
        )

class AddToCartView(View):
    def post(self, request, product_id):
        cart = Cart(request.session)
        product = Product.objects.get(id=product_id)
        cart.add(product, price=product.price_now)
        return redirect('main:cart_detail')

class RemoveSingleView(View):
    def post(self, request, product_id):
        cart = Cart(request.session)
        product = Product.objects.get(id=product_id)
        cart.remove_single(product)
        return redirect('cart_detail')

class RemoveFromCartView(View):
    def post(self, request, product_id):
        cart = Cart(request.session)
        product = Product.objects.get(id=product_id)
        cart.remove(product)
        return redirect('cart_detail')

class OrderView(View):
    def get(self, request):
        return render(request, 'cart/order.html')

    def post(self, request):
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')

        if not name or not email or not address or not phone:
            return HttpResponse("All fields are required.", status=400)

        order = Order.objects.create(
            name=name,
            email=email,
            address=address,
            phone=phone
        )

        cart = Cart(request.session)
        for item in cart.items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.price
            )

        cart.clear()
        return redirect('cart:order_success')

def place_order(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')

        if not name or not email or not address or not phone:
            return HttpResponse("All fields are required.", status=400)

        order = Order.objects.create(
            name=name,
            email=email,
            address=address,
            phone=phone
        )

        # Add order items to the order
        for item in request.session.get('cart', []):
            OrderItem.objects.create(
                order=order,
                product_id=item['product_id'],
                quantity=item['quantity'],
                price=item['price']
            )

        return redirect('cart:order_success')

    return render(request, 'cart/order.html')

def order_success(request):
    return render(request, 'cart/order_success.html')