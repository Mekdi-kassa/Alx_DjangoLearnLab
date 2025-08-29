from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book deleted successfully")

# Confirm deletion
remaining_books = Book.objects.all()
print(f"Books remaining in database: {list(remaining_books)}")