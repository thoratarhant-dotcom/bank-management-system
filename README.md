# 🏦 Banking System (OOP Project in Python)

A console-based Banking System built using Object-Oriented Programming principles in Python.  
This project simulates real-world banking operations such as account management, secure transactions, and banking system control.

---

## 📌 Project Overview

This system allows users to:
- Create and manage bank accounts
- Perform secure transactions (deposit & withdrawal)
- Authenticate using PIN-based security
- Maintain transaction history
- Manage multiple accounts through a central Bank system

The project focuses on **OOP design, encapsulation, and system-level thinking**.

---

## 🏗️ Project Structure
---

## ⚙️ Features

### 👤 Bank Account Features
- Create account with account number, name, balance, PIN
- Deposit money
- Withdraw money with PIN verification
- Check account balance securely
- Change PIN
- View transaction history

### 🏦 Bank System Features
- Store multiple accounts
- Search account by account number
- Delete accounts
- Prevent duplicate account creation
- Track total number of accounts (class variable)

---

## 🔐 Security Features
- PIN-based authentication for sensitive operations
- Encapsulation using private variables (`__balance`, `__pin`)
- Controlled access to account data
- Unauthorized access prevention

---

## 🧠 Object-Oriented Programming Concepts Used

### 1. Encapsulation
Sensitive data like balance and PIN are hidden using private variables and accessed only through methods.

### 2. Class & Object Design
- Each account is an independent object
- Bank acts as a controller for multiple objects

### 3. Class Interaction
- `Bank` class manages multiple `BankAccount` objects

### 4. Static/Class Variables
- `total_account` tracks total number of accounts created

---

## 🔄 System Workflow

1. Create a Bank object
2. Create BankAccount objects
3. Add accounts to Bank
4. Perform operations:
   - Deposit
   - Withdraw
   - Balance check
   - PIN change
   - Transaction history
5. Manage accounts via Bank system

---

## Banking-System/
│
├──`main.py`       # **program entry point (user interaction)**
├── `bank.py`          # **Bank class**
└── `account.py`       # **BankAccount class**

## 🖥️ How to Run

```bash
python main.py

