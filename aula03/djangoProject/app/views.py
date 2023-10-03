from django.shortcuts import render
from app.models import Book


# Create your views here.
def listTitles(request):
    books = Book.objects.all()
    return render(request, 'listTitles.html', {'books': books})


def book(request, book_id):
    b = Book.objects.get(id=book_id)
    return render(request, 'book.html', {'book': b})
