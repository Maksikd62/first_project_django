from django.shortcuts import render
from django.http import HttpResponse

from books.models import Book

def list(request):
    books = Book.objects.all()
    return render(request, "list.html", {"books": books})

def detail(request, id):
    try:
        book = Book.objects.get(id=id)
        return render(request, "detail.html", {"book": book})
    except Book.DoesNotExist:
        return HttpResponse("Book not found", status=404)
