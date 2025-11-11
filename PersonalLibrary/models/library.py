#class which cretes the books using the book class then stores them in a dict

class Library():
    def __init__(self):
        """Makes a book list to store all the book info, for books in library and borrowed books"""
        self.borrowed = {} #creates an empty dict to store borrowed books
        self.user_books = {} #creates an empty dict to store user's books

    # this method adds new books to the dict, it cretes a nested dict, where username is the primary key and 
    # then cretes another dict inside wehre the book information is the key and the pdf path is the value
    def add_book_library(self, book , pdf_path, username):
        if username not in self.user_books:
            self.user_books[username] = {}
        key = (book.title, book.author, book.year)
        self.user_books[username][key] = pdf_path

    #this method takes the book in the user_books dict and moves it to the borrowed books dict and pops it from the user_books dict
    def lend_book_library(self, username, key):
        if username in self.user_books and key in self.user_books[username]:
            if username not in self.borrowed:
                self.borrowed[username] = {}
            self.borrowed[username][key] = self.user_books[username].pop(key)
        else:
            raise KeyError("Book not found in available books")

    #this method takes the book in the borrowed dict and returns it to the user_books dict 
    def return_book_library(self, username, key):
        if username in self.borrowed and key in self.borrowed[username]:
            self.user_books[username][key] = self.borrowed[username].pop(key)
        else:
            raise KeyError("Book not found in borrowed books")


    #it lists out the books in the user_books dict
    def list_available_books(self, username):
        if username in self.user_books:
            return [f"{i+1}. {title}, {author}, {year}" for i, (title, author, year) in enumerate(self.user_books[username].keys())]
        return []

    #it lists out the books in the borrowed books dict
    def list_borrowed_books(self, username):
        if username in self.borrowed:
            return [f"{i+1}. {title}, {author}, {year}" for i, (title, author, year) in enumerate(self.borrowed[username].keys())]
        return []
    