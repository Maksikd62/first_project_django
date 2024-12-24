from django.urls import path

from books import views

urlpatterns = [
    path("", views.list, name='list'),
    path("detail/<int:id>", views.detail, name='detail'),
    path("delete/<int:id>", views.delete, name='delete'),
    path("create/", views.create, name='create'),
    path("edit/<int:id>", views.edit, name='edit'),
]
