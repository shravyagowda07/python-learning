#Inheritance in Python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_student(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
class EngineeringStudent:
    def __init__(self,branch):
        self.branch = branch
    def display_branch(self):
        print(f"Branch:{self.branch}")
student = Student("Shravya",19)
student.display_student()
student1 = EngineeringStudent("CSE")
student1.display_branch()


class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, USN):
        super().__init__(name)
        self.usn = USN

class EngineeringStudent(Student):
    def __init__(self,name, USN,branch):
        super().__init__(name, USN)
        self.branch = branch
    def display_details(self):
        print(f"Name:{self.name}")
        print(f"USN:{self.usn}")
        print(f"Branch:{self.branch}")
s1 = EngineeringStudent("Shravya","1SH25CS01","CSE")
s1.display_details()