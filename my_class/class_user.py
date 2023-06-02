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

def main() -> None:


if __name__ == "__main__":
    main()
