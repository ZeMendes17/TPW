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


def booksearch(request):
    if 'query' in request.POST:
        query = request.POST['query']
        if query:
            books = Book.objects.filter(title__icontains=query)
            return render(request, 'booklist.html', {'books': books, 'query': query})
        else:
            return render(request, 'booksearch.html', {'error': True})
    else:
        return render(request, 'booksearch.html', {'error': False})


def authorsearch(request):
    if 'query' in request.POST:
        query = request.POST['query']
        if query:
            authors = Author.objects.filter(name__icontains=query)
            return render(request, 'authorlist.html', {'authors': authors, 'query': query})
        else:
            return render(request, 'authorsearch.html', {'error': True})
    else:
        return render(request, 'authorsearch.html', {'error': False})


def listBooksBy(request):
    # we will serch by author and/or publisher, thus there will be two queries
    if 'author' in request.POST and 'publisher' in request.POST:
        author = request.POST['author']
        publisher = request.POST['publisher']
        if author and publisher:
            books = Book.objects.filter(authors__name__icontains=author, publisher__name__icontains=publisher)
            return render(request, 'booklistBy.html', {'books': books, 'author': author, 'publisher': publisher})
        elif author:
            books = Book.objects.filter(authors__name__icontains=author)
            return render(request, 'booklistBy.html', {'books': books, 'author': author})
        elif publisher:
            books = Book.objects.filter(publisher__name__icontains=publisher)
            return render(request, 'booklistBy.html', {'books': books, 'publisher': publisher})
        else:
            return render(request, 'listBooksBy.html', {'error': True})
    else:
        return render(request, 'listBooksBy.html', {'error': False})


def insertAuthor(request):
    if 'name' in request.POST and 'email' in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        if name and email:
            a = Author(name=name, email=email)
            a.save()
            return render(request, 'insertAuthor.html', {'success': True})
        else:
            return render(request, 'insertAuthor.html', {'error': True})
    else:
        return render(request, 'insertAuthor.html', {'error': False})


def insertPublisher(request):
    if 'name' in request.POST and 'city' in request.POST and 'country' in request.POST and 'website' in request.POST:
        name = request.POST['name']
        city = request.POST['city']
        country = request.POST['country']
        website = request.POST['website']
        if name and city and country and website:
            p = Publisher(name=name, city=city, country=country, website=website)
            p.save()
            return render(request, 'insertPublisher.html', {'success': True})
        else:
            return render(request, 'insertPublisher.html', {'error': True})
    else:
        return render(request, 'insertPublisher.html', {'error': False})


def insertBook(request):
    if request.method == 'GET':
        return render(request, 'insertBook.html', {'authors': Author.objects.all(), 'publishers': Publisher.objects.all()})

    if 'title' in request.POST and 'date' in request.POST and 'authors' in request.POST and 'publisher' in request.POST:
        title = request.POST['title']
        date = request.POST['date']
        authors = request.POST.getlist('authors')
        publisher = request.POST['publisher']
        if title and date and authors and publisher:
            b = Book(title=title, date=date, publisher=publisher, authors=authors)
            b.save()
            return render(request, 'insertBook.html', {'success': True})
        else:
            return render(request, 'insertBook.html', {'error': True})