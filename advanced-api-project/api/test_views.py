from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Author, Book


class BookAPITests(APITestCase):
    """
    Unit tests for the Book API endpoints.

    These tests cover:
    - CRUD operations on Book
    - Filtering, searching, and ordering on the list endpoint
    - Permissions and authentication behavior
    """

    def setUp(self):
        # Create a user for authenticated requests
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123",
        )

        # Create authors
        self.author1 = Author.objects.create(name="Chimamanda Adichie")
        self.author2 = Author.objects.create(name="George Orwell")

        # Create books
        self.book1 = Book.objects.create(
            title="Half of a Yellow Sun",
            publication_year=2006,
            author=self.author1,
        )
        self.book2 = Book.objects.create(
            title="Americanah",
            publication_year=2013,
            author=self.author1,
        )
        self.book3 = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author2,
        )

        # URLs using the names defined in api/urls.py
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book1.pk})
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", kwargs={"pk": self.book1.pk})
        self.delete_url = reverse("book-delete", kwargs={"pk": self.book1.pk})

    # -----------------------------
    # Read-only endpoints (no auth)
    # -----------------------------

    def test_list_books_anonymous_ok(self):
        """
        Anonymous users should be able to list all books (read-only access).
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # We created 3 books in setUp
        self.assertEqual(len(response.data), 3)

    def test_retrieve_book_anonymous_ok(self):
        """
        Anonymous users should be able to retrieve a single book (read-only access).
        """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    # -----------------------------
    # Create / Update / Delete – permissions
    # -----------------------------

    def test_create_book_requires_authentication(self):
        """
        Anonymous users should NOT be able to create a book.
        Expect a 401 or 403 depending on authentication setup.
        """
        data = {
            "title": "New Book",
            "publication_year": 2024,
            "author": self.author1.id,
        }
        response = self.client.post(self.create_url, data, format="json")
        self.assertIn(
            response.status_code,
            (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN),
        )

    def test_authenticated_user_can_create_book(self):
        """
        Authenticated users should be able to create a book successfully.
        """
        self.client.login(username="testuser", password="testpassword123")

        data = {
            "title": "New Auth Book",
            "publication_year": 2024,
            "author": self.author1.id,
        }
        response = self.client.post(self.create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(response.data["title"], "New Auth Book")

    def test_update_book_requires_authentication(self):
        """
        Anonymous users should NOT be able to update a book.
        """
        data = {
            "title": "Updated Title Anonymous",
            "publication_year": self.book1.publication_year,
            "author": self.book1.author.id,
        }
        response = self.client.put(self.update_url, data, format="json")
        self.assertIn(
            response.status_code,
            (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN),
        )

    def test_authenticated_user_can_update_book(self):
        """
        Authenticated users should be able to update a book.
        """
        self.client.login(username="testuser", password="testpassword123")

        data = {
            "title": "Updated Title Authenticated",
            "publication_year": self.book1.publication_year,
            "author": self.book1.author.id,
        }
        response = self.client.put(self.update_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title Authenticated")

    def test_delete_book_requires_authentication(self):
        """
        Anonymous users should NOT be able to delete a book.
        """
        response = self.client.delete(self.delete_url)
        self.assertIn(
            response.status_code,
            (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN),
        )
        self.assertEqual(Book.objects.count(), 3)

    def test_authenticated_user_can_delete_book(self):
        """
        Authenticated users should be able to delete a book.
        """
        self.client.login(username="testuser", password="testpassword123")

        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    # -----------------------------
    # Filtering, searching, ordering
    # -----------------------------

    def test_filter_books_by_title(self):
        """
        The list endpoint should support filtering by title via query params.
        Example: ?title=Americanah
        """
        response = self.client.get(self.list_url, {"title": "Americanah"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Americanah")

    def test_filter_books_by_publication_year(self):
        """
        The list endpoint should support filtering by publication_year.
        Example: ?publication_year=2006
        """
        response = self.client.get(self.list_url, {"publication_year": 2006})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Half of a Yellow Sun")

    def test_search_books_by_title_or_author(self):
        """
        The list endpoint should support text search across title and author name.
        Example: ?search=Chimamanda or ?search=Americanah
        """
        response = self.client.get(self.list_url, {"search": "Chimamanda"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Both books by Chimamanda Adichie should be returned
        self.assertEqual(len(response.data), 2)

        response2 = self.client.get(self.list_url, {"search": "1984"})
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response2.data), 1)
        self.assertEqual(response2.data[0]["title"], "1984")

    def test_order_books_by_publication_year_desc(self):
        """
        The list endpoint should support ordering by publication_year.
        Example: ?ordering=-publication_year
        """
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        years = [item["publication_year"] for item in response.data]
        # Ensure years are sorted in descending order
        self.assertEqual(years, sorted(years, reverse=True))

