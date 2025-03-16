from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    
    def setUp(self):
         # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123') 
        
        # Log the user in
        self.client.login(username='testuser', password='password123')
        # Create a sample book for testing
        self.book = Book.objects.create(title="Test Book", author="John Doe", description="A test book.")
        self.create_url = reverse('book-create')
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.id})
        self.update_url = reverse('book-update', kwargs={'pk': self.book.id})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book.id})

    # Test for listing all books
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    # Test for retrieving a single book
    def test_get_single_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    # Test for creating a book
    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": "Alice Smith",
            "description": "An amazing new book."
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    # Test for updating a book
    def test_update_book(self):
        data = {
            "title": "Updated Book",
            "author": "John Doe",
            "description": "An updated description."
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    # Test for deleting a book
    def test_delete_book(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
