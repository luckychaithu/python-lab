class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def print_student_info(self):
        print(f"name: {self.name}, marks: {self.marks}")

s1 = Student("tillu", 92)
s1.print_student_info()
