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

    def __init__(self, user_name: str, email: str, password: str, **kwargs) -> None:
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
    def __init__(self, shaba, **kwargs):
        super().__init__(**kwargs)
        self.shaba = shaba

    def order(self,order:"order")->None:
        print(f"from your products{order} was sold!")


class Bayer(User):
    def __init__(self, phone,**kwargs) -> None:
        super().__init__(**kwargs)
        self.phone = phone

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.user_name!r}, {self.email!r}, " \
               f"{self.password!r}, {self.phone!r})"


class SellerAndBayer(Seller, Bayer):
    def __init__(self,score,**kwargs):
        super().__init__(**kwargs)
        self.score = score


def main() -> None:
   b = Bayer(user_name="alireza",email="alirezaabdolmaleki2278@gmail.com",password="1234",phone="09188108836")
   s = Seller(user_name="reza",email="alirezaabdolmaleki2279@gmail.com",password="4321",shaba="123456789")
   sb = SellerAndBayer(user_name="sasan",email="@email",password="8585",phone="0912",shaba="5695",score="0")
   pprint(User.All_users)
if __name__ == "__main__":
    main()
