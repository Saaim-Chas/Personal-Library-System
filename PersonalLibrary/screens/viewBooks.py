import customtkinter as ctk #custon TK inter import to use custom tk
from tkinter import Listbox, messagebox
from screens.screens_class import Screens
import os
import webbrowser

#Add book class, it inharits from custom tk and screens class
class ViewAllBooksScreen(ctk.CTk, Screens):
    def __init__(self, parent, library, username, update_callback):
        #create variables
        ctk.CTk.__init__(self)
        Screens.__init__(self, parent)
        self.library = library
        self.username = username
        self.update_callback = update_callback
        self.geometry("800x500")
        self.title("View All Books")
        self.add_ui()


    #Abstract method, in each screen, to build the UI
    def add_ui(self):
       #frome for title
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20)

        #title label
        self.title = ctk.CTkLabel(self.frame, text="Available Books", font=ctk.CTkFont(size=18, weight="bold"))
        self.title.pack(pady=10)

        # Listbox to show all available books
        self.available_listbox = Listbox(self.frame, height=15, width=40)
        self.available_listbox.pack(pady=10)

        # Load the books for display
        self.load_books()

        # View PDF button
        self.view_pdf_button = ctk.CTkButton(self.frame, text="View PDF", command=self.view_pdf)
        self.view_pdf_button.pack(pady=5)

        self.delete_button = ctk.CTkButton(self.frame, text = "Delete", fg_color="red", hover_color="#930404", command=self.delete_book)
        self.delete_button.pack(pady=5)

        # Back button
        self.back_button = ctk.CTkButton(self.frame, text="Back", fg_color="green", hover_color="#cc0000", 
                                         command=self.back_to_main)
        self.back_button.pack(pady=5)

        self.mainloop()

    #Loads available books using the parent class extehntion to the load method
    def load_books(self):
        super().load_books()

        #builds a list of book_keys (title, author, year) for later when opening PDFs
        self.book_keys = []
        if self.username in self.library.user_books:
            for key in self.library.user_books[self.username].keys():
                self.book_keys.append(key)

    #Open the selected book's PDF in the system's default browser.
    def view_pdf(self):
        #checks which book the user clicked 
        selection = self.available_listbox.curselection()
        #if there is no pdf selected then it will show error
        if not selection:
            messagebox.showerror("Error", "Please select a book to view.")
            return
        #we get the first item in te listbox 
        selected_text = self.available_listbox.get(selection[0])
        # Remove numbering so it doesnt look like 1.1. in the other listbox
        selected_text = selected_text.split(". ", 1)[-1]

        #splits the title, name and year then puts them in a tuple
        title, author, year = [x.strip() for x in selected_text.split(",")]
        key = (title, author, year)


        # Get PDF path from library
        #ensures this user has books stored, then cjeks if that book exists. 
        # If both are true then retrieve the PDF file path from the dictionary and assign it to pdf_path
        pdf_path = None
        if (
            self.username in self.library.user_books
            and key in self.library.user_books[self.username]
        ):
            pdf_path = self.library.user_books[self.username][key]

        #if the book is not founnd or it doesnt exist then it will show error message
        if not pdf_path or not os.path.exists(pdf_path):
            messagebox.showerror("Error", f"No PDF found for '{title}'.")
            return

        #Exception to try and open the pdf in the browser, if there is an error it ill display it
        try:
            webbrowser.open_new(pdf_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open PDF: {e}")


    def delete_book(self):
            selection = self.available_listbox.curselection()
            if not selection:
                messagebox.showerror("Error", "Please select a book to delete.")
                return

            # Get selected book text (e.g., "Title, Author, Year")
            selected_text = self.available_listbox.get(selection[0])
            selected_text = selected_text.split(". ", 1)[-1]  # remove numbering
            title, author, year = [x.strip() for x in selected_text.split(",")]
            key = (title, author, year)

            # Confirm deletion
            confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{title}'?")
            if not confirm:
                return

            # Check if book exists in user's library
            if (
                self.username in self.library.user_books
                and key in self.library.user_books[self.username]
            ):
                pdf_path = self.library.user_books[self.username][key]

                # Try deleting the file (optional)
                if os.path.exists(pdf_path):
                    try:
                        os.remove(pdf_path)
                    except Exception as e:
                        messagebox.showwarning("Warning", f"Could not delete PDF file: {e}")

                # Remove the book from the library dictionary
                del self.library.user_books[self.username][key]

                # Update display
                self.available_listbox.delete(selection[0])

                # Save updated data (if your library class has a save method)
                if hasattr(self.library, "save_books"):
                    self.library.save_books()

                messagebox.showinfo("Success", f"'{title}' has been deleted successfully.")
            else:
                messagebox.showerror("Error", "Book not found in your library.")
            self.update_callback()

            
