from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request,'index.html')

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')
