from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Book instances.

    Endpoints:
    - GET    /api/books/        -> list all books
    - POST   /api/books/        -> create a new book
    - GET    /api/books/<id>/   -> retrieve a single book
    - PUT    /api/books/<id>/   -> full update
    - PATCH  /api/books/<id>/   -> partial update
    - DELETE /api/books/<id>/   -> delete a book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

