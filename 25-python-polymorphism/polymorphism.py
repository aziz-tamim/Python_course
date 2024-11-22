x = "Hello World!"
print(len(x))


mytuple = ("apple", "banana", "cherry")
print(len(mytuple))


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
print(len(thisdict))


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive!")
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Sail!")
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Fly!")
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")
for x in (car1, boat1, plane1):
    x.move()


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move!")
class Car(Vehicle):
    pass
class Boat(Vehicle):
    def move(self):
        print("sail!")
class Plane(Vehicle):
    def move(self):
        print("Fly!")
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")
for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()
