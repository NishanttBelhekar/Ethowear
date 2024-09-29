from django.shortcuts import render, redirect
from django.http import HttpResponse
from base.models.product import Product
from base.models.category import Category
from django.views import View

from base.models.type import Type

class Men(View):
    def post(self, request):
        product = request.POST.get('product')
        print(product)
        


    def get(self, request):
        products = Product.get_all_products()
        categories = Category.get_all_categories()
        # types = Type.get_all_types()
        types = Type.get_all_types()
        typeID = request.GET.get('type')
        categoryID = request.GET.get('category')
        typeID = request.GET.get('type')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        elif typeID:
            products = Product.get_all_products_by_typeid(typeID)
        else:
            products =Product.get_all_products()
        data = {}
        data['categories'] = categories
        data['products'] = products
        data['types'] = types
        print('you are : ',request.session.get('email'))
        return render(request, 'mens.html', data)


