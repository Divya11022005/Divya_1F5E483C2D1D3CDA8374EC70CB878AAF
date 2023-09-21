class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance is ${self.__account_balance}"
        else:
            return "Invalid deposit amount. Amount must be greater than 0."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. New balance is ${self.__account_balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount. Amount must be greater than 0."
        else:
            return "Insufficient balance."

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}"

my_account = BankAccount("123456789", "John Doe", 1000)


print(my_account.display_balance())
print(my_account.deposit(500))
print(my_account.withdraw(200))
print(my_account.withdraw(1500))