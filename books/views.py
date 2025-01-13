from django.shortcuts import redirect, render
from django.http import HttpResponse

from books.forms.create import CreateBook
from books.forms.edit import EditBook
from books.models import Book
import os
from django.conf import settings
from django.core.paginator import Paginator

def list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list_book.html', {'books': page_obj})

def detail(request, id):
    try:
        book = Book.objects.get(id=id)
        return render(request, "detail_book.html", {"book": book})
    except Book.DoesNotExist:
        return HttpResponse("Book not found", status=404)
    
def delete(request, id):
    try:
        book = Book.objects.get(id=id)
        if book.cover and book.cover.url != settings.MEDIA_URL + 'covers/default.jpg':
            if os.path.basename(book.cover.name) != 'default.jpg':
                os.remove(os.path.join(settings.MEDIA_ROOT, book.cover.name))
        book.delete()
        return redirect("/books")
    except Book.DoesNotExist:
        return HttpResponse("Book not found", status=404)
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)
    
def create(request):

    form = CreateBook()

    if request.method == "POST":
        form = CreateBook(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/books")

    return render(request, "create_book.html", {"form": form})


def edit(request, id):

    book = Book.objects.get(id=id)

    if book is None:
        return HttpResponse("Book not found")

    form = EditBook(instance=book)

    if request.method == "POST":
        form = EditBook(request.POST, instance=book, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/books")

    return render(request, "edit_book.html", {"form": form})