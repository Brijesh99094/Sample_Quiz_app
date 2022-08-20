from django.urls import path
from .views import *
urlpatterns = [
    path("",home,name='home'),
    path("register",register,name='register'),
    path("login",login,name='login'),
    path("logout",logout,name='logout'),
    path('about',about,name='about'),
    path('addQuestion/', addQuestion,name='addQuestion'),
]