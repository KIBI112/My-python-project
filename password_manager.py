import hashlib
import getpass
import tkinter as tk
from tkinter import messagebox, simpledialog

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
    