from django.contrib import admin
from django.urls import path, include
from .views import slider_view

urlpatterns = [
    path('', slider_view, name='home'),
]