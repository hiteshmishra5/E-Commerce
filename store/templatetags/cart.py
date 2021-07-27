from django import template

register = template.Library()


@register.filter(name='is_in_cart')  # register filter
def is_in_cart(products, cart):  # like this : cart = {'5': 6, '6': 3, '11': 1, '16': 1, '17': 2, '46': 1, '7': 1}
    keys = cart.keys()
    for id in keys:
        if int(id) == products.id:
            return True  # it return true:- if cart id and user product id is same
    return False


@register.filter(name='cart_quantity')
def cart_quantity(products, cart):  # like this : cart = {'5': 6, '6': 3, '11': 1, '16': 1, '17': 2, '46': 1, '7': 1}
    keys = cart.keys()
    for id in keys:
        if int(id) == products.id:
            return cart.get(id)  # it return all cart keys:-quantity
    return 0;


@register.filter(name='price_total')
def price_total(products, cart):
    return products.sale_price * cart_quantity(products, cart)


@register.filter(name='total_cart_price')
def total_cart_price(products, cart):
    sum = 0;
    for p in products:
        sum += price_total(p, cart)
    return sum
