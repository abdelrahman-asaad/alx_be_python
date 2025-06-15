book_shelf = { "1984": "George Orwell", "Brave New World": "Aldous Huxley"}

class Book:
    def __init__(self):
        self._is_checked_out = False

    def check_out(self, title):
        title = title.strip()
        if title in book_shelf:
            return f"{title} is available"
        else:
            return self._is_checked_out

class Library(Book):
    def __init__(self):
        super().__init__()
        self._books = book_shelf

    def add_book(self, title, author):
        book_shelf[title] = author
        return f"Added {title} by {author}"
    
    def check_out_book(self, title):
        for key in book_shelf:
            if key == title:
                return f"Yes, '{title}' exists"
        return False
    
    def return_book(self, title):
        if title in book_shelf:
            del book_shelf[title]
            return f"'{title}' is returned and removed"
        else:
            return f"'{title}' not found"

    def list_available_books(self):
        return f"Available Books: {list(book_shelf)}"

# تجربة
book_1 = Library()
print(book_1.add_book("Blue", "Mourad"))
print(book_shelf)
print(book_1.check_out_book("Blue"))
print(book_1.list_available_books())
print(book_1.return_book("Blue"))
print(book_1.list_available_books())
print(book_1.check_out_book("Blue"))
