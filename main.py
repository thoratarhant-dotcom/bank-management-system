from account import BankAccount
from bank import Bank

bank = Bank("MyBank")

while True:
    print("\n========== BANK MENU ==========")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Change PIN")
    print("6. Transaction History")
    print("7. Delete Account")
    print("8. Exit")
    print("================================")

    try:
        choice = int(input("Enter choice: "))
    except:
        print("Invalid input! Enter a number.")
        continue

    # 1. CREATE ACCOUNT
    if choice == 1:
        accntNum = int(input("Enter Account Number: "))
        Name = input("Enter Name: ")
        balance = int(input("Enter Initial Balance: "))
        PIN = int(input("Set PIN: "))

        acc = BankAccount(accntNum, Name, balance, PIN)
        bank.createAccount(acc)

    # 2. DEPOSIT
    elif choice == 2:
        acc_no = int(input("Enter Account Number: "))
        acc = bank.findAccount(acc_no)

        if acc:
            amt = int(input("Enter Amount to Deposit: "))
            acc.deposit(amt)
        else:
            print("Account not found!")

    # 3. WITHDRAW
    elif choice == 3:
        acc_no = int(input("Enter Account Number: "))
        acc = bank.findAccount(acc_no)

        if acc:
            pin = int(input("Enter PIN: "))
            amt = int(input("Enter Amount to Withdraw: "))
            acc.withDraw(pin, amt)
        else:
            print("Account not found!")

    # 4. CHECK BALANCE
    elif choice == 4:
        acc_no = int(input("Enter Account Number: "))
        acc = bank.findAccount(acc_no)

        if acc:
            pin = int(input("Enter PIN: "))
            acc.checkBalance(pin)
        else:
            print("Account not found!")

    # 5. CHANGE PIN
    elif choice == 5:
        acc_no = int(input("Enter Account Number: "))
        acc = bank.findAccount(acc_no)

        if acc:
            old_pin = int(input("Enter Old PIN: "))
            new_pin = int(input("Enter New PIN: "))
            acc.changePin(old_pin, new_pin)
        else:
            print("Account not found!")

    # 6. TRANSACTION HISTORY
    elif choice == 6:
        acc_no = int(input("Enter Account Number: "))
        acc = bank.findAccount(acc_no)

        if acc:
            pin = int(input("Enter PIN: "))
            history = acc.showTransaction_history(pin)

            if isinstance(history, list):
                print("\n--- Transaction History ---")
                for t in history:
                    print(t)
            else:
                print(history)
        else:
            print("Account not found!")

    # 7. DELETE ACCOUNT
    elif choice == 7:
        acc_no = int(input("Enter Account Number: "))
        bank.deleteAccount(acc_no)

    # 8. EXIT
    elif choice == 8:
        print("Exiting Banking System... Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1-8.")

















































