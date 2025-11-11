#Imports 
import customtkinter as ctk #custon TK inter import to use custom tk
from tkinter import messagebox #import for tkinter message box to show error or give info
import os # access os to creat a txt file to store login info
from main import LibraryMain  #import the main to open after



class LoginSystem(ctk.CTk):
    #init method, it uses supoer to call custom tkinter methods 
    def __init__(self):
        super().__init__()
        #setup the main window and its appearence
        self.title("Library Login")
        self.geometry("400x350")
        ctk.set_appearance_mode("light")

        # starting state for the program
        self.mode = "login"
        self.user_file = "login_info/user_data.txt"

        # creating the UI of the login page
        self.title_label = ctk.CTkLabel(self, text="Library Login", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=20)
        
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username", width=250) 
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=250)
        self.password_entry.pack(pady=10)

        self.action_button = ctk.CTkButton(self, text="Login", command=self.handle_action)
        self.action_button.pack(pady=15)

        self.switch_button = ctk.CTkButton(self, text="Don't have an account? Sign Up", fg_color="transparent", text_color="blue", 
                                           hover=False, command=self.switch_mode)
        self.switch_button.pack()

        self.exit_button = ctk.CTkButton(self, text="Exit", fg_color="red", hover_color="#cc0000", command=self.destroy)
        self.exit_button.pack(pady=20)

     # checks if the user has put in all the details then call other functions to login or register the user
    def handle_action(self):
        #gets the username and passward form the entry
        username = self.username_entry.get().strip() 
        password = self.password_entry.get().strip()

        #Displays error either field is not filled out
        if not username or not password:
            messagebox.showerror("Error", "Please fill out all fields.")
            return

        #Checks the mode of the program, if login call login method, if register then call registen method
        if self.mode == "login":
            self.login_user(username, password)
        else:
            self.register_user(username, password)

    # method for what happens when the program is in login state
    def login_user(self, username, password):
        """Logs in an existing user"""

        #uses exception to check if the txt file already exists, if not then it will tell user to signup since there is no users on this device yet
        try:
            if not os.path.exists(self.user_file):
                raise FileNotFoundError("User database not found. Please sign up first.")
            
            #if the file exists, it will open the file, which was initialized in the __init__ function, then stores the user and pass in a dict
            with open(self.user_file, "r") as f:
                users = dict(line.strip().split(":") for line in f if ":" in line)

            #usinf the dict it checks if the username given matches the username in the dict, if so it will show success then open main file
            #if not it will show error then tell user that they entered incalid info
            if username in users and users[username] == password:
                messagebox.showinfo("Success", f"Welcome back, {username}!")
                try:
                    self.destroy()
                except Exception:
                    pass

                # Open the main library dashboard
                LibraryMain(username).mainloop()

            else:
                messagebox.showerror("Error", "Invalid username or password.")

        #if the file not found error is rissen it will display it using the messagebox or other unexpected error
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # method for what happens when the program is in register state
    def register_user(self, username, password):
        """Registers a new user."""

        #using exception to catch any errors then display them
        try:
            os.makedirs("Login_info", exist_ok=True) #check if the folder exists, if not it creates it

            # checks if the file which stores the user data exists, If it does the program reads it line by line and stors username and pass in a dict
            users = {}
            if os.path.exists(self.user_file):
                with open(self.user_file, "r") as f:
                    users = dict(line.strip().split(":") for line in f if ":" in line)
            #using the dict it checks if the username given is in the dict, if so then it will say the user already exsists
            if username in users:
                messagebox.showwarning("Warning", "Username already exists.")
                return
            #if not then it will create the data file and the name will be the username initialized in the __init__ fucntion then writes the user and pass in the file
            with open(self.user_file, "a") as f:
                f.write(f"{username}:{password}\n")


            #success message then switches to login page using the switch_mode method
            messagebox.showinfo("Success", "Account created successfully! You can now log in.")
            self.switch_mode()
        except Exception as e:
            messagebox.showerror("Error", str(e)) # any excetions are displayed using the messagebox

    #this method switches all the widgets on the screen so it matches the login or signup pages
    def switch_mode(self):
        """Switch between Login and Signup mode."""
        if self.mode == "login":
            self.mode = "signup"
            self.title_label.configure(text="Create Account")
            self.action_button.configure(text="Sign Up")
            self.switch_button.configure(text="Already have an account? Login")
        else:
            self.mode = "login"
            self.title_label.configure(text="Library Login")
            self.action_button.configure(text="Login")
            self.switch_button.configure(text="Don't have an account? Sign Up")



LoginSystem().mainloop()