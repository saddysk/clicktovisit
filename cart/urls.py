from django.urls import path
from cart import views

from django.shortcuts import render
from django.http import HttpResponse

urlpatterns = [
    path('addtocart/', views.AddToCart),
    path('<str:id>', views.MyCart),
    path('gethotel/', views.getHotel),
    path('deletebooking/', views.DeleteBooking),
]