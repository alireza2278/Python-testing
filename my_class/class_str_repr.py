class Person:
    def __init__(self, first_name, last_name, age, national_code):
        self.first_name = first_name
        self.last_name = last_name
        self.national_code = national_code
        self.age = age

    def __add__(self, other_person):
        return self.age + other_person.age

    def __lt__(self, other_person):
        return self.age < other_person.age

    def __eq__(self, other_person):
        return self.national_code == other_person.national_code

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.first_name}' '{self.last_name}' {self.age} {self.national_code})"


person1 = Person("alireza", "abdolmaleki", 24, 3977646921)
person2 = Person("hamed", "abdolmaleki", 28, 5834758372)

print(str(person1))
print(repr(person1))
print(person1 == person2)