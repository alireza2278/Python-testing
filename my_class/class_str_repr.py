class person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.first_name}' '{self.last_name}' {self.age})"

Person1 = person("alireza", "abdolmaleki", 24)
print(str(Person1))
print(repr(Person1))