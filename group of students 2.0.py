class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}\nGender: {self.gender}\nAge: {self.age}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}\nRecord Book: {self.record_book}"


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise Exception("Group size limit reached")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Number: {self.number}\n{all_students}"


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 26, 'Liza', 'Taylor2', 'AN145')
st4 = Student('Female', 27, 'Liza', 'Taylor3', 'AN145')
st5 = Student('Female', 28, 'Liza', 'Taylor4', 'AN145')
st6 = Student('Female', 29, 'Liza', 'Taylor5', 'AN145')
st7 = Student('Female', 22, 'Liza', 'Taylor6', 'AN145')
st8 = Student('Female', 21, 'Liza', 'Taylor7', 'AN145')
st9 = Student('Female', 20, 'Liza', 'Taylor8', 'AN145')
st10 = Student('Female', 35, 'Liza', 'Taylor9', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
#print(gr)

try:
    st11 = Student('male', 31, 'Steve', 'Jobs2', 'AN145')
    gr.add_student(st11)
except Exception as e:
    print(e)
