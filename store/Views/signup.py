from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.views import View
from django.contrib.auth.hashers import make_password


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        # Access user information
        PostData = request.POST
        first_name = PostData.get('firstname')
        last_name = PostData.get('lastname')
        phone = PostData.get('phone')
        email = PostData.get('email')
        password = PostData.get('password')

        # Fetching Data If validation is wrong.
        value = {"first_name": first_name,
                 "last_name": last_name,
                 "phone": phone,
                 "email": email}

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = None
        error_message = self.ValidateCustomer(customer)

        # saving Data In Admin Panel
        if not error_message:
            customer.password = make_password(customer.password)
            customer.save()
            return redirect('homepage')  # redirect the homepage for showing the index page after the signup
        else:
            data = {"error": error_message, "values": value}
            return render(request, 'signup.html', data)

    # validation
    def ValidateCustomer(self, customer):
        error_message = None

        if not customer.first_name:
            error_message = "First Name Required!"
        elif len(customer.first_name) < 4:
            error_message = "First Name Must Be 4 Characters Long Or More"
        elif not customer.last_name:
            error_message = "Last Name Required"
        elif len(customer.last_name) < 2:
            error_message = "Last Name Must Be 2 Characters Long Or More"
        elif not customer.phone:
            error_message = "Phone Number Is Required"
        elif len(customer.phone) < 10:
            error_message = "Phone Number Must Be 10 Digits"
        elif len(customer.email) < 10:
            error_message = "This is Not a Valid Email"
        elif len(customer.password) <= 6:
            error_message = "Your password is too short"
        elif len(customer.password) >= 20:
            error_message = "Your password is too long"
        elif customer.IsExist():
            error_message = "Email Address Already Registered."

        return error_message



