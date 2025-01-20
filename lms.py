import json

# Library class to manage the books
class Library:
    def __init__(self, filename="books.json"):
        self.filename = filename
        self.load_books()

    def load_books(self):
        """Load books from a JSON file."""
        try:
            with open(self.filename, "r") as f:
                self.books = json.load(f)
        except FileNotFoundError:
            self.books = []

    def save_books(self):
        """Save books to a JSON file."""
        with open(self.filename, "w") as f:
            json.dump(self.books, f, indent=4)

    def add_book(self, title, author, year):
        """Add a new book to the library."""
        book = {
            "title": title,
            "author": author,
            "year": year
        }
        self.books.append(book)
        self.save_books()
        print(f"Book '{title}' added successfully!")

    def list_books(self):
        """List all books in the library."""
        if not self.books:
            print("No books found in the library.")
        else:
            print("\nBooks in Library:")
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book['title']} by {book['author']} ({book['year']})")

    def search_books(self, query):
        """Search for books by title or author."""
        result = [book for book in self.books if query.lower() in book["title"].lower() or query.lower() in book["author"].lower()]
        if result:
            print("\nSearch Results:")
            for book in result:
                print(f"{book['title']} by {book['author']} ({book['year']})")
        else:
            print("No matching books found.")

    def remove_book(self, title):
        """Remove a book by its title."""
        self.books = [book for book in self.books if book['title'].lower() != title.lower()]
        self.save_books()
        print(f"Book '{title}' removed successfully!")

# Main function to interact with the system
def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Search Books")
        print("4. Remove Book")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter publication year: ")
            library.add_book(title, author, year)
        
        elif choice == "2":
            library.list_books()

        elif choice == "3":
            query = input("Enter title or author to search: ")
            library.search_books(query)

        elif choice == "4":
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)

        elif choice == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
