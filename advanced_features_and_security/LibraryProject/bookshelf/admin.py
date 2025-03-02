from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book, CustomUser 


# Custom admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the list view
    list_filter = ('publication_year',)  # Add filters for publication_year
    search_fields = ('title', 'author')  # Add search capabilities for title and author

    def create_groups_and_permissions():
    # Get the content type for Book model
     book_content_type = ContentType.objects.get_for_model(Book)

    # Define permissions
    permissions = {
        "can_view": Permission.objects.get(codename="can_view", content_type=book_content_type), # type: ignore
        "can_create": Permission.objects.get(codename="can_create", content_type=book_content_type), # type: ignore
        "can_edit": Permission.objects.get(codename="can_edit", content_type=book_content_type), # type: ignore
        "can_delete": Permission.objects.get(codename="can_delete", content_type=book_content_type), # type: ignore
    }

    # Define groups
    groups = {
        "Viewers": ["can_view"],
        "Editors": ["can_view", "can_create", "can_edit"],
        "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
    }

    # Create groups and assign permissions
    for group_name, perms in groups.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for perm in perms:
            group.permissions.add(permissions[perm])



# Register the Book model
admin.site.register(Book,BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin) # type: ignore


