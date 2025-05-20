import json
import os

menu_file = "SRC/database/menu.json"

def load_menu():
    if not os.path.exists(menu_file):
        with open(menu_file, "w") as f:
            json.dump([], f)
    with open(menu_file, "r") as f:
        return json.load(f)

def save_menu(menu):
    with open(menu_file, "w") as f:
        json.dump(menu, f, indent=4)

def display_menu():
    menu = load_menu()
    if not menu:
        print("Menu is empty.")
    else:
        print("\n--- Menu ---")
        for item in menu:
            print(f'{item["id"]}. {item["name"]} - ₹{item["price"]}')

def add_menu_item():
    menu = load_menu()
    item_id = len(menu) + 1
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    menu.append({"id": item_id, "name": name, "price": price})
    save_menu(menu)
    print("Item added successfully.")