from Human import *
class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}\nRecord Book: {self.record_book}"

st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
print(st2)