from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=500)

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False

    def IsExist(self):
        if Customer.objects.filter(email = self.email):
            return True
        else:
            return False

    def __str__(self):
        return (self.first_name)






