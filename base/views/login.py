from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from base.models.customer import Customer
from django.views import View



class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            # if password == customerpas:
            if flag:
                    request.session['customer'] = customer.id
                    request.session['email'] = email
                    return redirect('home')
            else:
                error_message = 'Email or Password invalid !!!'
        else:
            error_message = 'Email or Password invalid !!!'
        # print(flag)
        print(customer)
        print(email, password)
        return render(request, 'login.html', {'error' : error_message} )
        # return render(request, 'home.html')


def logout(request):
    request.session.clear()
    return redirect('login')


    