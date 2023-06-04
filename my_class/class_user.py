from pprint import pprint


class UserList(list):
    def search(self, user_name):
        matching_user = []
        for user in self:
            if user_name in user.user_name:
                matching_user.append(user)
            return matching_user

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


def main() -> None:
    u1 = User("ali", "e", "1")
    u2 = User("reza", "g", "2")
    u3 = User("ali01", "e1", "3")
    u4 = User("sasan66", "e1", "3")
    pprint(User.All_users.search("ali"))
if __name__ == "__main__":
    main()
