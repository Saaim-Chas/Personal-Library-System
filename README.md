# Personal-Library-System
A Python-based Personal Library System using Tkinter/CustomTkinter. It allows users to manage their personal library. Users can **log in / sign up**, add books with associated PDFs, lend and return books, view all available books, and delete entries. The system persists data locally using `pickle`. Built with OOP and modular screen design.

---

## Features
- **Login & Signup System**
  - Secure user accounts stored in a local text file.
  - Switch between login and signup modes easily.

- **Book Management**
  - Add books with title, author, year, and PDF file.
  - Lend books to mark them as borrowed.
  - Return borrowed books back to available.
  - View all books with options to open PDFs or delete entries.

- **Persistence**
  - User libraries are saved automatically using `pickle`.
  - Each user has their own `.pkl` file inside `library_data/`.

- **CustomTkinter UI**
  - Modern, themed interface with multiple screens:
    - `AddBookScreen`
    - `LendBookScreen`
    - `ReturnBookScreen`
    - `ViewAllBooksScreen`
    - `LibraryMain` (dashboard)
---

## Project Structure
```
project/
│
├── models/
│   ├── book.py          # Book class
│   ├── library.py       # Library class (add, lend, return, list)
│   ├── save_load.py     # Save/load functions using pickle
│
├── screens/
│   ├── screens_class.py # Abstract base class for screens
│   ├── addBook.py       # AddBookScreen
│   ├── lendBook.py      # LendBookScreen
│   ├── returnBook.py    # ReturnBookScreen
│   ├── viewBooks.py     # ViewAllBooksScreen
│
├── login.py             # LoginSystem (entry point)
├── main.py              # LibraryMain dashboard

```

---

## Getting Started

### Prerequisites
- Python 3.10+
- Install dependencies:
  ```bash
  pip install customtkinter

# Run Application
1. Clone the repository or download the project files.
2. Start with Login system (Login.py)
3. Create an account or login
4. Manage your personal library through the dashboard


# Data Storage
  - User Credentials are stored in:
    - ```login_info/user_data.txt```
 - Each user’s library is stored in:
    - ```library_data/{username}.pkl```

---

# Notes

 - Passwords are stored in plain text (for demo purposes). \
    🔒 Consider hashing passwords for real-world use.

- Pickle files are not secure against tampering. \
    📦 For production, use JSON or SQLite.


# Author: 
Developed by Syed Saaim Asif Chashoo as a software engineering learning project at KMITL. This project demonstrates object-oriented design, persistence, and GUI development in Python.

