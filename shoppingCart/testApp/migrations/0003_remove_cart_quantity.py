# Generated by Django 3.0.2 on 2020-01-15 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0002_cart_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
    ]