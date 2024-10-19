import hashlib
import getpass
import tkinter as tk
from tkinter import messagebox, simpledialog

password_manager = {}
def create_account():
    username = simpledialog.askstring("Create Account", "Enter username:")
    password = simpledialog.askstring("Create Account", "Enter password:", show=".")
    
    if username and password:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        password_manager[username] = hashed_password
        messagebox.showinfo("Success", "Account has been created successfully!")
    else:
        messagebox.showwarning("Error", "Username or password cannot be empty.")
