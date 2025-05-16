from datetime import datetime

def calculate_total_price(items):
    return sum(item['price'] * item['quantity'] for item in items)

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
