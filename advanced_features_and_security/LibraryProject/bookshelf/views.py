from django.shortcuts import render , get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required , permission_required
from .models import Book
from django.db.models import Q
from .forms import BookForm # type: ignore
from .forms import ExampleForm


# View all books (Requires "can_view" permission)
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Create a new book (Requires "can_create" permission)
@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        publication_year = request.POST.get("publication_year")
        Book.objects.create(title=title, author=author, publication_year=publication_year)
    return render(request, 'bookshelf/create_book.html')

# Edit a book (Requires "can_edit" permission)
@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.publication_year = request.POST.get("publication_year")
        book.save()
    return render(request, 'bookshelf/edit_book.html', {'book': book})

# Delete a book (Requires "can_delete" permission)
@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
    return render(request, 'bookshelf/delete_book.html', {'book': book})


