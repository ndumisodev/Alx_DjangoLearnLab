from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone


class BookSerializer(serializers.ModelSerializer):
    """
    A serializer for the Book model.
    Includes custom validation to ensure the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
        read_only_fields = ['author']

    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    

class AuthorSerializer(serializers.ModelSerializer):
    """
    A serializer for the Author model.
    It includes a nested serializer for the related 'books',
    allowing the author's name and all their books to be
    serialized together. The 'books' field is read-only
    because it's populated from the reverse foreign key
    relationship.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']