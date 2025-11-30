from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


class BookListCreateView(generics.ListCreateAPIView):
    """
    List + Create view for Book model.

    - GET  /api/books/      -> return a list of all books
    - POST /api/books/      -> create a new Book instance

    Permissions:
    - Unauthenticated users: can only READ (GET).
    - Authenticated users: can READ and CREATE.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # IsAuthenticatedOrReadOnly:
    # - SAFE methods (GET, HEAD, OPTIONS) allowed for everyone
    # - write methods (POST) allowed only for authenticated users
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Custom hook called when a new Book is created.

        Here we just call save(), but this is where you could
        attach additional logic (e.g., set the creator, log, etc.).
        """
        serializer.save()


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail view for a single Book instance.

    - GET    /api/books/<pk>/   -> retrieve details of a single book
    - PUT    /api/books/<pk>/   -> full update
    - PATCH  /api/books/<pk>/   -> partial update
    - DELETE /api/books/<pk>/   -> delete the book

    Permissions:
    - Unauthenticated users: can only READ (GET).
    - Authenticated users: can READ, UPDATE, and DELETE.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        """
        Custom hook called when an existing Book is updated.

        You can extend this to add logging, extra validation hooks, etc.
        """
        serializer.save()

