from django.shortcuts import render, redirect
from base.models.customer import Customer
from base.models.orders import Order
from django.views import View
from base.models.product import Product
from django.db import models
from django.contrib import messages

class Payment(View):
    def post(self, request):
        try:
            Mail = request.POST.get('Email')
            customer = request.POST.get('customer')
            address = request.POST.get('Address')
            cart = request.session.get('cart')
            products = Product.get_products_by_id(list(cart.keys()))

            for product in products:
                order = Order(customer=Customer(id=customer),
                              product=product,
                              price=product.price * cart.get(str(product.id)),
                              address=address,
                              quantity=cart.get(str(product.id)))
                order.placeOrder()

            request.session['cart'] = {}

            # Add success message
            messages.success(request, 'Payment successful.')

        except Exception as e:
            # Add failure message
            messages.error(request, f'Payment failed: {str(e)}')

        return redirect('payment')

    def get(self, request):
        ids=list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'payment.html', {'products' : products})

   