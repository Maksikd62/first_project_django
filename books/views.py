from django.shortcuts import redirect, render
from django.http import HttpResponse

from books.forms.create import CreateBook
from books.forms.edit import EditBook
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
    
def delete(request, id):
    try:
        book = Book.objects.get(id=id)
        book.delete()
        return redirect("/books")
    except Book.DoesNotExist:
        return HttpResponse("Book not found", status=404)
    
def create(request):

    form = CreateBook()

    if request.method == "POST":
        form = CreateBook(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/books")

    return render(request, "create.html", {"form": form})


def edit(request, id):

    book = Book.objects.get(id=id)

    if book is None:
        return HttpResponse("Book not found")

    form = EditBook(instance=book)

    if request.method == "POST":
        form = CreateBook(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect("/books")

    return render(request, "edit.html", {"form": form})