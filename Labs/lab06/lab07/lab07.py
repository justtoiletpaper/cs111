class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.times_read = 0


class Library:
    """A Library takes in an arbitrary amount of books, and has a
    dictionary of id numbers as keys, and Books as values.
    >>> b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
    >>> b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
    >>> b3 = Book(2, "The Fellowship of the Ring", "J.R.R. Tolkien")
    >>> l = Library(b1, b2, b3)
    >>> l.books[0].title
    'A Tale of Two Cities'
    >>> l.books[0].author
    'Charles Dickens'
    >>> l.read_book(1)
    'The Hobbit has been read 1 time(s)'
    >>> l.read_book(3) # No book with this id
    ''
    >>> l.read_author("Charles Dickens")
    'A Tale of Two Cities has been read 1 time(s)'
    >>> l.read_author("J.R.R. Tolkien")
    'The Hobbit has been read 2 time(s)'
    'The Fellowship of the Ring has been read 1 time(s)'
    >>> b1.times_read
    1
    >>> b2.times_read
    2
    """

    def __init__(self, *args):
        """Takes in an arbitrary number of book objects and 
        puts them in a books dictionary which takes the book 
        id as the key and the book object as the value"""
        ___________
        for _____ in ______:
            _______________

    def read_book(self, id):
        """Takes in an id of the book read, and
        returns that book's title and the number
        of times it has been read."""
        if ___ in ___________:
            __________________
            __________________
            __________________________________

    def read_author(self, author):
        """Takes in the name of an author, and
        returns the total output of reading every
        book written by that author in a single string.
        Hint: Each book output should be on a different line."""
        ______________
        for _______________:
            if __________________:
                _______________________________
        ______________

    def add_book(self, book):
        """Takes in a book object and adds it to the books
        dictionary if the book id is not already taken."""
        if ______________:
            ______
        else:
            _____________
