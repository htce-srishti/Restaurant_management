import json
from getpass import getpass

def login():
    email = input("Enter your email: ")
    password = getpass("Enter your password (hidden): ")

    try:
        with open("SRC/database/users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("No users found. Please signup first.")
        return False

    for user in users:
        if user["email"] == email and user["password"] == password:
            print("Login successful.")
            return True

    print("Invalid email or password.")
    return False