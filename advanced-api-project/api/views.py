from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    ListView for the Book model.

    - GET /api/books/ -> return a list of all books.
    - Read-only endpoint, available to everyone (but protected by DRF permissions).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Unauthenticated users: read-only; authenticated users: same.
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookDetailView(generics.RetrieveAPIView):
    """
    DetailView for a single Book.

    - GET /api/books/<pk>/ -> return details for a single book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Same: read-only for everyone.
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    CreateView for the Book model.

    - POST /api/books/create/ -> create a new Book instance.

    Permissions:
    - Only authenticated users can create books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Hook to customize creation logic.
        """
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    UpdateView for the Book model.

    - PUT/PATCH /api/books/update/<pk>/ -> update an existing Book.

    Permissions:
    - Only authenticated users can update books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        """
        Hook to customize update logic.
        """
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    DeleteView for the Book model.

    - DELETE /api/books/delete/<pk>/ -> delete an existing Book.

    Permissions:
    - Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

