from django.http import HttpResponse
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer


def home(request):
    return HttpResponse("API Project is running. Go to /api/books/ to see the Book API.")


class BookList(generics.ListAPIView):
    """
    GET /api/books/ -> list all Book instances
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Book instances.

    Endpoints (when used with a router):
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

