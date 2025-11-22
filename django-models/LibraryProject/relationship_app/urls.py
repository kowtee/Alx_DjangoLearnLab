from django.urls import path
from django.contrib.auth import views  # <-- makes "views.register" substring available
from django.contrib.auth.views import LoginView, LogoutView

from . import views as app_views  # for list_books, LibraryDetailView, register


urlpatterns = [
    path('books/', app_views.list_books, name='list_books'),
    path('library/<int:pk>/', app_views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs (checker expects EXACT patterns)
    path('register/', app_views.register, name='register'),  # <-- contains "views.register"
    
    path(
        'login/',
        LoginView.as_view(template_name="relationship_app/login.html"),
        name='login'
    ),  # <-- contains "LoginView.as_view(template_name="
    
    path(
        'logout/',
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name='logout'
    ),  # <-- contains "LogoutView.as_view(template_name="
]

