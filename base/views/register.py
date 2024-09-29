from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from base.models.customer import Customer
from django.views import View




class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        email = postData.get('email')
        phone = postData.get('phone')
        password = postData.get('password')
        #validation
        value = {
            'first_name' : first_name,
            'last_name' : last_name,
            'phone' : phone,
            'email' : email
        }
        error_message = None

        customer = Customer(first_name = first_name,
                                             last_name = last_name,
                                             phone = phone,
                                             email = email,
                                             password = password)
        error_message = self.validateCustomer(customer)

        #saving
        if  not error_message :
                print(first_name, last_name, phone, email, password)
                customer.password = make_password(customer.password)
                customer.register()
                # return redirect(request,'index.html', )
                return redirect('login')
        else:
            data = {
                'error' : error_message,
                'values' : value,
            }
            return render(request , 'register.html' , data)

    def validateCustomer(self, customer):
        error_message = None;
        if(not customer.first_name):
            error_message = "First Name Required !!"
        
        elif not customer.last_name:
            error_message = "Last Name Required !!"
        
        elif not customer.phone:
            error_message = "Phone No Required !!"

        elif customer.isExists() :
            error_message = 'Email Address Already Registered...'

            return error_message