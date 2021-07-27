from django.shortcuts import redirect
from django.views import View
from store.models.product import Product
from store.models.orders import Order
from store.models.customer import Customer


class CheckOut(View):
    def post(self, request):
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))

        for product in products:
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()

        request.session['cart'] = {}
        return redirect('cart')



