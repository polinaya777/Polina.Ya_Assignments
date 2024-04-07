from bookshelf import Book, Room

def main():
    # Sample books
    books = {
        Book("The Pragmatic Programmer", "Andy Hunt and Dave Thomas", "Programming"),
        Book("Clean Code", "Robert C. Martin", "Programming"),
        Book("The Hunger Games", "Suzanne Collins", "Fiction"),
        Book("1984", "George Orwell", "Fiction"),
        Book("A Brief History of Time", "Stephen Hawking", "Science")
    }

    # Initialize John's room and organize books
    john_room = Room()
    john_room.organize_books(books)
    john_room.sort_shelves()

    # Print the organized shelves
    print(john_room)

if __name__ == "__main__":
    main()
