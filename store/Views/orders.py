from django.shortcuts import render
from django.views import View
from store.models.orders import Order

class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer')
        order = Order.get_order_by_customer(customer)
        orders = order.reverse()
        return render(request, 'orders.html', {'order': orders})