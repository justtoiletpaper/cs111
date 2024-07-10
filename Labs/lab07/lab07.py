class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.times_read = 0

    def __repr__(self):
        return f"Book({self.id}, '{self.title}', '{self.author}')"

    def __str__(self):
        return f"{self.title} by {self.author}"


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
        self.book_tuple = args
        self.books = {}
        for item in self.book_tuple:
            self.books[item.id] = item




    def read_book(self, id):
        """Takes in an id of the book read, and
        returns that book's title and the number
        of times it has been read."""
        if id in self.books:
            current_book = self.books[id]
            current_book.times_read += 1
            # print(current_book.title + " has been read " + str(current_book.times_read) + " time(s)")
            return f"{current_book.title} has been read " + str(current_book.times_read) + " time(s)"
        else:
            print("No book with this id")

    def read_author(self, author):
        """Takes in the name of an author, and
        returns the total output of reading every
        book written by that author in a single string.
        Hint: Each book output should be on a different line."""
        output_txt = []
        for i in self.books:
            if self.books[i].author == author:
                self.books[i].times_read += 1
                # print(self.books[i].title + " has been read " + str(self.books[i].times_read) + " time(s)")
                line_read = f"{self.books[i].title} has been read " + str(self.books[i].times_read) + " time(s)"
                output_txt.append(line_read)
        if len(output_txt) > 1:
            output = "\n".join(output_txt)
            return output
        else:
            return output_txt[0]



    def add_book(self, book):
        """Takes in a book object and adds it to the books
        dictionary if the book id is not already taken."""
        taken = 0
        for key in self.books:
            if key == book.id:
                taken += 1
        if taken == 0:
            self.books[book.id] = book

        # if id in self.books == book.id:
        #     self.books[book.id] = book
        # else:
        #     print("Book id is already taken")

    def __repr__(self):
        output_lst = []
        for book in self.book_tuple:
            output_lst.append(repr(book))
        output = ", ".join(output_lst)
        return f"Library({output})"


    def __str__(self):
        output_lst = []
        for key in self.books:
            output_lst.append(str(self.books[key]))
        output = ' | '.join(output_lst)
        return output


b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
b3 = Book(2, "The Fellowship of the Ring", "J.R.R. Tolkien")
l = Library(b1, b2)
