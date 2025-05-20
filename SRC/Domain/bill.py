import json
from datetime import datetime
from SRC.database import bills_json_path

class Billing:
    def __init__(self, customer_name, items):
        self.customer_name = customer_name
        self.items = items
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.total_amount = sum(item['quantity'] * item['price'] for item in items)
        self.payment_method = None

    def choose_payment_method(self):
        print("Select payment method:")
        print("1. UPI")
        print("2. Online")
        print("3. Cash")

        choice = input("Enter choice (1-3): ")
        if choice == "1":
            self.payment_method = "UPI"
        elif choice == "2":
            self.payment_method = "Online"
        elif choice == "3":
            self.payment_method = "Cash"
        else:
            print("Invalid choice. Defaulting to Cash.")
            self.payment_method = "Cash"

    def print_receipt(self):
        print(f"\nReceipt for {self.customer_name} on {self.date}")
        print("-" * 30)
        for item in self.items:
            print(f"{item['name']} x {item['quantity']} = ₹{item['quantity']*item['price']}")
        print(f"Total Amount: ₹{self.total_amount}")
        print(f"Payment Method: {self.payment_method}")
        print("-" * 30)

    def save_bill(self):
        bill_data = {
            "customer_name": self.customer_name,
            "items": self.items,
            "date": self.date,
            "total_amount": self.total_amount,
            "payment_method": self.payment_method
        }

        try:
            with open(bills_json_path, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append(bill_data)

        with open(bills_json_path, 'w') as f:
            json.dump(data, f, indent=4)
