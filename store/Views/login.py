from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # Access user email and password
        PostData = request.POST
        email = PostData.get("email")
        password = PostData.get("password")

        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            checking = check_password(password, customer.password)
            if checking:
                request.session['customer'] = customer.id # set session
                return redirect('homepage')
            else:
                error_message = "Email Or Password Invalid!!"
        else:
            error_message = "Email Or Password Invalid!!"
        return render(request, 'login.html', {'error': error_message})


def Logout(request):
    request.session.clear()
    return redirect('login')
