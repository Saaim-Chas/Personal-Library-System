from abc import ABC, abstractmethod
from tkinter import END


class Screens(ABC):
    def __init__(self, parent):
        self.parent = parent

#Abstract class which is set to chenge in each of the screens
    @abstractmethod
    def add_ui(self):
        """Each screen will have its own add_ui method"""
        pass

#This method is fr the back to the main file, this can be used in all of the subclasses.
    def back_to_main(self):
        self.destroy()
        self.parent.deiconify()

#this method will be a recurring method in the return and lend book classes
#this method deletes any information alrady on the listbox 
#then loads available books which are stored in a dictionary through the library class
    def load_books(self):
        """Loads available books (right list)."""
        self.available_listbox.delete(0, END)
        books = self.library.list_available_books(self.username)
        for book in books:
            self.available_listbox.insert(END, book)

#this method will be a recurring method in the return and lend book classes
#this method this method deletes any information alrady on the listbox 
#then loads borrowed books which are stored in a dictionary through the library class
    def load_borrowed_books(self):
        """Loads borrowed books (left list)."""
        self.borrowed_listbox.delete(0, END)
        books = self.library.list_borrowed_books(self.username)
        for book in books:
            self.borrowed_listbox.insert(END, book)
