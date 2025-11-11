import customtkinter as ctk
from tkinter import Listbox, END

#import models
from models.library import Library
from models.save_load import save_library, load_library
from models.book import Book


#import screens
from screens.addBook import AddBookScreen
from screens.lendBook import LendBookScreen
from screens.returnBook import ReturnBookScreen
from screens.viewBooks import ViewAllBooksScreen
class LibraryMain(ctk.CTk):
    def __init__(self, username: str = None):
        super().__init__()                         # proper CTk initialization
        self.username = username
        self.title("Personal Library Dashboard")
        self.geometry("750x500")


        self.library = load_library(self.username)

        self.create_frames_and_widgets()

        self.update_listbox()

    def create_frames_and_widgets(self):
        self.frame1 = ctk.CTkFrame(self)
        self.frame2 = ctk.CTkFrame(self)
        self.frame3 = ctk.CTkFrame(self)
        self.frame4 = ctk.CTkFrame(self)

        self.title_label = ctk.CTkLabel(self.frame1, text="Personal Library Dashboard", font=ctk.CTkFont(family="Comic Sans MS", size=24))
        welcome = f"Welcome, {self.username}!" if self.username else "Welcome!"
        self.welcome_label = ctk.CTkLabel(self.frame1, text=welcome, font=ctk.CTkFont(family= "Comic Sans MS", size=14))

        self.available_label = ctk.CTkLabel(self.frame2, text="Available Books:", font=ctk.CTkFont(size=15))
        self.borrowed_label = ctk.CTkLabel(self.frame2, text="Borrowed Books:", font=ctk.CTkFont(size=15))

        # tkinter Listbox is fine to use inside customtkinter UI
        self.box1 = Listbox(self.frame2, font=("Segoe UI", 10), height=15, width=30)
        self.box2 = Listbox(self.frame2, font=("Segoe UI", 10), height=15, width=30)

        self.add_book = ctk.CTkButton(self.frame3, text="Add Book", fg_color="#ca9e0e", command=self.add)
        self.lend_book = ctk.CTkButton(self.frame3, text="Lend Book", fg_color="#0fb609", command=self.lend)
        self.return_bookb = ctk.CTkButton(self.frame3, text="Return Book",fg_color="#3449e8", command=self.return_book)
        self.All_books = ctk.CTkButton(self.frame3, text="View All Books", command=self.All_books_window)
        self.exit_btn = ctk.CTkButton(self.frame4, text="EXIT", fg_color="red", hover_color="#cc0000", command=self.destroy)

        self.frame1.pack(pady=10)
        self.frame2.pack(pady=5)
        self.frame3.pack(pady=5)
        self.frame4.pack(pady=5)

        self.title_label.pack(padx=50, pady=5)
        self.welcome_label.pack(pady=2)
        self.available_label.grid(row=1, column=0)
        self.borrowed_label.grid(row=1, column=1)
        self.box1.grid(row=2, column=0, padx=10, sticky="n")
        self.box2.grid(row=2, column=1, padx=10, sticky="n")

        self.add_book.grid(row=0, column=0, padx=10, pady=5)
        self.lend_book.grid(row=0, column=1, padx=10, pady=5)
        self.return_bookb.grid(row=0, column=3, padx=10, pady=5)
        self.All_books.grid(row=0, column=4, padx=10, pady=5)
        self.exit_btn.grid(padx=10, pady=10)
    

    def update_listbox(self):
        self.box1.delete(0, END)
        for i in self.library.list_available_books(self.username):
            self.box1.insert(END, i)
        self.box2.delete(0, END)
        for i in self.library.list_borrowed_books(self.username):
            self.box2.insert(END, i)

        # Save the library automatically whenever listboxes update
        save_library(self.username, self.library)


    def add(self):
        self.withdraw()
        AddBookScreen(self, self.library, self.update_listbox, self.username)

    def lend(self):
        self.withdraw()
        LendBookScreen(self, self.library, self.username, self.update_listbox)
    
    def return_book(self):
        self.withdraw()
        ReturnBookScreen(self, self.library, self.username, self.update_listbox)
        
    def All_books_window(self):
        self.withdraw()
        ViewAllBooksScreen(self, self.library, self.username, self.update_listbox)

        

        
if __name__ == "__main__":
    app = LibraryMain()
    app.mainloop()