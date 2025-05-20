from SRC.order_processing.order_id_generator import generate_order_id
from SRC.order_processing.order_utils import calculate_total_price, get_current_time
from SRC.order_processing.order_status import update_order_status
from SRC.order_processing.order_database import load_orders, save_orders
from SRC.order_processing.receipt_generator import generate_receipt


def create_order(customer_name, items):
    orders = load_orders()
    order = {
        "order_id": generate_order_id(),
        "customer": customer_name,
        "items": items,
        "total": calculate_total_price(items),
        "status": "Pending",
        "timestamp": get_current_time()
    }
    orders.append(order)
    save_orders(orders)
    generate_receipt(order)

def cancel_order(order_id):
    orders = load_orders()
    found = False
    for order in orders:
        if order['order_id'] == order_id:
            if order['status'].lower() == "cancelled":
                print("Order already cancelled.")
            else:
                update_order_status(order, "Cancelled")
                save_orders(orders)
                print("Order cancelled successfully.")
            found = True
            break
    if not found:
        print("Order ID not found.")

def update_status(order_id, new_status):
    orders = load_orders()
    for order in orders:
        if order['order_id'] == order_id:
            update_order_status(order, new_status)
            save_orders(orders)
            print("Order status updated.")
            return
    print("Order ID not found.")

def view_all_orders():
    orders = load_orders()
    if not orders:
        print("No orders found.")
        return
    for order in orders:
        generate_receipt(order)
