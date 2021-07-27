from django.contrib import admin
from django.urls import path
from .Views import home, login, signup, cart, checkout, orders
from .middleware.auth import auth_middleware

# url mapping
urlpatterns = [
    path('', home.Index.as_view(), name='homepage'),
    path('index', home.Index.as_view()),
    path('search', home.Search.as_view(), name='search'),
    path('signup', signup.Signup.as_view(), name="signup"),
    path('login', login.Login.as_view(), name='login'),
    path('logout', login.Logout, name='logout'),
    path('cart', cart.Cart.as_view(), name='cart'),
    path('check-out', checkout.CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(orders.OrderView.as_view()), name='order'),

]
