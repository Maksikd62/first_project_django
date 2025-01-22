from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'year', 'genre', 'edition', 'number_of_pages') 
    search_fields = ('title', 'author', 'year', 'genre', 'edition')
    list_filter = ('genre',)

admin.site.register(Book, BookAdmin)
