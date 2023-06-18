from datetime import datetime
from pprint import pprint
class Product:
    def __init__(self, product_name, price, off):
        self.product_name = product_name
        self.price = price
        self.off = off


class Comment:
    def __init__(self, product, name, description, like_count, dislike_count):
        self.product = product
        self.name = name
        self.description = description
        self.date = datetime.now()
        self.like = like_count
        self.dislike = dislike_count

    def show(self):
        pprint(f"product: {self.product}\n"
               f"name: {self.name}\n"
               f"description: {self.description}\n"
               f"date: {self.date}\n"
               f"like: {self.like} and dislike: {self.dislike}" )
