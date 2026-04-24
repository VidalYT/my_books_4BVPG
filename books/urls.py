from django.contrib import admin
from django.urls import path
from .views import home, detail

urlpatterns = [
    path('', home, name='home'),
    path('book/<int:id>/', detail, name='detail'),
]
