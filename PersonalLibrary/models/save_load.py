#importts
import pickle
import os
from models.library import Library

#function for saving the lobrary info, including the books, and user details
def save_library(username, library):
    os.makedirs("library_data", exist_ok=True)
    with open(f"library_data/{username}.pkl", "wb") as f:
        pickle.dump(library, f)

#function for loading the user books

def load_library(username):
    try:
        with open(f"library_data/{username}.pkl", "rb") as f:
            library = pickle.load(f)
            return library
    except FileNotFoundError:
        return Library()
