import hashlib
import getpass
import tkinter as tk
from tkinter import messagebox, simpledialog
import unittest
from unittest.mock import patch
import sys

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

#Unittest
class TestPasswordManager(unittest.TestCase):

    def setUp(self):
        # Reset the password manager before each test
        global password_manager
        password_manager = {}

    @patch('__main__.simpledialog.askstring', side_effect=["testuser", "password123"])
    @patch('__main__.messagebox.showinfo')
    def test_create_account_success(self, mock_messagebox, mock_input):
        create_account()
        hashed_password = hashlib.sha256("password123".encode()).hexdigest()

        self.assertIn("testuser", password_manager)
        self.assertEqual(password_manager["testuser"], hashed_password)
        mock_messagebox.assert_called_with("Success", "Account has been created successfully!")

    @patch('__main__.simpledialog.askstring', side_effect=["", "password123"])
    @patch('__main__.messagebox.showwarning')
    def test_create_account_empty_username(self, mock_messagebox, mock_input):
        create_account()
        self.assertNotIn("", password_manager)
        mock_messagebox.assert_called_with("Error", "Username or password cannot be empty.")

    @patch('__main__.simpledialog.askstring', side_effect=["testuser", "password123"])
    @patch('__main__.messagebox.showinfo')
    def test_login_success(self, mock_messagebox, mock_input):
        hashed_password = hashlib.sha256("password123".encode()).hexdigest()
        password_manager["testuser"] = hashed_password

        login()
        mock_messagebox.assert_called_with("Login", "Login successful!")

    @patch('__main__.simpledialog.askstring', side_effect=["testuser", "wrongpassword"])
    @patch('__main__.messagebox.showerror')
    def test_login_invalid_password(self, mock_messagebox, mock_input):
        hashed_password = hashlib.sha256("password123".encode()).hexdigest()
        password_manager["testuser"] = hashed_password

        login()
        mock_messagebox.assert_called_with("Error", "Invalid username or password.")

    @patch('__main__.simpledialog.askstring', side_effect=["unknownuser", "password123"])
    @patch('__main__.messagebox.showerror')
    def test_login_invalid_username(self, mock_messagebox, mock_input):
        login()
        mock_messagebox.assert_called_with("Error", "Invalid username or password.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Run the unit tests if "test" argument is passed
        unittest.main(argv=[sys.argv[0]], exit=False)
    else:
        # Launch the GUI
        main()