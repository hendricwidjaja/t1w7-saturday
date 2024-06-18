class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposit successful! New balance: {self.__balance}"
        else: 
            return "Invalid deposit amount"
        
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdraw successful! New Balance: {self.__balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds!"
        
    def get_balance(self):
        return f"Account Balance: {self.__balance}"


# Create a bank account for John with an intial balance of $1000
john_account = BankAccount("John", 1000)

# Check balance
print("The balance in your acount is:", john_account.get_balance())

# Deposit money
print(john_account.deposit(500))

# Check balance again
print("The balance in your acount is:", john_account.get_balance())

# Withdraw money
print(john_account.withdraw(200))

# Withdraw more money than the balance
print(john_account.withdraw(2000))

# Experiment! This is becaue the function is not property encapsulated
john_account.__balance = -100
print(john_account.get_balance())