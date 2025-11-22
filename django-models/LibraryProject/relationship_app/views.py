from django.shortcuts import render
from django.http import HttpResponse
from LibraryProject.relationship_app.models import Book, Library
from django.views.generic import DetailView

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
    Display details for a specific library, including all books.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

