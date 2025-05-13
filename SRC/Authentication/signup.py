import json
import os
from getpass import getpass

def signup():
    email = input("Enter your email: ")
    password = getpass("Enter your password (hidden): ")

    if not os.path.exists("SRC/database/users.json"):
        with open("SRC/database/users.json", "w") as f:
            json.dump([], f)

    with open("SRC/database/users.json", "r") as file:
        users = json.load(file)

    for user in users:
        if user["email"] == email:
            print("Email already exists.")
            return

    users.append({"email": email, "password": password})

    with open("SRC/database/users.json", "w") as file:
        json.dump(users, file, indent=4)

    print("Signup successful.")