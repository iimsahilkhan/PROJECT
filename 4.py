import tkinter as tk
from tkinter import messagebox

# Library Class
class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        return self.books

    def borrowBook(self, bookName):
        if bookName in self.books:
            self.books.remove(bookName)
            return f'You have borrowed "{bookName}". Please return it in 30 days.'
        else:
            return "Sorry, this book is not available."

    def returnBook(self, bookName):
        self.books.append(bookName)
        return f'Thank you for returning "{bookName}".'

# GUI Application
class LibraryApp:
    def __init__(self, root, library):
        self.library = library
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("400x400")

        # Title
        tk.Label(root, text="Library Management System", font=("Arial", 14, "bold")).pack(pady=10)

        # Display Books Button
        tk.Button(root, text="List Available Books", command=self.show_books).pack(pady=5)

        # Borrow Section
        tk.Label(root, text="Enter Book to Borrow:").pack()
        self.borrow_entry = tk.Entry(root)
        self.borrow_entry.pack()
        tk.Button(root, text="Borrow Book", command=self.borrow_book).pack(pady=5)

        # Return Section
        tk.Label(root, text="Enter Book to Return:").pack()
        self.return_entry = tk.Entry(root)
        self.return_entry.pack()
        tk.Button(root, text="Return Book", command=self.return_book).pack(pady=5)

        # Quit Button
        tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white").pack(pady=10)

        # Result Display
        self.result_label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def show_books(self):
        books = "\n".join(self.library.displayAvailableBooks())
        messagebox.showinfo("Available Books", books if books else "No books available.")

    def borrow_book(self):
        book = self.borrow_entry.get()
        if book:
            msg = self.library.borrowBook(book)
            self.result_label.config(text=msg)
        else:
            self.result_label.config(text="Please enter a book name.")

    def return_book(self):
        book = self.return_entry.get()
        if book:
            msg = self.library.returnBook(book)
            self.result_label.config(text=msg)
        else:
            self.result_label.config(text="Please enter a book name.")

# Main Function
if __name__ == "__main__":
    library = Library(["Algorithms", "Django", "CLRS", "Python Notes"])
    root = tk.Tk()
    app = LibraryApp(root, library)
    root.mainloop()
