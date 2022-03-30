import json

from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
# Create your views here.

def home(request):
    return render(request,'index.html')

def product(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    else:
        items = { }
        order = {'get_cart_total':0,'get_cart_items':0}
        cartitems = order['get_cart_items']


    products = Products.objects.all()
    context = {'items':items,'products':products,'cartitems':cartitems,'order':order}
    return render(request,'Product_page.html',context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items

    else:
        items = { }
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartitems = order['get_cart_items']

    context = {'items':items, 'order':order,'cartitems':cartitems}
    return render(request,'cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    else:
        items = { }
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartitems = order['get_cart_items']

    context = {'items':items, 'order':order,'cartitems':cartitems}
    return render(request,'checkout.html',context)

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')


def updateitem(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    action = data['action']
    print('action:',action)
    print('product_id:', product_id)
    customer = request.user.customer
    product = Products.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer,complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()

    return JsonResponse('item was added', safe=False)












