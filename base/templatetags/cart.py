from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product ,cart):
    keys = cart.keys()
    for id in keys:
        # print(type(id) , type(product.id))
        if int(id) == product.id:
            return True
    return False;


@register.filter(name='cart_quantity')
def cart_quantity(product ,cart):
    keys = cart.keys()
    for id in keys:
        # print(type(id) , type(product.id))
        if int(id) == product.id:
            return cart.get(id)
    return 0;

@register.filter(name='popout')
def popout(product ,cart):
    keys = cart.keys()
    for id in keys:
        # print(type(id) , type(product.id))
        if int(id) == product.id:
            return cart.get(id).pop()
    return 0;

@register.filter(name='price_total')
def price_total(product ,cart):
    return product.price * cart_quantity(product, cart)

   
@register.filter(name='sub_total')
def sub_total(products, cart):
    sum = 0;
    for i in products:
        sum += price_total(i, cart)
    
    return sum

@register.filter(name='total_i')
def total_i(products, cart):
    sum = 0
    ship = 40
    sum = ship + sub_total(products, cart)
    
    return sum