#Polymorphism in Python
class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog says Woof!")
class Cat(Animal):
    def sound(self):
        print("Cat says meow!")
a = Animal()
a.sound()
d = Dog()
d.sound()
c = Cat()
c.sound()