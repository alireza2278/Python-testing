from random import randrange
from typing import Set


class AccountBank:
    All_account_numbers: Set[int] = set()

    def __init__(self, name: str) -> None:
        self.account_number: int = 0
        while True:
            if (an := randrange(100, 1000)) not in AccountBank.All_account_numbers:
                AccountBank.All_account_numbers.add(an)
                self.account_number = an
                break
        self.name = name
        self.balance: float = 0

    def display(self):
        print(40 * "-")
        print(f"hi {self.name}\nyour current balance: {self.balance} Rl")
        print(40 * "-")

    def withdraw(self):
        amount = float(input("please enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            self.display()



    def deposit(self):
        amount = float(input("please enter amount to deposit: "))
        self.balance += amount
        self.display()


def main():
    acc1 = AccountBank("AlirezaAbdolmaleki")
    print("*"*40)
    print(f"account number: {acc1.account_number}")
    print("*" * 40)
    acc1.display()
    while True:
        choice = input("1: Show inventory\n2: deposit\n3: withdrow\n4: Exit\n\tyour choice: ")
        if choice == "1":
            acc1.display()
        elif choice == "2":
            acc1.deposit()
        elif choice == "3":
            acc1.withdraw()
        elif choice == "4":
            print("fuck you :/ ")
            break
        else:
            print("choice not True")


if __name__ == "__main__":
    main()
