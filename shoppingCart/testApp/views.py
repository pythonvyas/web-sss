from django.shortcuts import render,redirect,HttpResponseRedirect
from testApp.models import Product,Cart,Order
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.

def home_view(request):
	product=Product.objects.all()
	return render(request,'testApp/home.html',{'product':product})

@login_required
def addToCart_view(request,pk):
	product=Product.objects.get(pk=pk)
	cart=Cart.objects.get_or_create(product=product)
	return redirect("/cart")
	# user=Cart.objects.filter()
	# return render(request,'testApp/cart.html',{'user':user})

@login_required
def cart_view(request):
	cart=Cart.objects.filter()
	# if request.method=="POST":
	# 	form=quantityForm(request.POST)
	# 	if form.is_valid():


	return render(request,'testApp/cart.html',{'cart':cart})

#@login_required
def removeToCart_view(request,pk):
	cart=Cart.objects.get(pk=pk)
	cart.delete()
	#return get_script_prefix('/')
	#return HttpResponseRedirect(reverse('delete'))
	return redirect('/cart')



	#return HttpResponseRedirect(reverse('arch-summary', args=[1945]))

@login_required
def order_View(request):
	return render(request,'testApp/order.html')
