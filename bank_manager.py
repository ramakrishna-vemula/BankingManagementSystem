from account import Account
from transaction import Transaction


class BankManager:

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            print("Creating BankManager Instance...")

            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):

        if not hasattr(self, "initialized"):

            self.bank_name = "ABC Bank"
            self.branch = "Hyderabad"

            self.accounts = {}
            self.next_acc_no = 1001

            self.transaction = Transaction()

            self.initialized = True

    # Create Account
    def create_account(self, name, balance):

        if balance < 0:
            print("Initial balance cannot be negative!")
            return

        acc = Account(self.next_acc_no, name, balance)

        self.accounts[self.next_acc_no] = acc

        print("\nAccount created successfully!")
        print("Account Number:", self.next_acc_no)

        self.next_acc_no += 1

    # Deposit
    def deposit(self, acc_no, amount):

        if acc_no in self.accounts:

            self.accounts[acc_no].deposit(amount)

            if amount > 0:
                self.transaction.add_transaction(
                    acc_no, "Deposit", amount
                )

        else:
            print("Account not found!")

    # Withdraw
    def withdraw(self, acc_no, amount):

        if acc_no in self.accounts:

            acc = self.accounts[acc_no]

            if amount > 0 and amount <= acc.balance:

                acc.withdraw(amount)

                self.transaction.add_transaction(
                    acc_no, "Withdrawal", amount
                )

            else:
                acc.withdraw(amount)

        else:
            print("Account not found!")

    # Check Balance
    def check_balance(self, acc_no):

        if acc_no in self.accounts:

            print("Available Balance: Rs.",
                  self.accounts[acc_no].balance)

        else:
            print("Account not found!")

    # Display Account
    def display_account(self, acc_no):

        if acc_no in self.accounts:
            self.accounts[acc_no].display()

        else:
            print("Account not found!")

    # Display All Accounts
    def display_all_accounts(self):

        print("\n----- ALL BANK ACCOUNTS -----")

        if not self.accounts:
            print("No accounts available.")

        else:
            for acc in self.accounts.values():
                acc.display()

    # Transaction History
    def transaction_history(self):

        self.transaction.display_history()

    # Bank Configuration
    def bank_configuration(self):

        print("\n----- BANK CONFIGURATION -----")
        print("Bank Name:", self.bank_name)
        print("Branch:", self.branch)
        print("Total Accounts:", len(self.accounts))