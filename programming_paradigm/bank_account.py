class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")

# Main script
def main():
    account = BankAccount(250)  # Example starting balance

    command = "deposit"
    amount = 67.0

    if command == "deposit" and amount is not None:
        account.deposit(amount)
    elif command == "withdraw" and amount is not None:
        account.withdraw(amount)
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
