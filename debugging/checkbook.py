class Checkbook:
    """
    A simple checkbook class to manage a bank balance.
    """
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """Adds a specified amount to the balance."""
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """Subtracts a specified amount if funds are available."""
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Prints the current balance."""
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        
        if action.lower() == 'exit':
            break
            
        elif action.lower() in ['deposit', 'withdraw']:
            try:
                # This is where the error handling happens
                amount_input = input("Enter the amount: $")
                amount = float(amount_input)
                
                if amount < 0:
                    print("Error: Amount cannot be negative.")
                    continue
                
                if action.lower() == 'deposit':
                    cb.deposit(amount)
                else:
                    cb.withdraw(amount)
                    
            except ValueError:
                # If float() fails, this block catches the error
                print("Invalid input: Please enter a numeric value (e.g., 10.50).")
                
        elif action.lower() == 'balance':
            cb.get_balance()
            
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
