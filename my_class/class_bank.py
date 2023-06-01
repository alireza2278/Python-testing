from random import randrange
from typing import List


class AccountBank:
    """
    Bank Account management.
    """
    All_account_numbers: List[int] = []
    Last_account_number: int = 999

    def __init__(self, name: str) -> None:
        AccountBank.Last_account_number += 1
        an = AccountBank.Last_account_number
        self.account_number = an
        AccountBank.All_account_numbers.append(an)
        self.name = name
        self.balance: float = 0

    def display(self):
        """
        show account balance.
        :return:
        """
        print(40 * "-")
        print(f"hi {self.name}\nyour current balance: {self.balance} Rl")
        print(40 * "-")

    def deposit(self) -> None:
        """
        Increace account balance.
        :return:
        """
        amount = float(input("please enter amount to deposit: "))
        self.balance += amount
        self.display()

    def withdraw(self) -> None:
        """
        withdrow from bank account.
        :return:
        """
        amount = float(input("please enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            self.display()


def main() -> None:
    acc1 = AccountBank("AlirezaAbdolmaleki")
    print("*"*40)
    print(f"account number: {acc1.account_number}")
    print("*" * 40)
    acc1.display()
    while True:
        choice = input("1: Show inventory\n2: deposit\n3: withdraw\n4: Exit\n\tyour choice: ")
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