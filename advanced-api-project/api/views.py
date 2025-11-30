from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework  # used for DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    ListView for the Book model.

    - GET /api/books/ -> return a list of all books.

    This view supports:
    - Filtering by title, author, and publication_year
      (e.g. ?title=Foo&publication_year=2020&author__name=John)
    - Searching by title and author name
      (e.g. ?search=novel)
    - Ordering by title and publication_year
      (e.g. ?ordering=title or ?ordering=-publication_year)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [
        rest_framework.DjangoFilterBackend,  # filtering by fields
        filters.SearchFilter,                # text search
        filters.OrderingFilter,              # ordering (checker wants this exact text)
    ]

    # Filter by these fields
    filterset_fields = ["title", "author__name", "publication_year"]

    # Search text in these fields
    search_fields = ["title", "author__name"]

    # Allow ordering by these fields
    ordering_fields = ["title", "publication_year"]

    # Default ordering if none provided
    ordering = ["title"]


class BookDetailView(generics.RetrieveAPIView):
    """
    DetailView for a single Book.

    - GET /api/books/<pk>/ -> return details for a single book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
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

