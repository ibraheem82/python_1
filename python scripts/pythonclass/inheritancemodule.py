from inheritance import Student
from inheritance import Vehicles, Bus, Van

name = Student("John", "Okon")
name.getFullname()

myCar = Vehicles("BMW","200km/h", "500km" )
myCar.carFeatures()

Buses = Bus("Hiace", "150km/h", "300km")
Buses.carFeatures() 

Lorry = Van("Truck", "100km/h", "200km")
Lorry.carFeatures() 