from relationship_app.models import *

def get_books_by_author(author_name) :
    """Query all books by specific author"""
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return f"No author found with name: {author_name}"
    

def get_books_in_library(library_name) :
    """List all the books in a library"""
    try :
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Librarian.DoesNotExist :
        return  f"No library found with name: {library_name}"


def get_librarian_for_library(library_name):
    """Retrieve the librarian for a library"""
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except Library.DoesNotExist:
        return f"No library found with name: {library_name}"
    except Librarian.DoesNotExist:
        return f"No librarian assigned to library: {library_name}"