from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)


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