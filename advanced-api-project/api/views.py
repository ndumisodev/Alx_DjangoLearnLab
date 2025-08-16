from django.shortcuts import render
from .models import Author, Book
from .serializers import BookSerializer
from rest_framework import generics, permissions

class BookListView(generics.ListAPIView):
    """
    A view to list all books.
    - GET request: Returns a list of all books.
    - Permissions: Any user can list books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    A view to create a new book.
    - POST request: Creates a new book.
    - Permissions: Only authenticated users can create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookDetailView(generics.RetrieveAPIView):
    """
    A view to retrieve a single book by its ID.
    - GET request: Retrieves a book by its primary key (pk).
    - Permissions: Any user can retrieve a single book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookUpdateView(generics.UpdateAPIView):
    """
    A view to update an existing book.
    - PUT/PATCH request: Updates a book by its primary key (pk).
    - Permissions: Only authenticated users can update a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    A view to delete a book.
    - DELETE request: Deletes a book by its primary key (pk).
    - Permissions: Only authenticated users can delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]