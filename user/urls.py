from django.contrib import admin
from django.urls import path , include
from user import views

urlpatterns = [
    path('signup/', views.signupUser),
    path('login/' , views.loginUser),
    path('logout/' , views.logoutUser),
    path('trip/' , views.gettrips),
]
