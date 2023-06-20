from datetime import datetime
class Product:
    def __init__(self, product_name, price, off):
        self.product_name = product_name
        self.price = price
        self.off = off

    def __str__(self):
        return self.product_name


class Comment:
    website_name = "sabzlearn.ir"

    def __init__(self, product, name, description, like_count, dislike_count):
        self.product = product
        self.name = name
        self.description = description
        self.date = datetime.now()
        self.like = like_count
        self.dislike = dislike_count

    def show(self):
        print(f"product: {self.product}\n"
               f"name: {self.name}\n"
               f"description: {self.description}\n"
               f"date: {self.date}\n"
               f"like: {self.like} and dislike: {self.dislike}" )
    @classmethod
    def info(cls):
        print(f"website name: {cls.website_name}")

python_course = Product("python expert", 0, 0)
c1 = Comment(python_course, "reza", "دوره تخمی و طولانی", 50, 7)
c1.show()
Comment.info()