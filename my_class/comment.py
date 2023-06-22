from datetime import datetime, timedelta


class Product:
    def __init__(self, product_name, price, off):
        self.product_name = product_name
        self.price = price
        self.off = off

    def __str__(self):
        return self.product_name


class Comment:
    website_name = "sabzlearn.ir"

    def __init__(self, product, name, description, like, dislike):
        self.product = product
        self.name = name
        self.description = description
        self.date = datetime.now()
        self.like = like
        self.dislike = dislike

    def show(self):
        print(f"product: {self.product}\n"
               f"name: {self.name}\n"
               f"description: {self.description}\n"
               f"date: {self.date}\n"
               f"like: {self.like} and dislike: {self.dislike}")

    @classmethod
    def info(cls):
        print(f"website name: {cls.website_name}")

    @classmethod
    def censorship(cls, product, name, description, like, dislike):
        print("The comment was censored!!!!")
        sc = description.replace("تخمی", "****")
        return cls(product, name, sc, like, dislike)

    @staticmethod
    def elapsed_time(time):
        print(datetime.now()-time)


python_course = Product("python expert", 0, 0)
c1 = Comment(python_course, "reza", "دوره تخمی و طولانی", 50, 7)
c1.show()
print(40 * "-")
Comment.info()
print(40 * "-")
c2 = Comment.censorship(python_course, "reza", "دوره تخمی و طولانی", 50, 7)
c2.show()
print(40 * "-")
Comment.elapsed_time(c2.date-timedelta(days=2, hours=4))
print(40 * "-")
