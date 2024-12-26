from django.urls import path

from books import views

urlpatterns = [
    path("", views.list, name='list_books'),
    path("detail/<int:id>", views.detail, name='detail_book'),
    path("delete/<int:id>", views.delete, name='delete_book'),
    path("create/", views.create, name='create_book'),
    path("edit/<int:id>", views.edit, name='edit_book'),
]
