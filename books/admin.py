from django.contrib import admin

# Adding some lines for the Admin funcions.
from .models import Category, Book

admin.site.register(Category)
admin.site.register(Book)