class BankAccount:
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self
    def display_account_info(self):
        self.display_account_info = self
        # print(f"My balance is {self.balance}, and my interest rate is {self.int_rate}")
account1 = BankAccount(.02,0)
account2 = BankAccount(.02,0)
account1.make_deposit(100).make_deposit(250).make_deposit(200).make_withdrawal(100).yield_interest().display_account_info()
# print(account1.balance)
account2.make_deposit(600).make_deposit(800).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).yield_interest().display_account_info()
# print(account2.balance)


class User:

    def __init__(self, name, email):
        self.name = name
        name = "Drew"
        self.email = email
        email = "thatguydrew@gmail.com"
        self.account = BankAccount(int_rate=.02, balance=0)
    def cust_deposit(self, amount):
        self.account.balance += amount
        return self
    def cust_withdrawal(self, amount):
        self.account.balance -= amount
        return self
    def display_cust_balance(self):
        print(f"Hello {self.name}, your balance is {self.account.balance}")

drew = User ("Drew", "thatguydrew@gmail.com")
drew.cust_deposit(300).cust_deposit(300).cust_withdrawal(100).display_cust_balance()

