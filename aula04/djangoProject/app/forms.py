from django import forms

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