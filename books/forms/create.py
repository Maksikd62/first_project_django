from django import forms
from books.models import Book
import datetime

class CreateBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"  # all Book model fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ініціалізуємо всі поля порожнім значенням
        for field_name, field in self.fields.items():
            field.initial = ""  # Поля будуть пустими за замовчуванням
            if field_name == 'cover':  # Робимо виключення для поля cover
                field.required = False
            
    def clean_author(self):
        author = self.cleaned_data.get("author")
        if not all(x.isalpha() or x.isspace() for x in author):
            raise forms.ValidationError("Author name must contain only letters.")
        return author

    def clean_year(self):
        year = self.cleaned_data.get("year")
        current_year = datetime.datetime.now().year
        if year > current_year:
            raise forms.ValidationError("Year cannot be greater than the current year.")
        return year

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 0:
            raise forms.ValidationError("Price must be a positive number.")
        return price

    def clean_language(self):
        language = self.cleaned_data.get("language")
        if not all(x.isalpha() or x.isspace() for x in language):
            raise forms.ValidationError("Language must contain only letters.")
        return language

    def clean_genre(self):
        genre = self.cleaned_data.get("genre")
        if not all(x.isalpha() or x.isspace() for x in genre):
            raise forms.ValidationError("Genre must contain only letters.")
        return genre
    
    def clean_number_of_pages(self):
        number_of_pages = self.cleaned_data.get("number_of_pages")
        if number_of_pages <= 0:
            raise forms.ValidationError("Number of pages must be a positive number.")
        return number_of_pages
