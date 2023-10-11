from django.shortcuts import render
from app.models import Book, Author, Publisher
from app.forms import BookQueryForm, AuthorQueryForm, ListBooksByForm, InsertAuthorForm, InsertPublisherForm, InsertBookForm


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
        return render(request, 'insertBook.html',
                      {'authors': Author.objects.all(), 'publishers': Publisher.objects.all()})

    if 'title' in request.POST and 'date' in request.POST and 'authors' in request.POST and 'publisher' in request.POST:
        print("ola")
        title = request.POST['title']
        date = request.POST['date']
        au = request.POST.getlist('authors')
        pub = request.POST['publisher']
        pub = Publisher.objects.get(name=pub)
        if title and date and au and pub:
            b = Book.objects.create(title=title, date=date, publisher=pub)
            for a in au:
                a = Author.objects.get(name=a)
                b.authors.add(a)
            b.save()
            return render(request, 'insertBook.html', {'success': True})
        else:
            return render(request, 'insertBook.html', {'error': True})
    else:
        print("ola2")
        return render(request, 'insertBook.html', {'error': False})


def updateAuthor(request):
    if request.method == 'GET':
        return render(request, 'updateAuthor.html', {'authors': Author.objects.all()})

    for a in Author.objects.all():
        if ("name___" + str(a.id)) in request.POST and ("email___" + str(a.id)) in request.POST:
            name = request.POST["name___" + str(a.id)]
            email = request.POST["email___" + str(a.id)]
            if name and email:
                if a.name != name:
                    a.name = name
                    a.save()
                if a.email != email:
                    a.email = email
                    a.save()

            else:
                return render(request, 'updateAuthor.html', {'error': True, 'authors': Author.objects.all()})
        else:
            return render(request, 'updateAuthor.html', {'error': True, 'authors': Author.objects.all()})

    return render(request, 'updateAuthor.html', {'success': True, 'authors': Author.objects.all()})


def updatePublisher(request):
    if request.method == 'GET':
        return render(request, 'updatePublisher.html', {'publishers': Publisher.objects.all()})

    for p in Publisher.objects.all():
        if ("name___" + str(p.id)) in request.POST and ("city___" + str(p.id)) in request.POST and (
                "country___" + str(p.id)) in request.POST and ("website___" + str(p.id)) in request.POST:
            name = request.POST["name___" + str(p.id)]
            city = request.POST["city___" + str(p.id)]
            country = request.POST["country___" + str(p.id)]
            website = request.POST["website___" + str(p.id)]
            if name and city and country and website:
                if p.name != name:
                    p.name = name
                    p.save()
                if p.city != city:
                    p.city = city
                    p.save()
                if p.country != country:
                    p.country = country
                    p.save()
                if p.website != website:
                    p.website = website
                    p.save()
            else:
                return render(request, 'updatePublisher.html', {'error': True, 'publishers': Publisher.objects.all()})
        else:
            return render(request, 'updatePublisher.html', {'error': True, 'publishers': Publisher.objects.all()})

    return render(request, 'updatePublisher.html', {'success': True, 'publishers': Publisher.objects.all()})


def updateBook(request):
    if request.method == 'GET':
        return render(request, 'updateBook.html', {'books': Book.objects.all(), 'publishers': Publisher.objects.all(), 'authors': Author.objects.all()})

    for b in Book.objects.all():
        if ("title___" + str(b.id)) in request.POST and ("date___" + str(b.id)) in request.POST and ("publisher___" + str(b.id)) in request.POST:
            title = request.POST["title___" + str(b.id)]
            date = request.POST["date___" + str(b.id)]
            authList = []
            for auth in Author.objects.all():
                if ("authors___" + str(b.id) + "___" + str(auth.id)) in request.POST:
                    authList.append(auth)
            pub = request.POST["publisher___" + str(b.id)]
            pub = Publisher.objects.get(id=pub)
            if title and date and authList and pub:
                if b.title != title:
                    b.title = title
                    b.save()
                if b.date != date:
                    b.date = date
                    b.save()
                if b.publisher != pub:
                    b.publisher = pub
                    b.save()
                if b.authors != authList:
                    b.authors.clear()
                    for a in authList:
                        a = Author.objects.get(name=a)
                        b.authors.add(a)
                    b.save()
            else:
                return render(request, 'updateBook.html', {'error': True, 'books': Book.objects.all(), 'publishers': Publisher.objects.all(), 'authors': Author.objects.all()})
        else:
            return render(request, 'updateBook.html', {'error': True, 'books': Book.objects.all(), 'publishers': Publisher.objects.all(), 'authors': Author.objects.all()})

    return render(request, 'updateBook.html', {'success': True, 'books': Book.objects.all(), 'publishers': Publisher.objects.all(), 'authors': Author.objects.all()})


def bookquery(request):
    if request.method == 'POST':
        form = BookQueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            books = Book.objects.filter(title__icontains=query)
            return render(request, 'booklist.html', {'books': books, 'query': query})
    else:
        form = BookQueryForm()
    return render(request, 'bookquery.html', {'form': form})


def authorquery(request):
    if request.method == 'POST':
        form = AuthorQueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            authors = Author.objects.filter(name__icontains=query)
            return render(request, 'authorlist.html', {'authors': authors, 'query': query})
    else:
        form = AuthorQueryForm()
    return render(request, 'bookquery.html', {'form': form})


def bookauthpubquery(request):
    if request.method == 'POST':
        form = ListBooksByForm(request.POST)
        if form.is_valid():
            author_name = form.cleaned_data['author_name']
            publisher_name = form.cleaned_data['publisher_name']
            books = Book.objects.filter(authors__name__icontains=author_name, publisher__name__icontains=publisher_name)
            return render(request, 'booklist.html', {'books': books, 'author': author_name, 'publisher': publisher_name})
    else:
        form = ListBooksByForm()
    return render(request, 'bookquery.html', {'form': form})


def insertauthorform(request):
    if request.method == 'POST':
        form = InsertAuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            if name and email:
                a = Author(name=name, email=email)
                a.save()
                return render(request, 'insert.html', {'success': True, 'form': InsertAuthorForm()})
            else:
                return render(request, 'insert.html', {'error': True, 'form': InsertAuthorForm()})
    else:
        form = InsertAuthorForm()
    return render(request, 'insert.html', {'form': form})


def insertpublisherform(request):
    if request.method == 'POST':
        form = InsertPublisherForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            country = form.cleaned_data['country']
            website = form.cleaned_data['website']
            if name and city and country and website:
                p = Publisher(name=name, city=city, country=country, website=website)
                p.save()
                return render(request, 'insert.html', {'success': True, 'form': InsertPublisherForm()})
            else:
                return render(request, 'insert.html', {'error': True, 'form': InsertPublisherForm()})
    else:
        form = InsertPublisherForm()
    return render(request, 'insert.html', {'form': form})


def insertbookform(request):
    if request.method == 'POST':
        form = InsertBookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            date = form.cleaned_data['date']
            publisher = form.cleaned_data['publisher']
            authors = form.cleaned_data['author']
            if title and date and publisher and authors:
                b = Book(title=title, date=date, publisher=publisher)
                b.save()
                for a in authors:
                    b.authors.add(a)
                b.save()
                return render(request, 'insert.html', {'success': True, 'form': InsertBookForm()})
            else:
                return render(request, 'insert.html', {'error': True, 'form': InsertBookForm()})
    else:
        form = InsertBookForm()
    return render(request, 'insert.html', {'form': form})