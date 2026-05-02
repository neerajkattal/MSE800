import sqlite3

def create_connection():
    return sqlite3.connect("exchange.db")

# ---------------- CUSTOMER ----------------
def add_customer(fname, lname, email, phone, address):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Customer (FirstName, LastName, Email, Phone, Address)
        VALUES (?, ?, ?, ?, ?)
    """, (fname, lname, email, phone, address))

    conn.commit()
    conn.close()
    print("Customer added!")

def view_customers():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Customer")
    rows = cursor.fetchall()
    conn.close()
    return rows

# ---------------- ACCOUNT ----------------
def add_account(acc_num, acc_type, balance, customer_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Account (AccountNumber, AccountType, Balance, CustomerID)
        VALUES (?, ?, ?, ?)
    """, (acc_num, acc_type, balance, customer_id))

    conn.commit()
    conn.close()
    print("Account added!")

def view_accounts():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Account")
    rows = cursor.fetchall()
    conn.close()
    return rows

# ---------------- TRANSACTIONS ----------------
def add_transaction(date, amount, ttype, status, account_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Transactions (TransactionDate, Amount, TransactionType, Status, AccountID)
        VALUES (?, ?, ?, ?, ?)
    """, (date, amount, ttype, status, account_id))

    conn.commit()
    conn.close()
    print("Transaction added!")

def view_transactions():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Transactions")
    rows = cursor.fetchall()
    conn.close()
    return rows

# ---------------- CURRENCY ----------------
def add_currency(code, name, symbol, rate, date):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Currency (CurrencyCode, CurrencyName, Symbol, ExchangeRate, LastUpdated)
        VALUES (?, ?, ?, ?, ?)
    """, (code, name, symbol, rate, date))

    conn.commit()
    conn.close()
    print("Currency added!")

def view_currency():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Currency")
    rows = cursor.fetchall()
    conn.close()
    return rows