class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

    def __repr__(self):
        return f"{self.title} by {self.author}, Category: {self.category}"
    
class Shelf:
    def __init__(self):
        self.books = []
        self.categories = set()

    def add_book(self, book):
        if book.category not in self.categories:
            self.categories.add(book.category)
        self.books.append(book)

    def sort_books(self):
        self.books.sort(key=lambda book: book.title)

class Room:
    def __init__(self):
        self.shelves = []

    def organize_books(self, books):
        for book in books:
            placed = False
            for shelf in self.shelves:
                if book.category in shelf.categories:
                    shelf.add_book(book)
                    placed = True
                    break
            if not placed:
                new_shelf = Shelf()
                new_shelf.add_book(book)
                self.shelves.append(new_shelf)

    def sort_shelves(self):
        for shelf in self.shelves:
            shelf.sort_books()

    def __repr__(self):
        representation = ""
        for i, shelf in enumerate(self.shelves, start=1):
            representation += f"Shelf {i}:\n"
            for book in shelf.books:
                representation += f"  {book}\n"
        return representation