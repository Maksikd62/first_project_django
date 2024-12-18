from django.urls import path

from books import views

urlpatterns = [
    path("list/", views.list, name='list'),
    path("detail/<int:id>", views.detail, name='detail'),
    path("delete/<int:id>", views.delete, name='delete'),
]
