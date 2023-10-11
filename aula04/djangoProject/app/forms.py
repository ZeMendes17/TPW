from django import forms
from app.models import Book, Author, Publisher

class BookQueryForm(forms.Form):
    query = forms.CharField(label='Search:', max_length=100)

class AuthorQueryForm(forms.Form):
    query = forms.CharField(label='Search:', max_length=100)

class ListBooksByForm(forms.Form):
    author_name = forms.CharField(label='Author Name:', max_length=100)
    publisher_name = forms.CharField(label='Publisher Name:', max_length=100)

class InsertAuthorForm(forms.Form):
    name = forms.CharField(label='Author Name:', max_length=100)
    email = forms.CharField(label='Author Email:', max_length=100)

class InsertPublisherForm(forms.Form):
    name = forms.CharField(label='Publisher Name:', max_length=100)
    city = forms.CharField(label='Publisher City:', max_length=100)
    country = forms.CharField(label='Publisher Country:', max_length=100)
    website = forms.CharField(label='Publisher Website:', max_length=100)

class InsertBookForm(forms.Form):
    title = forms.CharField(label='Book Title:', max_length=100)
    date = forms.DateField(label='Book Date (YYYY-MM-DD):')
    publishers = Publisher.objects.all()
    publisher = forms.ModelChoiceField(queryset=publishers, label='Publisher Name:', to_field_name="name", required=True)
    authors = Author.objects.all()
    # check box list of authors
    author = forms.ModelMultipleChoiceField(queryset=authors, label='Author Name:', to_field_name="name", required=True)