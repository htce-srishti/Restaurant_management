import json
import os

table_file = "SRC/database/tables.json"

def load_tables():
    if not os.path.exists(table_file):
        with open(table_file, "w") as f:
            json.dump([], f)
    with open(table_file, "r") as f:
        return json.load(f)

def save_tables(tables):
    with open(table_file, "w") as f:
        json.dump(tables, f, indent=4)

def book_table():
    tables = load_tables()
    name = input("Enter your name: ")
    table_no = input("Enter table number to book: ")

    for t in tables:
        if t["table_no"] == table_no:
            print("Table already booked.")
            return

    tables.append({"name": name, "table_no": table_no})
    save_tables(tables)
    print("Table booked successfully.")

def show_booked_tables():
    tables = load_tables()
    if not tables:
        print("No tables booked.")
    else:
        print("\n--- Booked Tables ---")
        for t in tables:
            print(f'Table No: {t["table_no"]} - Name: {t["name"]}')