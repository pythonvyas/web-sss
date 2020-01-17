from django.db import models


# Create your models here.
class User(models.Model):
	user_name=models.CharField(max_length=250)
	user_email=models.EmailField()
	user_address=models.CharField(max_length=250)
	user_phone=models.IntegerField()

class Product(models.Model):
	item_name=models.CharField(max_length=250)
	item_detail=models.CharField(max_length=250)
	item_price=models.FloatField()
	item_image=models.ImageField()
	# def __str__(self):
	# 	return self.item_name

class Cart(models.Model):
	# quantity=models.PositiveIntegerField()
	# grand_total=models.PositiveIntegerField()
	product=models.ForeignKey(Product, on_delete=models.CASCADE)

class Order(models.Model):
	
	product=models.ForeignKey(Product, on_delete=models.CASCADE)
