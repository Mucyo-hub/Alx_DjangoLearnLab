# Create Operation

## Command
```python
from bookshelf.models import Book

book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Retrieve Operation

## Command
```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

# Update Operation

## Command
```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Delete Operation

## Command
```python
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

books = Book.objects.all()
print(books)