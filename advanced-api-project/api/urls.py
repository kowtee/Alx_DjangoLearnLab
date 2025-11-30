from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    # /api/books/  -> list all books (GET), create new book (POST)
    path("books/", BookListCreateView.as_view(), name="book-list-create"),

    # /api/books/<pk>/  -> retrieve, update, delete a single book
    path("books/<int:pk>/", BookRetrieveUpdateDestroyView.as_view(), name="book-detail"),
]

