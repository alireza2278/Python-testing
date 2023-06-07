from pprint import pprint


class UserList(list):
    def search(self, user_name):
        matching_user = []
        for user in self:
            if user_name in user.user_name:
                matching_user.append(user)
            return matching_user

    def append(self, obj) -> None:

        if not isinstance(obj, User):
            raise TypeError("this is only accepts User")
        return super().append(obj)

class User:
    All_users: list["User"] = UserList()

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


class Bayer(User):
    def __init__(self, user_name: str, email: str, password: str,phone) -> None:
        super().__init__(user_name,email,password)
        self.phone = phone

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.user_name!r}, {self.email!r}, " \
               f"{self.password!r}, {self.phone!r})"


def main() -> None:
    u1 = Bayer("alireza","email","pass","0918")
    li = UserList()
    li.append(4)
    print(li)
if __name__ == "__main__":
    main()