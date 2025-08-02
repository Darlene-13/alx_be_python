class BankAccount:
    """A simple bank account class demonstrating OOP concepts."""
    
    def __init__(self, initial_balance=0):
        """Initialize a bank account with an optional initial balance."""
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        self.account_balance += amount
    
    def withdraw(self, amount):
        """
        Withdraw the specified amount if sufficient funds are available.
        Returns True if successful, False otherwise.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """Display the current account balance in a user-friendly format."""
        return f"Current Balance: ${self.account_balance:.2f}"