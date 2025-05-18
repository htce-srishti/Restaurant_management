import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

menu_json_path = os.path.join(BASE_DIR, 'menu.json')
order_json_path = os.path.join(BASE_DIR, 'order.json')
table_json_path = os.path.join(BASE_DIR, 'table.json')
bills_json_path = os.path.join(BASE_DIR, 'bills.json')   # Added for bills storage
