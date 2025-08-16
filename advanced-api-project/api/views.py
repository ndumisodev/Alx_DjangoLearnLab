from django.shortcuts import render
from .models import Author, Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as django_filters

class BookListView(generics.ListAPIView):
    """
    A view to list all books with filtering, searching, and ordering capabilities.
    - GET request: Returns a list of all books.
    - Permissions: Any user can list books.
    - Filtering: Supports filtering by 'title', 'author', and 'publication_year'
      using query parameters.
    - Searching: Supports searching by 'title' and 'author' name using
      the '?search=' query parameter.
    - Ordering: Supports ordering by 'title' and 'publication_year' using
      the '?ordering=' query parameter.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']



class BookCreateView(generics.CreateAPIView):
    """
    A view to create a new book.
    - POST request: Creates a new book.
    - Permissions: Only authenticated users can create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDetailView(generics.RetrieveAPIView):
    """
    A view to retrieve a single book by its ID.
    - GET request: Retrieves a book by its primary key (pk).
    - Permissions: Any user can retrieve a single book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookUpdateView(generics.UpdateAPIView):
    """
    A view to update an existing book.
    - PUT/PATCH request: Updates a book by its primary key (pk).
    - Permissions: Only authenticated users can update a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    A view to delete a book.
    - DELETE request: Deletes a book by its primary key (pk).
    - Permissions: Only authenticated users can delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]