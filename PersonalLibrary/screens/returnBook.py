import customtkinter as ctk #custon TK inter import to use custom tk
from tkinter import Listbox, messagebox #imports tkinter 
from screens.screens_class import Screens #import screen class for inheritance


#Add book class, it inharits from custom tk and screens class
class ReturnBookScreen(ctk.CTk, Screens):
    def __init__(self, parent, library, username, update_callback):

        #create variables
        ctk.CTk.__init__(self)
        Screens.__init__(self, parent)
        self.library = library
        self.username = username
        self.update_callback = update_callback

        self.title("Return a Book")
        self.geometry("600x400")
        self.add_ui()


    #Abstract method, in each screen, to build the UI
    def add_ui(self):
        #frame for title
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20)

        #title label
        self.title = ctk.CTkLabel(self.frame, text="Select a Book to Return", font=ctk.CTkFont(family="Comic Sans MS",size=16))
        self.title.pack(pady=10)

        #frame for others
        list_frame = ctk.CTkFrame(self.frame)
        list_frame.pack(pady=10)

        # Borrowed books label
        borrowed_lable = ctk.CTkLabel(list_frame, text="Borrowed Books")
        borrowed_lable.grid(row=0, column=0, padx=10, pady=5)
        # borrowed books listbox
        self.borrowed_listbox = Listbox(list_frame, height=10, width=25)
        self.borrowed_listbox.grid(row=1, column=0, padx=10)

        # Available books label
        available_lable= ctk.CTkLabel(list_frame, text="Available Books")
        available_lable.grid(row=0, column=1, padx=10, pady=5)

        # Abailable books listbox
        self.available_listbox = Listbox(list_frame, height=10, width=25)
        self.available_listbox.grid(row=1, column=1, padx=10)

        #load the books in each lisbox
        self.load_borrowed_books()
        self.load_books()

        # return book button
        self.return_button = ctk.CTkButton(self.frame, text="Return Book", command=self.return_book)
        self.return_button.pack(pady=5)

        #back button to return to main
        self.back_button = ctk.CTkButton(self.frame, text="Back", fg_color="red", hover_color="#cc0000", command=self.back_to_main)
        self.back_button.pack(pady=10)

        self.mainloop()


    #method for returning book
    def return_book(self):
        #checks which book the user clicked 
        selection = self.borrowed_listbox.curselection()

        #if there are no books in the listbox then it will tell the user to select a book first (returns tuple)
        if self.borrowed_listbox.size() == 0:
            messagebox.showerror("Error", "No Books Borrowed.")
            return
        
        #no book selected then it will show error using a message box
        elif not selection:   
            messagebox.showerror("Error", "Please select a book from the 'Borrowed Books' listbox to return.")
            return
        
         #we get the first item in te listbox 
        selected_text = self.borrowed_listbox.get(selection[0])
        # Remove numbering so it doesnt look like 1.1. in the other listbox
        selected_text = selected_text.split(". ", 1)[-1]  

        #splits the title, name and year then puts them in a tuple
        
        title, author, year = [x.strip() for x in selected_text.split(",")]
        key = (title, author, year)
        

        #which moves the book from the borrowed book to user_books by calling return_book_library from library class
        #then it calles load_book and load_borrowed_books to refresh the listbox

        #if there dosent exist a book then it will call keyError and say book not found
        try:
            self.library.return_book_library(self.username, key)

            messagebox.showinfo("Success", f"You returned: {title}")
            self.load_borrowed_books()
            self.load_books()
            self.update_callback()

        except KeyError:
            messagebox.showerror("Error", "Book not found or already returned.")
