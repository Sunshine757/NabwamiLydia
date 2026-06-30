#Real world bank account
#real world bank account(balance, deposit)
class Bank_account:
    def __init__(self):
        self.__balance = 1000000

    def deposit(self, amount):
        self._balance += amount

    def show_balance(self):
        return self.__balance

acc = Bank_account()
acc.deposit(50000)
print(acc.show_balance())

