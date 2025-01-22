from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages

from books.forms.create import CreateBook
from books.forms.edit import EditBook
from books.models import Book
import os
from django.conf import settings
from django.core.paginator import Paginator

from books.cart import add_to_cart, clear_cart, get_cart, get_cart_count
# from users.models import User

def list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'books/list.html', {'books': page_obj})

def detail(request, id):
    try:
        book = Book.objects.get(id=id)
        return render(request, "books/detail.html", {"book": book})
    except Book.DoesNotExist:
        return HttpResponse("Book not found", status=404)
    
def delete(request, id):
    try:
        book = Book.objects.get(id=id)
        if book.cover and book.cover.url != settings.MEDIA_URL + 'covers/default.jpg':
            if os.path.basename(book.cover.name) != 'default.jpg':
                os.remove(os.path.join(settings.MEDIA_ROOT, book.cover.name))
            items = get_cart(request.session)
            if str(id) in items:
                del items[str(id)]
                request.session['cart'] = items
            book.delete()
            messages.success(request, "Book deleted successfully!")
            return redirect("/")
            
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
            messages.success(request, "Book created successfully!")

            return redirect("/")
        else:
            messages.error(request, "Invalid data!")

    return render(request, "books/create.html", {"form": form})


def edit(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return HttpResponse("Book not found", status=404)

    old_cover = book.cover.path if book.cover and os.path.basename(book.cover.name) != 'default.jpg' else None

    form = EditBook(instance=book)

    if request.method == "POST":
        form = EditBook(request.POST, instance=book, files=request.FILES)

        if form.is_valid():
            updated_book = form.save(commit=False)

            if 'cover' in request.FILES and old_cover:
                try:
                    os.remove(old_cover)
                except FileNotFoundError:
                    pass

            updated_book.save()
            messages.success(request, "Book edited successfully!")

            return redirect("/")
        else:
            messages.error(request, "Invalid data!")

    return render(request, "books/edit.html", {"form": form})


#cart
def index(request):
    items = get_cart(request.session)
    books = Book.objects.filter(id__in=items.keys())

    # Обчислення загальної ціни
    total_price = sum(book.price * items[str(book.id)] for book in books)
    
    cart_count = get_cart_count(request.session)

    return render(request, "cart/index.html", {"books": books, "total_price": total_price, "cart_count": cart_count})


def add(request, id, quantity = 1):
    cart = get_cart(request.session)
    book=Book.objects.get(id=id)
    if book is None:
        messages.error(request, "Book not found!")
    
    if str(id) in cart:
        messages.warning(request, f"The book '{book.title}' is already in your cart!")

    add_to_cart(request.session, id, quantity)
    messages.success(request, f"Book '{book.title}' added to cart!")
    return redirect("/")

def clear(request):
    clear_cart(request.session)
    messages.success(request, "Cart cleared!")

    return redirect("/")

def delete_cart(request, id):
    items = get_cart(request.session)
    if str(id) in items:
        del items[str(id)]
        request.session['cart'] = items
        messages.success(request, "Book deleted from cart!")
    else:
        messages.error(request, "Book not found in cart!")
    return redirect("/cart")