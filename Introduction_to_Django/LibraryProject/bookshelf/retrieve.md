**Retrieve Operation**

**Python Command:**
```python
from bookshelf.models import Book
retrieved_book = Book.objects.get(title="1984")
print(f"Title: {retrieved_book.title}, Author: {retrieved_book.author}, Publication Year: {retrieved_book.publication_year}")