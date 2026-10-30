class Account:

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):

        if amount <= 0:
            print("Invalid deposit amount!")
        else:
            self.balance += amount
            print("Amount deposited successfully!")

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdrawal amount!")

        elif amount > self.balance:
            print("Insufficient balance!")

        else:
            self.balance -= amount
            print("Amount withdrawn successfully!")

    def display(self):

        print("\n----- ACCOUNT DETAILS -----")
        print("Account Number:", self.acc_no)
        print("Account Holder:", self.name)
        print("Balance: Rs.", self.balance)