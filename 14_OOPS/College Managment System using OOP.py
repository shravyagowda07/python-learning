#College Managment System
from abc import ABC
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def calculate_result(self):
        pass
    def display_details(self):
        pass
class Student(Person):
    def __init__(self, name, age, branch, marks):
        super().__init__(name, age)
        self.branch = branch
        self.__marks = marks
    def get_marks(self):
        return self.__marks
    def calculate_result(self):
        if self.__marks >= 40:
            return "Pass"
        else:
            return "Fail"
    def display_details(self):
        print("--Student Details--")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)
        print("Marks:", self.__marks)
        print("Result:", self.calculate_result())
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def display_details(self):
        print("--Teacher Details--")
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Subject:{self.subject}")
student = Student("Shravya", 19, "CSE",90)
teacher = Teacher("anitha",35, "Python")   
student.display_details()
print()
teacher.display_details()
print()
