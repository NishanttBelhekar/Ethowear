from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from base import views
from .views import men, common
# from .views.men import Shop 
from .views.login import Login , logout
from .views.register import Register 
from .views.common import  Proddetails
from .views.men import Men
from .views.home import Items
from .views.cart import Cart
from .views.payment import Payment
from .views.order import OrderView


urlpatterns = [
    path('', Items.as_view(), name="home"),
    path('men/',Men.as_view(), name="men"),
    path('women/',common.women, name="women"),
    path('contact/',common.contact, name="contact"),
    path('about/',common.about, name="about"),
    path('men/productspage/<str:id>',Proddetails.as_view(), name="productdetails"),
    path('cart/',Cart.as_view(), name="cart"),
    path('register/',Register.as_view(), name="register"),
    path('login/',Login.as_view(), name="login"),
    path('logout/',logout, name="logout"),
    path('payment/',Payment.as_view(), name="payment"),
    path('response/',common.response, name="response"),
    path('order/',OrderView.as_view(), name="order"),

    # path('order/',views.order, name="order "),

] 
