from django import forms
from books.models import Book


class EditBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"  # all Book model fields
