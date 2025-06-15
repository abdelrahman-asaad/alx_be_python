class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  #private attribtute

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []   #private list to store instances Book class

    def add_book(self, book: Book):   #book is an object from Book class
        self._books.append(book)

    def check_out_book(self, title_of):
        for book in self._books:
            if book.title == title_of and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title_of):
        for book in self._books:
            if book.title == title_of and not book.is_available():
                book.return_book()  #false
                return True
        return False

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")





                 
#Creating object and test:
#library = Library()

#book1 = Book("1984", "George Orwell")  # ← هنا بوضوح بننشئ كائن من كلاس Book

#library.add_book(book1) 

#library.list_available_books()