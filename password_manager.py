import hashlib
import getpass

password_manager = {}
def create_account():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account has been created successfully!")