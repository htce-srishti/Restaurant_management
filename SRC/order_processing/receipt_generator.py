def generate_receipt(order):
    print("\n====== ORDER RECEIPT ======")
    print(f"Order ID: {order['order_id']}")
    print(f"Time: {order['timestamp']}")
    print("Items:")
    for item in order['items']:
        print(f"- {item['name']} x {item['quantity']} = ₹{item['price'] * item['quantity']}")
    print(f"Total: ₹{order['total']}")
    print(f"Status: {order['status']}")
    print("===========================\n")
