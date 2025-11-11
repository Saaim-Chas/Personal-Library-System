#Class to all the books list and titles

class Book():
    def __init__(self, title, author, year):
        """Stores attributes for a book"""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title}, {self.author}, {self.year}"
