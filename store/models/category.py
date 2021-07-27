from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='store/static', default = '')

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name
