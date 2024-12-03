class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number  
        self.__balance = balance  # Private attribute

    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    
    def get_balance(self):
        return self.__balance

    def display_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: ${self.__balance}")


account = BankAccount("123456789", 500)
account.deposit(200)
account.withdraw(100)
account.display_account_info()
