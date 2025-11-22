from django.shortcuts import render
from django.http import HttpResponse

from .models import Library
from .models import Book

from django.views.generic.detail import DetailView
from django.views.generic import ListView


def list_books(request):
    """
    Function-based view:
    Lists all books with their authors.
    """
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    """
    Class-based view:
    Shows one library and all books in it.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

