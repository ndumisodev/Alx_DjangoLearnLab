from django.db import models


class Author(models.Model):
    """
    Represents an author with their name.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book with its title, publication year,
    and a foreign key linking it to its Author.
    This creates a one-to-many relationship where one Author
    can have many Books.
    """
    title = models.CharField(max_length=225)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
