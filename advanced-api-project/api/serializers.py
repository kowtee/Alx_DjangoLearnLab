from datetime import datetime

from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    - Serializes all fields of the Book model.
    - Adds custom validation for publication_year to ensure it is not in the future.
    """

    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, value):
        """
        Ensure publication_year is not greater than the current year.

        This prevents creating or updating books that are set in the future.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                f"publication_year cannot be in the future (got {value}, current year is {current_year})."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    - Includes the author's name.
    - Includes a nested list of books using BookSerializer.
      The `books` field uses the related_name='books' on the Book.author ForeignKey,
      so it automatically pulls all Book instances for a given Author.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]

