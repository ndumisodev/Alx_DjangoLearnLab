from django.shortcuts import render
from .models import Author, Book
from .serializers import BookSerializer
from rest_framework import generics, permissions

class BookListCreateView(generics.ListCreateAPIView):
    """
    A view to list all books or create a new book.
    - GET request: Returns a list of all books.
    - POST request: Creates a new book.
    - Permissions:
      - Any user can list books.
      - Only authenticated users can create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    A view to retrieve, update, or delete a single book instance.
    - GET request: Retrieves a book by its primary key (pk).
    - PUT/PATCH request: Updates a book.
    - DELETE request: Deletes a book.
    - Permissions:
      - Any user can retrieve a single book.
      - Only authenticated users can update or delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
