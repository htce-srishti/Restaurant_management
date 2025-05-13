from SRC.Authentication.signup import signup
from SRC.Authentication.login import login
from SRC.menu.menu_managment import display_menu, add_menu_item
from SRC.table.table_booking import book_table, show_booked_tables

def main():
    while True:
        print("\n--- Restaurant Management System ---")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            signup()
        elif choice == "2":
            if login():
                after_login_menu()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

def after_login_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Display Menu")
        print("2. Add Menu Item")
        print("3. Book a Table")
        print("4. Show Booked Tables")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_menu()
        elif choice == "2":
            add_menu_item()
        elif choice == "3":
            book_table()
        elif choice == "4":
            show_booked_tables()
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()