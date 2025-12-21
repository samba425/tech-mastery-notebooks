"""
Demo Project 8: Library Management System
Part 2: Backend Development - Hour 12
Difficulty: ⭐⭐⭐ Advanced

Features:
- Book management with borrow/return system
- Search functionality
- Inventory tracking
- OOP with inheritance
"""

class Book:
    """Base Book class"""
    
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.available = True
        self.borrower = None
    
    def borrow(self, borrower_name):
        """Borrow the book"""
        if self.available:
            self.available = False
            self.borrower = borrower_name
            print(f"✅ '{self.title}' borrowed by {borrower_name}")
            return True
        else:
            print(f"❌ '{self.title}' is already borrowed by {self.borrower}")
            return False
    
    def return_book(self):
        """Return the book"""
        if not self.available:
            borrower = self.borrower
            self.available = True
            self.borrower = None
            print(f"✅ '{self.title}' returned by {borrower}")
            return True
        else:
            print(f"❌ '{self.title}' is already available")
            return False
    
    def __str__(self):
        status = "Available" if self.available else f"Borrowed by {self.borrower}"
        return f"{self.title} by {self.author} ({self.year}) - {status}"


class FictionBook(Book):
    """Fiction book subclass"""
    
    def __init__(self, isbn, title, author, year, genre):
        super().__init__(isbn, title, author, year)
        self.genre = genre
    
    def __str__(self):
        return f"[Fiction - {self.genre}] {super().__str__()}"


class NonFictionBook(Book):
    """Non-fiction book subclass"""
    
    def __init__(self, isbn, title, author, year, subject):
        super().__init__(isbn, title, author, year)
        self.subject = subject
    
    def __str__(self):
        return f"[Non-Fiction - {self.subject}] {super().__str__()}"


class Library:
    """Library management system"""
    
    def __init__(self):
        self.books = {}
    
    def add_book(self, book):
        """Add a book to library"""
        self.books[book.isbn] = book
        print(f"✅ Book added: {book.title}")
    
    def search_by_title(self, keyword):
        """Search books by title"""
        results = [b for b in self.books.values() if keyword.lower() in b.title.lower()]
        return results
    
    def search_by_author(self, keyword):
        """Search books by author"""
        results = [b for b in self.books.values() if keyword.lower() in b.author.lower()]
        return results
    
    def list_available_books(self):
        """List all available books"""
        available = [b for b in self.books.values() if b.available]
        return available
    
    def list_borrowed_books(self):
        """List all borrowed books"""
        borrowed = [b for b in self.books.values() if not b.available]
        return borrowed
    
    def get_statistics(self):
        """Get library statistics"""
        total = len(self.books)
        available = len(self.list_available_books())
        borrowed = len(self.list_borrowed_books())
        
        return {
            'total': total,
            'available': available,
            'borrowed': borrowed
        }


def main():
    """Demo the library system"""
    library = Library()
    
    # Add books
    book1 = FictionBook("978-123", "The Python Adventure", "Alice Dev", 2023, "Sci-Fi")
    book2 = NonFictionBook("978-456", "Python Programming Guide", "Bob Tech", 2023, "Programming")
    book3 = FictionBook("978-789", "Code Chronicles", "Charlie Code", 2022, "Mystery")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    # List all books
    print("\n📚 All Books:")
    for book in library.books.values():
        print(f"  - {book}")
    
    # Borrow books
    print("\n📖 Borrowing Books:")
    book1.borrow("John Doe")
    book2.borrow("Jane Smith")
    
    # List available books
    print("\n✅ Available Books:")
    for book in library.list_available_books():
        print(f"  - {book.title}")
    
    # Search functionality
    print("\n🔍 Search Results (Python):")
    results = library.search_by_title("Python")
    for book in results:
        print(f"  - {book}")
    
    # Statistics
    stats = library.get_statistics()
    print(f"\n📊 Library Statistics:")
    print(f"  Total Books: {stats['total']}")
    print(f"  Available: {stats['available']}")
    print(f"  Borrowed: {stats['borrowed']}")
    
    # Return a book
    print("\n📥 Returning Book:")
    book1.return_book()


if __name__ == "__main__":
    main()


