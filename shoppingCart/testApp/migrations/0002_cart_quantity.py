# Generated by Django 3.0.2 on 2020-01-15 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
