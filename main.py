class Bank_Account:

    def __init__(self):
        self.balance = 0
        print("KASPI")
    def deposit(self):
        balance = int(input("толыктыру суммасын енгиз: "))
        self.balance += balance
        print("тускен акша: ", balance)
    def withdraw(self):
        balance = int(input("неше шешу керек: "))
        self.balance -= balance
        print("кэш:",balance)


kowelek = Bank_Account()
kowelek.deposit()
kowelek.withdraw()
print("баланста:",kowelek.balance)