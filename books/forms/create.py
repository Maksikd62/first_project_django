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
        for field in self.fields.values():
            field.required = True  # Робимо всі поля обов'язковими
            field.initial = ""  # Поля будуть пустими за замовчуванням
            
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
