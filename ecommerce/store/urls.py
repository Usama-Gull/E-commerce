from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('cart/',views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('product/', views.product, name="product"),
    path('update_item/', views.updateitem, name="update_item"),
]
