import customtkinter as ctk #custon TK inter import to use custom tk
from tkinter import Listbox, messagebox #imports tkinter 
from screens.screens_class import Screens #import screen class for inheritance

#Add book class, it inharits from custom tk and screens class
class LendBookScreen(ctk.CTk, Screens):
    def __init__(self, parent, library, username, update_callback):
        #create variables
        ctk.CTk.__init__(self)
        Screens.__init__(self, parent)
        self.library = library
        self.username = username
        self.update_callback = update_callback

        self.title("Lend a Book")
        self.geometry("600x400")
        self.add_ui()

    #Abstract method, in each screen, to build the UI
    def add_ui(self):

        # frame for label
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20)

        # Title Label 
        self.title = ctk.CTkLabel(self.frame, text="Select a Book to Lend", font=ctk.CTkFont(family="Comic Sans MS",size=16))
        self.title.pack(pady=10)

        # Frame for the rest 
        list_frame = ctk.CTkFrame(self.frame)
        list_frame.pack(pady=10)
        
        #available lable
        available_lable= ctk.CTkLabel(list_frame, text="Available Books")
        available_lable.grid(row=0, column=0, padx=10, pady=5)

        #available list box
        self.available_listbox = Listbox(list_frame, height=10, width=25)
        self.available_listbox.grid(row=1, column=0, padx=30)

        #Borrowed lable
        borrowed_lable = ctk.CTkLabel(list_frame, text="Borrowed Books")
        borrowed_lable.grid(row=0, column=1, padx=10)

        #Borrowed listbox
        self.borrowed_listbox = Listbox(list_frame, height=10, width=25)
        self.borrowed_listbox.grid(row=1, column=1, padx=10)

        #load the two dictionaries
        self.load_books()
        self.load_borrowed_books()

        #lend button
        self.lend_button = ctk.CTkButton(self.frame, text="Lend Book", command=self.lend_book)
        self.lend_button.pack(pady=5)

        #back button
        self.back_button = ctk.CTkButton(self.frame, text="Back", fg_color="red", hover_color="#cc0000", command=self.back_to_main)
        self.back_button.pack(pady=10)

        self.mainloop()
        

    # lend book method
    def lend_book(self):
        #checks which book the user clicked 
        selection = self.available_listbox.curselection()

        #if there are no books in the listbox then it will tell the user to select a book first (returns tuple)
        if self.available_listbox.size() == 0:
            messagebox.showerror("Error", "No Books Available, Please add a book first")
            return
        #no book selected then it will show error using a message box
        elif not selection:
            messagebox.showerror("Error", "Please select a book from the 'Available Books' listbox to lend.")
            return
        
        #we get the first item in te listbox 
        selected_text = self.available_listbox.get(selection[0])
        # Remove numbering so it doesnt look like 1.1. in the other listbox
        selected_text = selected_text.split(". ", 1)[-1]
        #splits the title, name and year then puts them in a tuple
        title, author, year = [x.strip() for x in selected_text.split(",")]
        key = (title, author, year)

        #which is then moves the book from the user_books to borrowed book by calling lend_book_library from library class
        #then it calles load_book and load_borrowed_books to refresh the listbox in all screens

        #if there dosent exist a book then it will call keyError and say book not found
        try:
            self.library.lend_book_library(self.username, key)
            messagebox.showinfo("Success", f"You lent: {title}")
            self.load_books()
            self.load_borrowed_books()
            self.update_callback()
        except KeyError:
            messagebox.showerror("Error", "Book not found or already lent.")

