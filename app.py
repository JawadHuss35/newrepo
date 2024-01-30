class ATM:
    def __init__(self, balance=1000):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        else:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"


def main():
    atm = ATM()
    
    while True:
        print("\n===== ATM Simulator =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(f"Your balance: ${atm.check_balance()}")
        elif choice == '2':
            amount = float(input("Enter the deposit amount: $"))
            print(atm.deposit(amount))
        elif choice == '3':
            amount = float(input("Enter the withdrawal amount: $"))
            print(atm.withdraw(amount))
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-4).")


if __name__ == "__main__":
    main()
