from dataclasses import dataclass, InitVar


@dataclass
class Person:
    name: str
    family: str
    age: int
    gender: InitVar[str]

    def __post_init__(self, gender):
        if self.age < 0:
            self.age = 0
        if gender == "man":
            self.name += "*"


p = Person("alireza", "abdolmaleki", 24, "man")
print(p)
p.name = "sasan"
print(p)
