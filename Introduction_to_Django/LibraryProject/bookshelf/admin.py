from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ['title', 'author', 'publication_year']
    
    # Enable filtering by publication year and author
    list_filter = ['publication_year', 'author']
    
    # Enable search functionality
    search_fields = ['title', 'author']
    
    # Fields to display in the detail/edit form
    fields = ['title', 'author', 'publication_year']
    
    # Optional: Add ordering
    ordering = ['title']  # Books will be ordered by title by default