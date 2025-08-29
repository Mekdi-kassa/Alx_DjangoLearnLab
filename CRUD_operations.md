
## 6. Complete CRUD_operations.md

```markdown
# CRUD Operations for Book Model

## Create Operation
```python


>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> print(f"Created book: {book}")
Created book: 1984 by George Orwell (1949)
>>> book = Book.objects.get(title = "1984")
>>> print(f"Title: {book.title}")
Title: 1984
>>> print(f"Author: {book.author}")
Author: George Orwell
>>> print(f"Publication Year: {book.publication_year}")
Publication Year: 1949
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> print(f"Updated title to: {book.title}")
Updated title to:Nineteen Eighty-Four
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()
>>> print("Book deleted successfully")
Book deleted successfully
# Confirm deletion
>>> remaining_books = Book.objects.all()
>>> print(f"Books remaining in database: {list(remaining_books)}")
Books remaining in database: []