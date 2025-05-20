import json
import os
from datetime import datetime

TABLE_FILE = os.path.join(os.path.dirname(__file__), '..', 'database', 'tables.json')
TABLE_FILE = os.path.abspath(TABLE_FILE)

def load_tables():
    with open(TABLE_FILE, 'r') as f:
        return json.load(f)

def save_tables(tables):
    with open(TABLE_FILE, 'w') as f:
        json.dump(tables, f, indent=4)

def show_table_status():
    tables = load_tables()
    print("\n Table Status:")
    for table in tables:
        available = table['total_chairs'] - table['booked_chairs']
        print(f"Table {table['table_id']} | Total: {table['total_chairs']} | Booked: {table['booked_chairs']} | Available: {available}")

def show_booked_tables():
    tables = load_tables()
    print("\n Booked Tables:")
    for table in tables:
        if table['booked_chairs'] > 0:
            available = table['total_chairs'] - table['booked_chairs']
            print(f"Table {table['table_id']} | Booked: {table['booked_chairs']} | Available: {available} | Customer: {table['customer']} | Time: {table['time']}")

def book_table():
    tables = load_tables()
    show_table_status()

    try:
        table_id = int(input("\nEnter Table ID to book: "))
        chairs_needed = int(input("Enter number of chairs to book: "))
        customer = input("Enter customer name: ")

        for table in tables:
            if table['table_id'] == table_id:
                available = table['total_chairs'] - table['booked_chairs']
                if chairs_needed <= available:
                    table['booked_chairs'] += chairs_needed
                    table['customer'] = customer
                    table['status'] = 'booked' if table['booked_chairs'] == table['total_chairs'] else 'partially booked'
                    table['time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    save_tables(tables)
                    print(f"\n Booked {chairs_needed} chair(s) at Table {table_id} for {customer}")
                    return
                else:
                    print(f"\n Only {available} chairs available at Table {table_id}")
                    return

        print("\n Invalid Table ID.")
    except ValueError:
        print("\  Please enter valid numbers.")

if __name__ == "__main__":
    book_table()
