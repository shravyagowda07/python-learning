#Method Overriding
class Vehicle:
    def start(self):
        print("Vehicle started!")
class Car(Vehicle):
    def start(self):
        print("Car starts with a key/button.")
class Bike(Vehicle):
    def start(self):
        print("Bike starts with a key/button.")
c = Car()
c.start()
b = Bike()
b.start()