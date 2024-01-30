class ATM:
    def _init_(self):
        # Dictionary to store account information (account number, PIN, balance)
        self.accounts = {
            '1234567890': {'pin': '1234', 'balance': 1000.0},
            '0987654321': {'pin': '4321', 'balance': 500.0}
        }
        self.current_account = None

    def display_menu(self):
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")

    def authenticate_user(self, account_number, pin):
        if account_number in self.accounts and self.accounts[account_number]['pin'] == pin:
            self.current_account = account_number
            return True
        else:
            return False

    def check_balance(self):
        return f"Your balance is ${self.accounts[self.current_account]['balance']}"

    def deposit(self, amount):
        self.accounts[self.current_account]['balance'] += amount
        return f"${amount} has been deposited. Your new balance is ${self.accounts[self.current_account]['balance']}"

    def withdraw(self, amount):
        if amount <= self.accounts[self.current_account]['balance']:
            self.accounts[self.current_account]['balance'] -= amount
            return f"${amount} has been withdrawn. Your new balance is ${self.accounts[self.current_account]['balance']}"
        else:
            return "Insufficient funds. Withdrawal failed."

# Example Usage
if _name_ == "_main_":
    atm = ATM()

    while True:
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")

        if atm.authenticate_user(account_number, pin):
            print("Authentication successful.")
            break
        else:
            print("Invalid account number or PIN. Please try again.")

    while True:
        atm.display_menu()
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            print(atm.check_balance())
        elif choice == '2':
            amount = float(input("Enter the deposit amount: "))
            print(atm.deposit(amount))
        elif choice == '3':
            amount = float(input("Enter the withdrawal amount: "))
            print(atm.withdraw(amount))
        elif choice == '4':
            print("Exiting ATM. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
