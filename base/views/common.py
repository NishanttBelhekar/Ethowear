from django.shortcuts import render, redirect
from django.http import HttpResponse
from base.models.product import Product
from django.views import View



# Create your views here.

# def home(request):
#     return render(request, 'home.html')


def women(request):
    return render(request, 'mens.html')


def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def addtocart(request):
    return render(request, 'addtocart.html')

def payment(request):
    return render(request, 'payment.html')

def response(request):
    return render(request, 'Response.html')


class Proddetails(View):

    def post(self, request):
        productt = request.POST.get('product.id')
        print(productt)
        redirect('Home')



    def get(self, request, id):
        productt = Product.objects.filter(id = id).first
        data = {
            'productt' : productt
        }
        # print(productt)
        return render(request, 'singleproduct.html',data)



