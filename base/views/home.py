from django.shortcuts import render, redirect
from django.views import View
from base.models.product import Product
from base.models.category import Category

class Items(View):
    def post(self, request):
        product_id = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart', {})

        if cart:
            quantity = cart.get(product_id, 0)
            if remove:
                if quantity <= 1:
                    cart.pop(product_id, None)
                else:
                    cart[product_id] = quantity - 1
            else:
                cart[product_id] = quantity + 1
        else:
            cart = {product_id: 1 if not remove else 0}

        request.session['cart'] = cart
        return redirect('men')  # Assuming 'men' is the URL name for the page where the form is located

    def get(self, request):
        print('You are:', request.session.get('email'))
        return render(request, 'home.html', {})  # Adjust context as needed
