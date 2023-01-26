from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('wordcounter', views.word_counter, name="word_counter"),
    path('counter', views.counter, name="counter"),
    path('register', views.register, name='register'),
    path('login', views.login, name="login")
]