
# ER Diagram – Finance Money Exchange System

##  Overview

This Entity-Relationship (ER) diagram represents a **finance money exchange system**. It includes key entities such as customers, accounts, transactions, currencies, and exchanges, along with their relationships.

---

#  Entities and Attributes

## 1. CUSTOMER

* **CustomerID (PK)**
* FirstName
* LastName
* Email
* Phone
* Address
* DateOfBirth

---

## 2. ACCOUNT

* **AccountID (PK)**
* AccountNumber
* AccountType
* Balance
* **CustomerID (FK)**

---

## 3. TRANSACTION

* **TransactionID (PK)**
* TransactionDate
* Amount
* TransactionType
* Status
* **AccountID (FK)**

---

## 4. CURRENCY

* **CurrencyCode (PK)**
* CurrencyName
* Symbol
* Country
* ExchangeRate

---

## 5. EXCHANGE

* **ExchangeID (PK)**
* ExchangeDate
* AmountFrom
* AmountTo
* RateUsed
* **TransactionID (FK)**
* **FromCurrency (FK)**
* **ToCurrency (FK)**

---

#  Relationships

## 1. CUSTOMER — OWNS — ACCOUNT

* Type: **1 : N**
* One customer can own multiple accounts
* Each account belongs to one customer

---

## 2. ACCOUNT — HAS — TRANSACTION

* Type: **1 : N**
* One account can have many transactions
* Each transaction belongs to one account

---

## 3. TRANSACTION — GENERATES — EXCHANGE

* Type: **1 : 1**
* Each transaction generates one exchange record

---

## 4. CURRENCY — EXCHANGE (FROM)

* Type: **1 : N**
* One currency can be used in many exchanges as source

---

## 5. CURRENCY — EXCHANGE (TO)

* Type: **1 : N**
* One currency can be used in many exchanges as target

---

#  Relationship Summary Table

| Relationship               | Type  |
| -------------------------- | ----- |
| CUSTOMER → ACCOUNT         | 1 : N |
| ACCOUNT → TRANSACTION      | 1 : N |
| TRANSACTION → EXCHANGE     | 1 : 1 |
| CURRENCY → EXCHANGE (FROM) | 1 : N |
| CURRENCY → EXCHANGE (TO)   | 1 : N |


