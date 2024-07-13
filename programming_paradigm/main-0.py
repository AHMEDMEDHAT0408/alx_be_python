import sys
from bank_account import BankAccount


def main():
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = params[0] if params else None

    if command == "deposit":
        if amount is None:
            print("Invalid amount provided.")
            sys.exit(1)
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount format.")
            sys.exit(1)
        account.deposit(amount)
    elif command == "withdraw":
        if amount is None:
            print("Invalid amount provided.")
            sys.exit(1)
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount format.")
            sys.exit(1)
        account.withdraw(amount)
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()
