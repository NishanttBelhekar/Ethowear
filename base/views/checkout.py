from django.shortcuts import render, redirect
from base.models.customer import Customer
from django.contrib.auth.hashers import  check_password
from django.views import View
from base.models.product import Product

class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.POST.get('customer')
        print(address, phone, customer)
        return redirect('Payment')

   
 

          
        
           

    