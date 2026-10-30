class Transaction:

    def __init__(self):
        self.history = []

    def add_transaction(self, acc_no, transaction_type, amount):

        record = (
            f"Account: {acc_no} | "
            f"{transaction_type}: Rs.{amount}"
        )

        self.history.append(record)

    def display_history(self):

        print("\n----- TRANSACTION HISTORY -----")

        if not self.history:
            print("No transactions available.")

        else:
            for record in self.history:
                print(record)