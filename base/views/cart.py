from django.shortcuts import render, redirect
from base.models.customer import Customer
from django.contrib.auth.hashers import  check_password
from django.views import View
from base.models.product import Product

class Cart(View):
    def get(self, request):
        if(request.session.get('cart') == None):
            return redirect('response')
        else:
            ids=list(request.session.get('cart').keys())
            products = Product.get_products_by_id(ids)
            print(products)
            return render(request, 'cart.html', {'products' : products})
 

          
        
           

    