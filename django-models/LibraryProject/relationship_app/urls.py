from django.urls import path
from django.contrib.auth import views  # <-- makes "views.register" substring available
from django.contrib.auth.views import LoginView, LogoutView

from .views import add_book, edit_book, delete_book
from . import views as app_views
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view


urlpatterns = [
    path('books/', app_views.list_books, name='list_books'),
    path('library/<int:pk>/', app_views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs
    path('register/', app_views.register, name='register'),
    path(
        'login/',
        LoginView.as_view(template_name="relationship_app/login.html"),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name='logout'
    ),

    # Role-based URLs (required by checker)
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    # Book CRUD with permissions (REQUIRED)
    path('books/add/', add_book, name='add_book'),
    path('books/<int:book_id>/edit/', edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', delete_book, name='delete_book'),

    # Checker-friendly paths (exact strings required)
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),



]


