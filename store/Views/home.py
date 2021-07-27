from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.db.models import Q
from django.views import View
 


# Create your views here.

# This is for home

class Index(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        categories = Category.get_all_categories()
        category_ID = request.GET.get('category')

        if category_ID:
            products = Product.get_all_products_by_id(category_ID)
        else:
            products = Product.get_all_products()
        data = {"product": products,
                "categorys": categories}

        return render(request, 'index.html', data)

    # This is for cart

    def post(self, request):
        products_id = request.POST.get('product')
        remove = request.POST.get('remove')  # if user remove the cart product this remove and products is alwaya take value
        cart = request.session.get('cart')  # getting session, accessing cart product
        if cart:
            quantity = cart.get(products_id)  # accessing user_product_id: quantity
            if quantity:
                if remove:  # it works onyl: - if user remove any product
                    if quantity == 1:  # it works only: - if products quantity is 1 like (1 in cart) and user is going to remove this product
                        cart.pop(products_id)
                    else:
                        cart[products_id] = quantity - 1
                else:
                    cart[products_id] = quantity + 1
            else:
                cart[products_id] = 1
        else:
            cart = {}
            cart[products_id] = 1
        request.session['cart'] = cart  # set session

        return redirect('homepage')


# this is for search

class Search(View):
    def get(self, request):
        categories = Category.get_all_categories()
        search = request.GET.get('search')
        if search:
            products = Product.objects.filter(
                Q(name__icontains=search) | Q(search_for_name__icontains=search))  # Filter product with Q object
        else:
            products = Product.get_all_products()

        data = {"product": products,
                "categorys": categories}
        return render(request, 'index.html', data)
