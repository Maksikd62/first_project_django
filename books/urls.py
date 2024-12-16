from django.urls import path

from books import views

urlpatterns = [
    path("list/", views.list),
    path("detail/<int:id>", views.detail),
]