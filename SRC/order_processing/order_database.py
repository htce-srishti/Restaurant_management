import json
import os

ORDERS_FILE = os.path.join("database", "order.json")  

def load_orders():
    if not os.path.exists(ORDERS_FILE):
        return []
    with open(ORDERS_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_orders(orders):
    folder = os.path.dirname(ORDERS_FILE)
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(ORDERS_FILE, 'w') as f:
        json.dump(orders, f, indent=4)
