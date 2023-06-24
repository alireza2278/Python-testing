class Question:
    def __init__(self, q, a):
        self.q = q
        self.a = a


class ExamPaper:
    def __init__(self):
        self.question = Question("whats your name?", ["reza", "ali"])

    def __str__(self):
        return f"{self.question.q}\n{self.question.a}"


# ---------------------------------------------------------------


class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}:{self.number}"


class University:
    def __init__(self, students):
        self.students = students


st = [Student("nilo", 65), Student("hesam", 73), Student("nazi", 36)]
university = University(st)
for s in university.students:
    print(s)
