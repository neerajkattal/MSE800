import sqlite3

def create_tables():
    conn = sqlite3.connect("exchange.db")
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

    # CUSTOMER
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customer (
        CustomerID INTEGER PRIMARY KEY,
        FirstName TEXT,
        LastName TEXT,
        Email TEXT,
        Phone TEXT,
        Address TEXT
    );
    """)

    # ACCOUNT
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Account (
        AccountID INTEGER PRIMARY KEY,
        AccountNumber TEXT,
        AccountType TEXT,
        Balance REAL,
        CustomerID INTEGER,
        FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
    );
    """)

    # TRANSACTIONS (fixed name)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Transactions (
        TransactionID INTEGER PRIMARY KEY,
        TransactionDate TEXT,
        Amount REAL,
        TransactionType TEXT,
        Status TEXT,
        AccountID INTEGER,
        FOREIGN KEY (AccountID) REFERENCES Account(AccountID)
    );
    """)

    # CURRENCY
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Currency (
        CurrencyCode TEXT PRIMARY KEY,
        CurrencyName TEXT,
        Symbol TEXT,
        ExchangeRate REAL,
        LastUpdated TEXT
    );
    """)

    # EXCHANGE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Exchange (
        ExchangeID INTEGER PRIMARY KEY,
        ExchangeDate TEXT,
        AmountFrom REAL,
        AmountTo REAL,
        RateUsed REAL,
        TransactionID INTEGER,
        FromCurrency TEXT,
        ToCurrency TEXT,
        FOREIGN KEY (TransactionID) REFERENCES Transactions(TransactionID),
        FOREIGN KEY (FromCurrency) REFERENCES Currency(CurrencyCode),
        FOREIGN KEY (ToCurrency) REFERENCES Currency(CurrencyCode)
    );
    """)

    conn.commit()
    conn.close()
    print("Database created successfully!")