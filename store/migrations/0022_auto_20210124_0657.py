# Generated by Django 3.1.3 on 2021-01-24 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_auto_20210123_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='saving',
            field=models.CharField(default=0, max_length=10),
        ),
    ]