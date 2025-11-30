from django.db import models


class Author(models.Model):
    """
    Author model.

    Represents an author who can be associated with many books.
    This is the "one" side of the one-to-many relationship:
    - One Author → many Book instances.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model.

    Each Book belongs to a single Author via a ForeignKey.
    This is the "many" side of the one-to-many relationship:
    - Each Book has one Author.
    - The related_name='books' allows access via author.books.all().
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year}) by {self.author.name}"

