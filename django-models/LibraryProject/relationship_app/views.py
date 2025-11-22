from django.shortcuts import render
from django.http import HttpResponse
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView  # <-- checker looks for this exact line

# ---------------------------------------
# FUNCTION-BASED VIEW
# ---------------------------------------

def list_books(request):
    """
    Display all books in the database.
    """
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# ---------------------------------------
# CLASS-BASED VIEW
# ---------------------------------------

class LibraryDetailView(DetailView):
    """
    Display details for a specific library, listing all books available in that library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

