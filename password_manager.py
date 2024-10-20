import hashlib
import getpass
import tkinter as tk
from tkinter import messagebox, simpledialog
import sys
import unittest
from unittest.mock import patch

password_manager = {}
#creat account
def create_account():
    username = simpledialog.askstring("Create Account", "Enter username:")
    password = simpledialog.askstring("Create Account", "Enter password:", show=".")
    
    if username and password:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        password_manager[username] = hashed_password
        messagebox.showinfo("Success", "Account has been created successfully!")
    else:
        messagebox.showwarning("Error", "Username or password cannot be empty.")


#login
def login():
    username = simpledialog.askstring("Login", "Enter your username:")
    password = simpledialog.askstring("Login", "Enter your password:", show=".")

    if username in password_manager and password_manager[username] == hashlib.sha256(password.encode()).hexdigest():
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password.")
    
#main window layout
def main():
    root = tk.Tk()
    root.title("Password Manager")
    root.geometry("400x400")
    root.config(bg="black")

    title = tk.Label(root, text="Password Manager", font=("Times New", 22, "bold"), bg="black", fg="white")
    title.pack(pady=30)

    button_style = {"font": ("Arial", 14), "bg": "dark slate blue", "fg": "white", "activebackground": "grey", "activeforeground": "red"}
    
    tk.Button(root, text="Create Account", command=create_account, **button_style).pack(pady=25)
    tk.Button(root, text="Login", command=login, **button_style).pack(pady=25)
    tk.Button(root, text="Exit", command=root.quit, **button_style).pack(pady=25)

    root.mainloop()



if __name__ == "__main__":
    main()