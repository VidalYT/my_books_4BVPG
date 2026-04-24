    # -*- coding: utf-8 -*-
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import Book, Category

# Create your views here.
def home(request):
    books = Book.objects.filter(status=Book.ACTIVE).order_by('-created_at')
    context = {
        'books': books
    }
    return render(request, 'book/home.html', context)

def detail(request, id):
    books = get_object_or_404(Book, id=id, status=Book.ACTIVE)
    context = {
        'books': books,
    }
    return render(request, 'book/detail_book.html', context)
