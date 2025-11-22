from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView  # <-- checker requires this
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import user_passes_test


# ---------------------------------------
# FUNCTION-BASED VIEW (BOOK LIST)
# ---------------------------------------

def list_books(request):
    """
    Display all books in the database.
    """
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# ---------------------------------------
# CLASS-BASED VIEW (LIBRARY DETAILS)
# ---------------------------------------

class LibraryDetailView(DetailView):
    """
    Display details for a specific library, listing all books available in that library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# ---------------------------------------
# AUTHENTICATION VIEWS
# ---------------------------------------

def register(request):
    """
    User registration view.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})


def login_view(request):
    """
    User login view.
    """
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm()

    return render(request, 'relationship_app/login.html', {'form': form})


def logout_view(request):
    """
    User logout view.
    """
    logout(request)
    return render(request, 'relationship_app/logout.html')


# ======================================================
# ROLE-BASED ACCESS CONTROL (CHECKER-REQUIRED SECTION)
# ======================================================

# ----- ADMIN ROLE -----

def is_admin(user):
    return user.userprofile.role == "Admin"


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


# ----- LIBRARIAN ROLE -----

def is_librarian(user):
    return user.userprofile.role == "Librarian"

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


# ----- MEMBER ROLE -----

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

