# Generated by Django 3.0.2 on 2020-01-15 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0003_remove_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]