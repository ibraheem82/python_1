class Person:
    def __init__(self, fname, lname):
          self.fname = fname
          self.lname = lname
    def getFullname(self):
        print("My full Name is:", self.fname, self.lname)

class Student(Person):
    pass

# Class work inheriance class
class School:
    pass

class Vehicles:
    def __init__(self, Car, Speed, Distance):
        self.Car = Car
        self.Speed = Speed
        self.Distance = Distance

    def carFeatures(self, color = "blue"):
        print("I own a", color, self.Car, "has the max-speed", self.Speed, "it can covers", self.Distance, "in a day.")

class Bus(Vehicles):
   pass

class Van(Vehicles):
   pass


