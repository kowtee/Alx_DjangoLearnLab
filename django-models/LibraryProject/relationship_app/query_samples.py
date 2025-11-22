import os
import sys
import django

# -----------------------------------
# Make sure Python can find the project folder
# -----------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Tell Django where settings.py is located
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    print(f"Books by {author.name}:")
    for book in books:
        print("-", book.title)

def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in {library.name}:")
    for book in books:
        print("-", book.title)

def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"Librarian for {library.name}: {librarian.name}")

if __name__ == "__main__":
    books_by_author("John Doe")
    books_in_library("Main Library")
    librarian_for_library("Main Library")

