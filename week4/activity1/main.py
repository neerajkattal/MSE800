from database import create_tables
from user_manager import *

def menu():
    print("\n==== Money Exchange System ====")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Add Account")
    print("4. View Accounts")
    print("5. Add Transaction")
    print("6. View Transactions")
    print("7. Add Currency")
    print("8. View Currency")
    print("9. Exit")

def main():
    create_tables()

    while True:
        menu()
        choice = input("Select an option (1-9): ")

        if choice == '1':
            add_customer(
                input("First Name: "),
                input("Last Name: "),
                input("Email: "),
                input("Phone: "),
                input("Address: ")
            )

        elif choice == '2':
            for row in view_customers():
                print(row)

        elif choice == '3':
            add_account(
                input("Account Number: "),
                input("Account Type: "),
                float(input("Balance: ")),
                int(input("Customer ID: "))
            )

        elif choice == '4':
            for row in view_accounts():
                print(row)

        elif choice == '5':
            add_transaction(
                input("Date: "),
                float(input("Amount: ")),
                input("Type: "),
                input("Status: "),
                int(input("Account ID: "))
            )

        elif choice == '6':
            for row in view_transactions():
                print(row)

        elif choice == '7':
            add_currency(
                input("Currency Code: "),
                input("Name: "),
                input("Symbol: "),
                float(input("Rate: ")),
                input("Date: ")
            )

        elif choice == '8':
            for row in view_currency():
                print(row)

        elif choice == '9':
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()