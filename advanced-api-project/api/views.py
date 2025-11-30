from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    ListView for the Book model.

    - GET /api/books/ -> return a list of all books.
    - Read-only endpoint, available to everyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Allow anyone to read the list.
    permission_classes = [permissions.AllowAny]


class BookDetailView(generics.RetrieveAPIView):
    """
    DetailView for a single Book.

    - GET /api/books/<pk>/ -> return details for a single book.
    - Read-only endpoint, available to everyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    CreateView for the Book model.

    - POST /api/books/create/ -> create a new Book instance.

    Permissions:
    - Only authenticated users can create books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Hook to customize creation logic.

        You could, for example, attach the request.user here.
        """
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    UpdateView for the Book model.

    - PUT/PATCH /api/books/<pk>/update/ -> update an existing Book.

    Permissions:
    - Only authenticated users can update books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Hook to customize update logic.

        Called whenever a Book instance is updated.
        """
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    DeleteView for the Book model.

    - DELETE /api/books/<pk>/delete/ -> delete an existing Book.

    Permissions:
    - Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

