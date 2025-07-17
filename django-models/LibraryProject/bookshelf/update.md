**Update Operation**

**Python Command:**
```python


book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)













# from bookshelf.models import Book
# book_to_update = Book.objects.get(title="1984")
# book_to_update.title = "Nineteen Eighty-Four"
# book_to_update.save()
# print(book_to_update.title)