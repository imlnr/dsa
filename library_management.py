class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False
        self.borrower = None

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books[isbn] = new_book

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]

    def checkout_book(self, isbn, borrower):
        if isbn in self.books and not self.books[isbn].checked_out:
            self.books[isbn].checked_out = True
            self.books[isbn].borrower = borrower
            return True
        else:
            return False

    def return_book(self, isbn):
        if isbn in self.books and self.books[isbn].checked_out:
            self.books[isbn].checked_out = False
            self.books[isbn].borrower = None
            return True
        else:
            return False

    def list_books(self):
        for book in self.books.values():
            print(f"{book.title} by {book.author} (ISBN: {book.isbn}) {'(Checked Out)' if book.checked_out else ''}")


if __name__  == '__main__':
    library = Library()

    # Add some books to the library
    library.add_book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "9780590353427")
    library.add_book("To Kill a Mockingbird", "Harper Lee", "9780446310789")

    # List all the books in the library
    library.list_books()

    # Check out a book
    library.checkout_book("9780590353427", "John Smith")

    # List all the books again to see the checked-out status
    library.list_books()

    # Return a book
    library.return_book("9780590353427")

    # List all the books one more time to confirm the book was returned
    library.list_books()
