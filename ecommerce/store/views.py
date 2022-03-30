from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request,'index.html')

def product(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request,'Product_page.html',context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = { }
        order = {'get_cart_total':0}

    context = {'items':items, 'order':order}
    return render(request,'cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = { }
        order = {'get_cart_total':0}

    context = {'items':items, 'order':order}
    return render(request,'checkout.html',context)

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')
