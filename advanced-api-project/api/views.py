from django.shortcuts import render
from django_filters import rest_framework
from rest_framework import generics, filters

from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView (generics.ListAPIView):
  """
    API view to retrieve the list of books with filtering, searching, and ordering capabilities.

    Filtering:
    - Filter by title, author name, and publication year.
    - Usage example: /api/books/?title=Harry

    Searching:
    - Search within the title and author name.
    - Usage example: /api/books/?search=Rowling

    Ordering:
    - Order results by title or publication year (ascending or descending).
    - Usage example: /api/books/?ordering=-publication_year
    """
  queryset =Book.objects.all()
  serializer_class = BookSerializer
  filter_backends =[DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]
  filterset_fields = ['title','author__name' 'publication_year']
  search_fields = ['title','author__name']
  ordering_fields = ['title','publication_year']


