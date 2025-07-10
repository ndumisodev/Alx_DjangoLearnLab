from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    # Customize the list view to display specific fields
    list_display = ('title', 'author', 'publication_year')

    # Add filters to the sidebar
    list_filter = ('publication_year', 'author')

    # Enable search functionality
    search_fields = ('title', 'author')

# Register your Book model with the custom BookAdmin
admin.site.register(Book, BookAdmin)