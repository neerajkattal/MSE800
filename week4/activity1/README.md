# Money Exchange Database System (SQLite3)

##  Project Overview

This project implements a **Money Exchange Database System** using SQLite3. The database is designed based on an Entity-Relationship (ER) diagram and supports managing customers, accounts, transactions, currencies, and currency exchanges.

---

## Total Number of Tables: 5

The database consists of the following five tables:

1. Customer
2. Account
3. Transaction
4. Currency
5. Exchange

---

##  Table Descriptions and Justification

### 1. Customer Table

Stores personal details of users.

**Attributes:**

* CustomerID (Primary Key)
* FirstName
* LastName
* Email
* Phone
* Address

**Justification:**
This table is necessary to store user information. Each customer represents a user of the system who can own one or more accounts.

---

### 2. Account Table

Stores financial account details linked to customers.

**Attributes:**

* AccountID (Primary Key)
* AccountNumber
* AccountType
* Balance
* CustomerID (Foreign Key)

**Justification:**
This table separates financial data from personal data. A customer can have multiple accounts, establishing a one-to-many relationship.

---

### 3. Transaction Table

Stores records of financial operations.

**Attributes:**

* TransactionID (Primary Key)
* TransactionDate
* Amount
* TransactionType
* Status
* AccountID (Foreign Key)

**Justification:**
This table tracks all activities such as deposits, withdrawals, and exchanges. It is essential for maintaining transaction history.

---

### 4. Currency Table

Stores information about different currencies.

**Attributes:**

* CurrencyCode (Primary Key)
* CurrencyName
* Symbol
* ExchangeRate
* LastUpdated

**Justification:**
This table enables the system to support multiple currencies and store exchange rates required for conversions.

---

### 5. Exchange Table

Stores currency conversion details.

**Attributes:**

* ExchangeID (Primary Key)
* ExchangeDate
* AmountFrom
* AmountTo
* RateUsed
* TransactionID (Foreign Key)
* FromCurrency (Foreign Key)
* ToCurrency (Foreign Key)

**Justification:**
This table handles currency exchange operations. It links transactions with currencies and stores conversion details, resolving many-to-many relationships between currencies.

---

##  Relationships Between Tables

* One Customer → Many Accounts (1:N)
* One Account → Many Transactions (1:N)
* One Transaction → One Exchange (1:1)
* Currency used in Exchanges (M:N resolved through Exchange table)

---

## Technologies Used

* Python
* SQLite3

---

## How to Run

1. Run the Python program:

   ```bash
   python main.py
   ```
2. The database file (`exchange.db`) will be created automatically.
3. Use the menu to interact with the system.

---

## Project Files

* `main.py` → Main application (menu system)
* `database.py` → Database and table creation
* `user_manager.py` → Functions for managing data
* `exchange.db` → SQLite database file

---

##  Author

Your Name
