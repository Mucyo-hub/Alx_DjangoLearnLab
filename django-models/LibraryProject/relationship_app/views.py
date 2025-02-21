from django.shortcuts import render
from .models import Book 

def list_books(request): # retrieve all Books from database 
  books = Book.objects.all()
  return render(request,'relationship_app/list_books.html',{'books': books})


from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library  # Specify the model to use
    template_name = 'relationship_app/library_detail.html'  # Specify the template
    context_object_name = 'library'  # Name of the context variable in the template