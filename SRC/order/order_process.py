import json
from datetime import datetime
from SRC.database import order_json_path

def place_order(menu):
    print("\nPlace your order:")
    order = []
    total_price = 0

    while True:
        try:
            print("\n--- Menu ---")
            for item in menu:
                name = item['name'].capitalize()
                portion = item.get('portion', 'full')
                category = item.get('category', 'Uncategorized')
                price = item['price']
                print(f"{item['id']}. {name} ({portion.capitalize()}) - ₹{price} [{category.capitalize()}]")

            item_id = int(input("Enter item ID to order (0 to finish): "))
            if item_id == 0:
                break

            selected_item = next((item for item in menu if item['id'] == item_id), None)
            if not selected_item:
                print("Invalid item ID. Try again.")
                continue

            portion = input("Enter portion size (half/full): ").strip().lower()
            if portion not in ['half', 'full']:
                print("Invalid portion size.")
                continue

            try:
                quantity = int(input(f"Enter quantity for {selected_item['name']} ({portion}): "))
            except ValueError:
                print("Please enter valid numbers for quantity.")
                continue

            price = selected_item['price']
            item_total = price * quantity
            total_price += item_total

            order.append({
                "id": selected_item['id'],
                "name": selected_item['name'],
                "portion": portion,
                "quantity": quantity,
                "price": price,
                "total": item_total
            })

            print(f"Added {quantity} x {portion} {selected_item['name']} to your order.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    if not order:
        print("No items ordered.")
        return

    # Show order summary
    print("\nCurrent Order Summary:")
    for idx, item in enumerate(order, 1):
        print(f"{idx}. {item['quantity']} x {item['portion']} {item['name'].capitalize()} - ₹{item['total']:.2f}")

    print(f"\nTotal Amount: ₹{total_price:.2f}")

    # Ask for confirmation
    confirm = input("\nDo you want to confirm this order? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("Order cancelled.")
        return

    # Add timestamp and save order
    order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    order_data = {
        "items": order,
        "total_price": total_price,
        "order_time": order_time
    }

    try:
        with open(order_json_path, 'r') as f:
            all_orders = json.load(f)
    except FileNotFoundError:
        all_orders = []

    all_orders.append(order_data)

    with open(order_json_path, 'w') as f:
        json.dump(all_orders, f, indent=4)

    print("\n Order confirmed!")
    print(f" Ordered on: {order_time}")
