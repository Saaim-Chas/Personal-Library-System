#imports 
import customtkinter as ctk #custon TK inter import to use custom tk
from models.book import Book #import book class for use
from tkinter import filedialog,  messagebox, END, Listbox #import tkinter for specific elemenrts
from screens.screens_class import Screens #import screen class for inheritance


#Add book class, it inharits from custom tk and screens class
class AddBookScreen(ctk.CTk, Screens):
    def __init__(self, parent, library, update_callback, username):
        #create variables
        ctk.CTk.__init__(self)
        Screens.__init__(self, parent)
        self.library = library
        self.update_callback = update_callback
        self.pdf_path = None
        self.username = username
        self.geometry("750x550")
        self.add_ui()

#Abstract method, in each screen, to build the UI
    def add_ui(self):

        # Title Label 
        self.frame1 = ctk.CTkFrame(self)
        self.frame1.pack(pady=10)

        self.title_label = ctk.CTkLabel(self.frame1, text="Add Book", font=ctk.CTkFont("Comic Sans MS", 20))
        self.title_label.pack(padx=50, pady=15)

        #  Input Fields 
        self.frame2 = ctk.CTkFrame(self)
        self.frame2.pack(pady=10)

        # Book Name
        ctk.CTkLabel(self.frame2, text="Book Name:", font=ctk.CTkFont("Arial", 14)).grid(row=1, column=0, padx=10, sticky="w")
        self.name_entry = ctk.CTkEntry(self.frame2, width=200)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        # Author
        ctk.CTkLabel(self.frame2, text="Author:", font=ctk.CTkFont("Arial", 14)).grid(row=2, column=0, padx=10, sticky="w")
        self.author_entry = ctk.CTkEntry(self.frame2, width=200)
        self.author_entry.grid(row=2, column=1, padx=10, pady=5)

        # Year
        ctk.CTkLabel(self.frame2, text="Year Published:", font=ctk.CTkFont("Arial", 14)).grid(row=3, column=0, padx=10, sticky="w")
        self.year_entry = ctk.CTkEntry(self.frame2, width=200)
        self.year_entry.grid(row=3, column=1, padx=10, pady=5)

        # Add Button
        self.add_button = ctk.CTkButton(self.frame2, text="Add", command=self.add_book)
        self.add_button.grid(row=6, column=0, columnspan=2, pady = 5)

        #upload button
        self.upload_button = ctk.CTkButton(self.frame2, text="Upload PDF", command= self.upload_pdf)
        self.upload_button.grid(row=4, column=0, columnspan=2)

        #Not uploaded PDF
        self.status_label = ctk.CTkLabel(self.frame2, text = "PDF not uploaded", font=ctk.CTkFont("Arial", 10), text_color="red")
        self.status_label.grid(row=5, column =0, columnspan=2, sticky='N')

        #Listbox for Available Books 
        ctk.CTkLabel(self.frame2, text="Available Books:", font=ctk.CTkFont("Arial", 14)).grid(row=0, column=2, padx=10)
        self.book_listbox = Listbox(self.frame2, height=15, width=30)
        self.book_listbox.grid(row=1, column=2, rowspan=4, padx=10, pady=5)

        #it delets all previous data in the listbox and reloads the available lists
        self.book_listbox.delete(0, END)
        for i in self.library.list_available_books(self.username):
                self.book_listbox.insert(END, i)

        #frame 3, for button
        self.frame3 = ctk.CTkFrame(self)
        self.frame3.pack(pady=10)


        # Back Button 
        self.back_button = ctk.CTkButton(self.frame3, text="Back", fg_color="red", hover_color="#cc0000", command=self.back_to_main)
        self.back_button.grid(row=0, column=0, pady=20)

        self.mainloop()

    #upload PDF method
    def upload_pdf(self):
        #opens a file picker dialog restricted to pdf files only.
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

        #If the user selects a file, if the file_path is not empty, the path is saved in self.pdf_path
        #then it shows sussessful message
        if file_path:
            self.pdf_path = file_path
            messagebox.showinfo("Upload", "PDF uploaded successfully!")
            self.status_label.configure(text="PDF UPLOADED", text_color="green")

    #add mood method using the data entered and pdf path
    def add_book(self):
        #Reads user input from entry fields
        try:
            title = self.name_entry.get().strip()
            author = self.author_entry.get().strip()
            year = int(self.year_entry.get().strip())

            #error for if they did not add the pdf file first
            if not self.pdf_path:
                raise FileNotFoundError
        #exception for no pdf and value error
        except FileNotFoundError:
            messagebox.showerror("Missing PDF", "Please upload a PDF file.")
            return
        except ValueError:
            messagebox.showerror("Not a number", "Please enter a valid year, ex: 2025")
            return

        #Creates a Book object with the given details and stores them using the library method
        if title and author and year:
            book = Book(title, author, str(year))
            self.library.add_book_library(book, self.pdf_path, self.username)

        #clears the listbox, reloads all available books from the library and displays them.
            self.book_listbox.delete(0, END)
            for i in self.library.list_available_books(self.username):
                self.book_listbox.insert(END, i)
            self.name_entry.delete(0, "end")
            self.author_entry.delete(0, "end")
            self.year_entry.delete(0, "end")
            self.pdf_path = None
            self.update_callback()
            messagebox.showinfo("Successful", "Added Book successfully")
            self.status_label.configure(text="PDF not uploaded", text_color="red")


