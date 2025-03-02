from django.contrib import admin
from .models import Book, CustomUser 


# Custom admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the list view
    list_filter = ('publication_year',)  # Add filters for publication_year
    search_fields = ('title', 'author')  # Add search capabilities for title and author


# Register the Book model
admin.site.register(Book,BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin) # type: ignore


