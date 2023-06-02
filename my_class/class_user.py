from pprint import pprint
class User:
    All_users: list["User"] = []

    def __init__(self, user_name: str, email: str, password: str) -> None:
        self.user_name = user_name
        self.email = email
        self.password = password
        User.All_users.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.user_name!r}, {self.email!r}, " \
               f"{self.password!r})"

    def __str__(self):
        return self.user_name


class Seller(User):
    def order(self,order:"order")->None:
        print(f"from your products{order} was sold!")


def main() -> None:
    ali = User("ali","gmail","8585")
    reza = Seller("reza","email","9595")
    sasan = User("sasan","gmail2","7575")
    ahmad = Seller("ahmad","email2","1000")
    print("user:",ali.user_name,ali.email)
    print("saler:",reza.user_name, reza.email)
    reza.order("book")



if __name__ == "__main__":
    main()
