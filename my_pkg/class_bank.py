from random import randrange

class Account_Banc:
    All_account_numbers = set()
    def __init__(self, name):
        self.account_number = 0
        while True:
            if (an := randrange(100,1000)) not in Account_Banc.All_account_numbers:
                Account_Banc.All_account_numbers.add(an)
                self.account_number = an
                break
        self.name = name
        self.balance = 0

    def display(self):
        print(f"hi {self.name}\nyour current balance: {self.balance}")

account_1 = Account_Banc("hadis")
account_1.display()
