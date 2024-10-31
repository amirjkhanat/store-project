from django.shortcuts import redirect
from django.views import View
from carton.cart import Cart
from products.models import Product
from django.shortcuts import render

class CartDetailView(View):
    def get(self, request):
        cart = Cart(request.session)
        return render(request, 'cart/cart_detail.html', {'cart': cart})

class AddToCartView(View):
    def post(self, request, product_id):
        cart = Cart(request.session)
        product = Product.objects.get(id=product_id)
        cart.add(product, price=product.price_now)
        return redirect('cart_detail')

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
