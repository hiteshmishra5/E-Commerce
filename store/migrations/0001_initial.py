# Generated by Django 3.1.3 on 2020-12-23 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(default='', max_length=40)),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
    ]
