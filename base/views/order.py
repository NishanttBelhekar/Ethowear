from django.shortcuts import render
from base.models.orders import Order
from django.views import View

class OrderView(View):
    def get(self, request):
        # Retrieve the customer ID from the session
        customer_id = request.session.get('customer')
        
        # Retrieve orders associated with the customer ID
        orders = Order.get_orders_by_customer(customer_id)
        
        # Pass the orders to the template for rendering
        return render(request, 'order.html', {'orders': orders})
