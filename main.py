from bank_manager import BankManager


# Creating Singleton Object
bank1 = BankManager()

while True:

    print("\n================================")
    print("       ABC BANK MANAGEMENT")
    print("================================")

    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Display Account")
    print("6. Display All Accounts")
    print("7. Transaction History")
    print("8. Bank Configuration")
    print("9. Verify Singleton")
    print("10. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':

        name = input("Enter customer name: ")
        balance = float(input("Enter initial balance: "))

        bank1.create_account(name, balance)

    elif choice == '2':

        acc_no = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: "))

        bank1.deposit(acc_no, amount)

    elif choice == '3':

        acc_no = int(input("Enter account number: "))
        amount = float(input("Enter withdrawal amount: "))

        bank1.withdraw(acc_no, amount)

    elif choice == '4':

        acc_no = int(input("Enter account number: "))

        bank1.check_balance(acc_no)

    elif choice == '5':

        acc_no = int(input("Enter account number: "))

        bank1.display_account(acc_no)

    elif choice == '6':

        bank1.display_all_accounts()

    elif choice == '7':

        bank1.transaction_history()

    elif choice == '8':

        bank1.bank_configuration()

    elif choice == '9':

        bank2 = BankManager()
        bank3 = BankManager()

        print("\n----- SINGLETON VERIFICATION -----")

        print("Bank1 ID:", id(bank1))
        print("Bank2 ID:", id(bank2))
        print("Bank3 ID:", id(bank3))

        print("Bank1 and Bank2 same:", bank1 is bank2)
        print("Bank2 and Bank3 same:", bank2 is bank3)

        print("\nOnly one BankManager instance exists!")

    elif choice == '10':

        print("Thank you for using ABC Bank!")
        break

    else:

        print("Invalid choice! Please try again.")