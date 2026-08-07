        
class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        """Displays individual book details."""
        print(f"Title:  {self.title}")
        print(f"Author: {self.author}")
        print(f"Price:  ₹{self.price:.2f}")
        print("-" * 30)


class LibraryManagementSystem:

    def __init__(self):
        self.books = []

    def add_book(self, title, author, price):
        """Creates a new Book instance and adds it to the library collection."""
        new_book = Book(title, author, price)
        self.books.append(new_book)
        print(f"Successfully added '{title}' to the library.\n")

    def display_details(self):
        """Displays details of all books in the system."""
        if not self.books:
            print("No books available in the library.")
            return

        print("\n--- 📚 Library Book List ---")
        for index, book in enumerate(self.books, start=1):
            print(f"Book #{index}")
            book.display_details()


# Test Run
if __name__ == "__main__":
    # Create library object
    library = LibraryManagementSystem()

    # Add books
    library.add_book("The Guide", "R.K. Narayan", 299.00)
    library.add_book("Wings of Fire", "A.P.J. Abdul Kalam", 350.50)

    # Display all book details
    library.display_details()