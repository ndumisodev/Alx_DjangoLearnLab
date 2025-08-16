# api/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Author, Book


class BookAPITests(APITestCase):
    """
    Comprehensive tests for the Book API endpoints.
    """
    def setUp(self):
        """
        Set up the test environment.
        - Create a sample user for authenticated requests.
        - Create a sample author.
        - Create multiple sample books for testing list, filter, search, and ordering.
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(name='J.R.R. Tolkien')
        self.book1 = Book.objects.create(
            title='The Fellowship of the Ring',
            publication_year=1954,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title='The Two Towers',
            publication_year=1954,
            author=self.author
        )
        self.book3 = Book.objects.create(
            title='The Return of the King',
            publication_year=1955,
            author=self.author
        )

        # URLs for testing
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        self.update_url = reverse('book-update', kwargs={'pk': self.book1.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book1.pk})

    # --- Test CRUD Operations ---

    def test_list_books(self):
        """
        Ensure we can retrieve a list of books.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_create_book_authenticated(self):
        """
        Ensure an authenticated user can create a new book.
        """
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'The Hobbit', 'publication_year': 1937, 'author': self.author.pk}
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(Book.objects.get(title='The Hobbit').publication_year, 1937)

    def test_create_book_unauthenticated(self):
        """
        Ensure an unauthenticated user cannot create a new book.
        """
        data = {'title': 'The Hobbit', 'publication_year': 1937, 'author': self.author.pk}
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 3)

    def test_retrieve_book(self):
        """
        Ensure we can retrieve a single book.
        """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'The Fellowship of the Ring')

    def test_update_book_authenticated(self):
        """
        Ensure an authenticated user can update a book.
        """
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'The Fellowship of the Ring (Revised)', 'publication_year': 1965, 'author': self.author.pk}
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'The Fellowship of the Ring (Revised)')
        self.assertEqual(self.book1.publication_year, 1965)

    def test_update_book_unauthenticated(self):
        """
        Ensure an unauthenticated user cannot update a book.
        """
        data = {'title': 'Updated Title', 'publication_year': 2000, 'author': self.author.pk}
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.book1.refresh_from_db()
        self.assertNotEqual(self.book1.title, 'Updated Title')

    def test_delete_book_authenticated(self):
        """
        Ensure an authenticated user can delete a book.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())

    def test_delete_book_unauthenticated(self):
        """
        Ensure an unauthenticated user cannot delete a book.
        """
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertTrue(Book.objects.filter(pk=self.book1.pk).exists())

    # --- Test Filtering, Searching, and Ordering ---

    def test_filter_by_title(self):
        """
        Ensure filtering by title works correctly.
        """
        response = self.client.get(self.list_url, {'title': 'The Two Towers'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Two Towers')

    def test_filter_by_publication_year(self):
        """
        Ensure filtering by publication year works correctly.
        """
        response = self.client.get(self.list_url, {'publication_year': 1954})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_by_title(self):
        """
        Ensure searching by title works correctly.
        """
        response = self.client.get(self.list_url, {'search': 'Ring'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Fellowship of the Ring')

    def test_search_by_author_name(self):
        """
        Ensure searching by author name works correctly.
        """
        response = self.client.get(self.list_url, {'search': 'Tolkien'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_ordering_by_title_descending(self):
        """
        Ensure ordering by title in descending order works.
        """
        response = self.client.get(self.list_url, {'ordering': '-title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'The Two Towers')
        self.assertEqual(response.data[2]['title'], 'The Fellowship of the Ring')

    def test_ordering_by_publication_year(self):
        """
        Ensure ordering by publication year works.
        """
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1954)
        self.assertEqual(response.data[2]['publication_year'], 1955)