from django.shortcuts import render
from app.models import Book, Author, Publisher


# Create your views here.
def books(request):
    b = Book.objects.all()
    return render(request, 'books.html', {'books': b})


def book(request, book_id):
    b = Book.objects.get(id=book_id)
    return render(request, 'book.html', {'book': b})


def authors(request):
    a = Author.objects.all()
    return render(request, 'authors.html', {'authors': a})


def author(request, author_id):
    a = Author.objects.get(id=author_id)
    return render(request, 'author.html', {'author': a})


def publishers(request):
    e = Publisher.objects.all()
    return render(request, 'publishers.html', {'publishers': e})


def publisher(request, publisher_id):
    e = Publisher.objects.get(id=publisher_id)
    return render(request, 'publisher.html', {'publisher': e})


def booksByAuthor(request, author_id):
    a = Author.objects.get(id=author_id)
    b = Book.objects.filter(authors__name=a.name)
    return render(request, 'booksByAuthor.html', {'books': b, 'author': a})


def authorsByPublisher(request, publisher_id):
    p = Publisher.objects.get(id=publisher_id)
    a = Author.objects.filter(book__publisher__name=p.name)
    return render(request, 'authorsByPublisher.html', {'authors': a, 'publisher': p})
