# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print('move')


#     def draw(self):
#         print('draw')


# Point = Point(10, 20)
# Point.x = 11
# print(Point.x)


# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()


# point2.x = Point()
# point2.x = 1
# print(point2.x)

# class Person:
#         def __init__(self, name):
#                 self.name = name
#         def talk(self):
#                 print(f'Hi, I am {self.name}')
# ibraheem = Person('Ibraheem Coder')
# ibraheem.talk()


# bob = Person("Omikunle Adisa")
# bob.talk()

# class User:
#     # Constructor
#     def __init__(self, name, email, age):
#         self.name = name
#         self.email = email
#         self.age = age
#
#     def greeting(self):
#         return f'My name is {self.name} and I am {self.age}'
#
#     def has_birthday(self):
#         self.age += 1


# Extend class

# class Customer(User):
#     Constructor
# def __init__(self, name, email, age):
#     self.name = name
#     self.email = email
#     self.age = age
#     self.balance = 0
#
# def set_balance(self, balance):
#     self.balance = balance
#
# def greeting(self):
#     return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

# Init user Object


# coder = User('Ibraheem Omikunle', 'ibraheemomikunle82@gmail.com', 20)
# Init customer object
# boss = Customer('Coder Javascript', 'Coder@yahoo.com', 25)
# boss.set_balance(800)
# print(boss.greeting())
#
#
# coder.has_birthday()
# print(coder.greeting())


# class Person:
#     def __init__(self.)

# class MyClass:
#   x = 5
#
# print(MyClass)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#
# p1 = Person("Omikunle", 80)

# print(p1.name)
# print(p1.age)


# class MyClass:
#   x = 5
# p1 = MyClass()
# print(p1.x)


# class Person:
#   def __init__(self, name, email, age):
#     self.name = name
#     self.email = email
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name + " Email is : " + self.email + " And am " + self.age + " years old.")


# p1 = Person("Ibraheem", "IbraheemOmikunle82@gmail.com", str(20))
# p1.myfunc()

# CLASSES AND BEHAVIOUR AND OBJECTS

# class Person1:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def code(self):
#         print(self.name + " is busy writing codes <>👨‍💻</>")

#     def teach(self):
#         print(f'Hello my name is  {self.name} and I am {self.age} years old ')


# ib = Person1('Ibraheem', 20)
# na = Person1('Brad', 40)

# print(ib.name + ' ' + str(ib.age))
# ib.code()
# ib.teach()

# print('-------------------------------------')

# print(na.name + ' ' + str(na.age))
# na.code()
# na.teach()


# class Me:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = Me("Ibraheem", 20)

# print(p1.name)
# print(p1.age)


# class Person5:
#         def __init__(self, name, age):
#             self.name = name
#             self.age = age

#         def myfunc(self):
#             print("Hello my name is " + self.name)

# p1 = Person5("John", 36)
# p1.myfunc()

# class Person9:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


#     def myfunc(self):
#         print("Hello my name is " + self.name)
# p1 = Person9("John", 36)

# p1.age = 40

# print(p1.age)


# class Dog(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.li = [1, 3, 4]

#         # print('Nice you made a dog! 🐕')


#     def speak(self):
#         print('hi i am ', self.name, 'and i am', self.age, 'years old')

#     def change_age(self, age):
#         self.age = age


#     def add_weight(self, weight):
#         self.weight = weight

# tim = Dog('tim 😀', 55)
# fred = Dog('fred 😆',3)
# tim.change_age(5)
# tim.add_weight(70)
# # tim.change_age(5)
# tim.speak()
# fred.speak()

# print(tim.age)
# print(tim.name)
# print(tim.li)
# print(fred.li)

# print(tim.weight)


# class Any:
#     def __init__(self,numAdd1,numAdd2):
#         self.firstAdd1 = numAdd1
#         self.firstAdd2 = numAdd2


#     def adddition(self):
#             print( self.firstAdd1 + self.firstAdd2)
#     def subtraction(self):
#             print( self.firstAdd1 - self.firstAdd2)
#     def multiply(self):
#             print( self.firstAdd1 * self.firstAdd2)
#     print('[A]-----------------------------------------')
# add = Any(10, 20)
# add.adddition() 


# print('[B]--------------------------------------------')

# sub = Any(80,20)
# sub.subtraction()


# print('[C}---------------------------------------------')
# mul = Any(16,8)
# mul.multiply()


# class Dog:
#         def __init__(self, name, age):
#                 self.name = name
#                 self.age = age
#                 # print(name)


#         def get_name(self):
#                 return self.name
#         # def add_one(self, x):
#         #         return x + 1
#         def get_age(self):
#                 return self.age

#         def set_age(self, age):
#                 self.age = age

#         # def bark(self):
#         #         print('bark')
# a = Dog('tim', 34)
# # print(a.name)
# a.set_age(23)
# # print(a.get_name())
# print(a.get_age())
# b3 = Dog('bill', 12)
# # print(b3.name)
# print(b3.get_name())
# print(b3.get_age())
# # d = Dog()
# # d.bark()
# # print(d.add_one(5))

# # print(type(d))


# class Customer:
#     def __init__(self, name, membership_type):
#         self.name = name
#         self.membership_type = membership_type
# print("customer created")
#
# def update_membership(self, new_membership):
#     print("Calculating costs")
#     self.membership_type = new_membership
#
# def __str__(self):
# print("converting to string")
# return self.name + " " + self.membership_type
#
# def print_all_customers(customers):
#         for customer in customers:
#                 print(customer)
#
# def __eq__(self, other):
#     if self.name == other.name and self.membership_type == other.membership_type:
#             return True
#
#     return False
#
# customers = [Customer("Caleb", "Gold"), Customer("Brad", "Bronze")]
# customers = [Customer("Ibraheem", "Coder"), Customer("Ibraheem", "Coder")]


# print(customers[0] == customers[1])
# print(id(customers[0]), id(customers[1]))
# Customer.print_all_customers(customers)
# print(customers[1])
# print(customers[1].membership_type)
# customers[1].update_membership("Gold")
# print(customers[1])
# print(customers[1].membership_type)
# customers[1].verified = False
# print(customers[0].name)
# print(customers[1].name)
# print(customers[1].verified)

# class Statistic:
#         def __init__(self, mean_num):
#                 self.mean_num = mean_num

#         def mean(self):
#                 return sum(self.mean_num)/4

#         def range_num(self):
#                 return max(self.mean_num) - min(self.mean_num)

# mean_num = Statistic([3, 4, 5, 6])

# print(f'The mean is = {mean_num.mean()}')
# print(f'The range is = {mean_num.range_num()}')

# class Get:
#     def __init__(self, getter1):
#         self.getter1 = getter1
#


#     def square_list(self):
#         square_root = [numbers ** 2 for numbers in self.getter1]
#         return square_root
#
#     def add_square(self):
#         add_the_square = [sum([numbers ** 2 for numbers in self.getter1])]
#         return add_the_square
#
#
# getter1 = Get([8, 7, 2, 5])
# print(getter1.square_list())
# print(getter1.add_square())
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade  # 0 - 100
#         def get_grade(self):
#             return self.grade

# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []
#
#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
#
#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#
#         return value / len(self.students)
#
#
# s1 = Course("Tim", 19, 55)
# s2 = Course("Bill", 19, 75)
# s3 = Course("Jill", 19, 65)
#
# course = Course("Science", 2)
# course.add_student(s1)
# course.add_student(s2)
# print(course.get_average_grade())
# # course.add_student(s3)


# class Calculator:
#
#     def __init__(self, num1, num2, num3, num4, num5, num6):
#         self.num1 = num1
#         self.num2 = num2
#         self.num3 = num3
#         self.num4 = num4
#         self.num5 = num5
#         self.num6 = num6
#
#     def getSum(self):
#         return (self.num1 + self.num2 + self.num3 + self.num4 + self.num5 + self.num6)
#
#     def getAverage(self):
#         number = self.num1, self.num2, self.num3, self.num4, self.num5, self.num6
#         x = len(number)
#         print(x)
#         return (self.getSum() / x)
#
#     def getOdd(self):
#         number = self.num1, self.num2, self.num3, self.num4, self.num5, self.num6
#         num_list = list(number)
#         # print(num_list)
#         odd = []
#         sumOdd = 0
#         for i in num_list:
#             # print(i)
#             if i % 2 != 0:
#                 # print("check {i}")
#                 odd.append(i)
#                 sumOdd += i
#
#         print(f"Odd Number {odd} and Total Sum of Odd Number {sumOdd}")
#         # return(odd)
#
#         # oddsum =0
#
#     def multiple(self):
#         num = self.num1, self.num2, self.num3, self.num4, self.num5, self.num6
#         num_list = list(num)
#
#         result = []
#         for multiple in num_list:
#             result.append(multiple * 2)
#
#         return (result)
#
#
# ans = Calculator(25, 30, 40, 47, 80, 45)
#
# print(f"Total Sum {ans.getSum()}")
# print(f"Average {ans.getAverage()}")
# ans.getOdd()
# print(f"Multiply by two {ans.multiple()}")
#
#
# class Calculator:
#
#     def __init__(self, num1, num2, num3, num4, num5, num6):
#         self.num1 = num1
#         self.num2 = num2
#         self.num3 = num3
#         self.num4 = num4
#         self.num5 = num5
#         self.num6 = num6
#
#     def getSum(self):
#         return (self.num1 + self.num2 + self.num3 + self.num4 + self.num5 + self.num6)
#
#     def getAverage(self):
#         number = self.num1, self.num2, self.num3, self.num4, self.num5, self.num6
#         x = len(number)
#         print(x)
#         return (self.getSum() / x)

#     def getOdd(self):
#         number = self.num1, self.num2, self.num3, self.num4, self.num5, self.num6
#         num_list = list(number)
#         # print(num_list)
#         odd = []
#         sumOdd = 0
#         for i in num_list:
#             # print(i)
#             if i % 2 != 0:
#                 # print("check {i}")
#                 odd.append(i)
#                 sumOdd += i
#
#         print(f"Odd Number {odd} and Total Sum of Odd Number {sumOdd}")
# return(odd)
#
# oddsum =0
#
#     def multiple(self):
#         num = self.num1, self.num2, self.num3, self.num4, self.num5, self.num6
#         num_list = list(num)
#
#         result = []
#         for multiple in num_list:
#             result.append(multiple * 2)
#
#         return (result)
#
#
# ans = Calculator(25, 30, 40, 47, 80, 45)
#
# print(f"Total Sum {ans.getSum()}")
# print(f"Average {ans.getAverage()}")
# ans.getOdd()
# print(f"Multiply by two {ans.multiple()}")


# class Calculator:
#
#     def __init__(self, num1, num2, num3, num4, num5, num6):
#         self.num1 = num1
#         self.num2 = num2
#         self.num3 = num3
#         self.num4 = num4
#         self.num5 = num5
#         self.num6 = num6
#
#     def getSum(self):
#         return (self.num1 + self.num2 + self.num3 + self.num4 + self.num5 + self.num6)
#
#     def getAverage(self):
#         number = self.num1, self.num2, self.num3, self.num4, self.num5, self.num6
#         x = len(number)
#         print(x)
#         return (self.getSum() / x)
#
#     def getOdd(self):
#         number = self.num1, self.num2, self.num3, self.num4, self.num5, self.num6
#         num_list = list(number)
#         # print(num_list)
#         odd = []
#         sumOdd = 0
#         for i in num_list:
#             # print(i)
#             if i % 2 != 0:
#                 # print("check {i}")
#                 odd.append(i)
#                 sumOdd += i
#
#         print(f"Odd Number {odd} and Total Sum of Odd Number {sumOdd}")
#         # return(odd)
#
#         # oddsum = 0
#
#     def multiple(self):
#         num = self.num1, self.num2, self.num3, self.num4, self.num5, self.num6
#         num_list = list(num)
#
#         result = []
#         for multiple in num_list:
#             result.append(multiple * 2)
#
#         return (result)
#
#
# ans = Calculator(25, 30, 40, 47, 80, 45)
#
# print(f"Total Sum {ans.getSum()}")
# print(f"Average {ans.getAverage()}")
# ans.getOdd()
# print(f"Multiply by two {ans.multiple()}")

#
# class Calculator:
#
#     def __init__(self, num1, num2, num3, num4, num5, num6):
#         self.num1 = num1
#         self.num2 = num2
#         self.num3 = num3
#         self.num4 = num4
#         self.num5 = num5
#         self.num6 = num6
#
#     def getSum(self):
#         return (self.num1 + self.num2 + self.num3 + self.num4 + self.num5 + self.num6)
#
#     def getAverage(self):
#         number = self.num1, self.num2, self.num3, self.num4, self.num5, self.num6
#         x = len(number)
#         print(x)
#         return (self.getSum() / x)
#
#     def getOdd(self):
#         number = self.num1, self.num2, self.num3, self.num4, self.num5, self.num6
#         num_list = list(number)
#         # print(num_list)
#         odd = []
#         sumOdd = 0
#         for i in num_list:
#             # print(i)
#             if i % 2 != 0:
#                 # print("check {i}")
#                 odd.append(i)
#                 sumOdd += i
#
#         print(f"Odd Number {odd} and Total Sum of Odd Number {sumOdd}")
#         # return(odd)
#
#         # oddsum =0
#
#     def multiple(self):
#         num = self.num1, self.num2, self.num3, self.num4, self.num5, self.num6
#         num_list = list(num)
#
#         result = []
#         for multiple in num_list:
#             result.append(multiple * 2)
#
#         return (result)
#
#     def getPrime(self):
#         number = self.num1, self.num2, self.num3, self.num4, self.num5, self.num6
#
#         prime_list = list(number)
#         result = []
#
#         for i in prime_list:
#             count = 0
#             print("Count {}".format(count))
#             for j in range(1,int(i)):
#                 if i % j == 0:
#                     count += 1
#             if count == 1:
#                 result.append(i)
#
#         return ("Prime number = {}".format(result))
#
#
# ans = Calculator(25, 30, 40, 47, 80, 13)
#
# print(ans.getPrime())
# print(f"Total Sum {ans.getSum()}")
# print(f"Average {ans.getAverage()}")
# ans.getOdd()
# print(f"Multiply by two {ans.multiple()}")


# class Statistics:
#     def __init__(self, arr):
#         self.arr = arr
#
#     def getMean(self):
#         sum_num = sum(self.arr)
#         # print("Sum = {}".format(sum_num))
#         lent_num = len(self.arr)
#         # print("Length {}".format(lent_num))
#         print(f"Mean = {sum_num / lent_num}")
#
#
#     def getMedian(self):
#         median_num = self.arr
#         media_sort = sorted(median_num)
#         print("Sort List = {} ".format(media_sort))
#         lenArr = len(self.arr)
#         if (lenArr % 2 == 0):
#
#             indexone = lenArr // 2
#             indextwo = indexone - 1
#
#             firstvalue = media_sort[int(indexone)]
#
#             secondvalue = media_sort[int(indextwo)]
#
#             result = firstvalue + secondvalue
#
#             print("Median = {}".format(result//2))
#
#         else:
#             middleindex = lenArr // 2
#
#             middlevalue = media_sort[int(middleindex)]
#
#             print("Median = {}".format(middlevalue))
#
#
#
# answer = Statistics([8, 7, 2, 5, 9, 10, 15, 18])
# answer.getMean()
# answer.getMedian()

# class Finder:
#     def __init__(self, findIt):
#         self.findIt = findIt
#
#     def getMode(self):
#         mode_num = self.findIt
#         b = list(mode_num)
#         my_dict = {}
#
#         for i in range(len(b)):
#             if b[i] not in my_dict:
#                 x = b.count(b[i])
#         print(my_dict.update({b[i]:x}))
#
#     a = Finder([40, 12, 70, 2, 3, 3, 56, 56, 56, 56])
#     a.getMode()

# class Finder:
#     def __init__(self, findIt):
#         self.findIt = findIt

#     def getmode(self):
#         mode_num = self.findIt
#         nums = {}
#         for number in mode_num:
#             nums.setdefault(number, 0)
#             nums[number] += 1
#         hightestOccur = max(nums.values())
#         highestAppear = []
#         for number, appear in nums.items():
#             if appear == hightestOccur:
#                 highestAppear.append(number)

#         return highestAppear


# a = Finder([40, 12, 70, 2, 3, 3, 3, 3, 3, 56, 56, 56, 56])
# print(f"mode is = {a.getmode()}")


# class Vehicle:

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         # self.color = color
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"


# class Bus(Vehicle):
#     def seating_capacity(self, capacity=80):
#         return super().seating_capacity(capacity=80)


# school_bus = Bus("school Volvo", 180, 12)
# print(school_bus.seating_capacity())


# school_bus = Bus("School Volvo,", "Light-Green,", 180, 12)
# print("Vehicle Name:", school_bus.name, "Color:", school_bus.color,  "Speed:", school_bus.max_speed,","   "Mileage:", school_bus.mileage,",")
# class S


# def getMode(self):
#     dict_value = {}
#     final = []
#     for i in self.arr:
#         if (i not in dict_value):
#             dict_value.update({i:self.arr.count()})

#     max_value = max(dict_value.values())

#     for key, val in dict_value.items():
#         if (val == max_value):
#             final.append(key)
#     print("Mode = {}".format(final))


# class Mammal:
#     def walk(slef):
#         print('walk')


# class Dog(Mammal):
#     pass


# class Cat(Mammal):
#     pass


# dog1 = Dog()
# dog1.walk()


# class Dog(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age


#     def speak(self):
#         print('hi i am ', self.name, 'and i am', self.age, 'years old')

#     def talk(self):
#         print('Bark! 🐶')


# class Cat(Dog):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color
#         # self.name = 'tech'

#     def talk(self):
#             print('Meow! 🐱')

# jim = Dog('jim', 70)
# jim.talk()

# tim = Cat('tim', 5, 'blue')
# # tim.talk()
# tim.speak()


# class Cat(object):
#     def __init__(self,name,age,color):
#         self.name = name
#         self.age = age
#         self.color = color


#     def speak(self):
#         print('hi i am ', self.name, 'and i am', self.age, 'years old')


# tim.talk()


# General class

# class Vehicle():
#     def __init__(self, price, gas, color):
#         self.price = price
#         self.gas = gas
#         self.color = color
#
#     def fillUpTank(self):
#         self.gas = 100
#
#     def emptyTank(self):
#         self.gas = 0
#
#     def gasLeft(self):
#         return self.gas
#
#
# class Car(Vehicle):
#     def __init__(self, price, gas, color, speed):
#         super().__init__(price, gas, color)
#         self.speed = speed
#
#     def beep(self):
#         print('Beep beep 🚘')
#
#
# class Truck(Vehicle):
#     def __init__(self, price, gas, color, tiers):
#         super().__init__(price, gas, color)
#         self.tiers = tiers
#
#     def beep(self):
#         print('Honk Honk 🚚')

# # Class
# class SoftwareEngineer:
#
#     # class attribute
#     alias = "Code Salayer"
#
#     def __init__(self, name, age, level, salary):
#         # Instance attributes
#         self.name = name
#         self.age = age
#         self.level = level
#         self.salary = salary


# Instance
# se1 = SoftwareEngineer("Ibraheem", 20, "Junior", 5000)
# print(se1.name, se1.age)

# print(se1.alias)
# print(SoftwareEngineer.alias)
# se2 = SoftwareEngineer("Brad", 40, "Senior", 7000)
# print(se2.alias)


# OOP

# class PlayerCharacter:
#     membership = True
#     def __init__(self, name, age):
#             self.name = name
#             self.age = 'age'
#
#     def shout(self):
#         print(f'My name is {self.name}')
#
#     @classmethod
#     def adding_things(cls, num1, num2):
#         return num1 + num2
#
#
# player1 = PlayerCharacter("Ibraheem", 21)
# player2 = PlayerCharacter("Coder", 20)
# player2.attack = 50


# print(player1.adding_things(8,8))
# print(PlayerCharacter.adding_things(23,45))

# print(player2.shout())

# print(player2.attack)
# print(player1.name)


# Encapsulation
# class Example:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def test(self):
#         print('Testing')
#
#     def speak(self):
#         print(f'my name is {self.name}, and i am {self.age} years old.')
#
#
# speaker = Example('Ibraheem', 20)
# print(speaker.name)
# print(speaker.age)
# speaker1 = {'name': 'Ibraheem', 'age': 20}
# print(speaker1['name'])
# print(speaker1['age'])
# # speaker.speak()


# Abstraction
# class Example:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def test(self):
#         print('Testing')
#
#     def speak(self):
#         print(f'my name is {self.name}, and i am {self.age} years old.')
#
#
# speaker = Example('Ibraheem', 20)
# speaker.speak()
#
#
# Inheritance
# class User(object):
#     def sign_in(self):
#         print('logged in')
#
#
# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#
#     def attack(self):
#         print(f'attacking with power of {self.power}')
#
#
# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows
#
#     def attack(self):
#         print(f'attacking with arrows: arrows left- {self.num_arrows}')
#
#
# wizard1 = Wizard('Merlin', 50)
# print(isinstance(wizard1, object))
# print(isinstance(wizard1, User))
#
# archer1 = Archer('Robin', 500)
# wizard1.attack()
# # archer1.attack()
# #
# # # Polymorphism#
# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#
#     def attack(self):
#         print(f'attacking with power of {self.power}')
#
#
# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows
#
#     def attack(self):
#         print(f'attacking with arrows: arrows left- {self.num_arrows}')
#
#
# wizard1 = Wizard('Merlin', 50)
# print(isinstance(wizard1, object))
# # print(isinstance(wizard1, User))
#
# archer1 = Archer('Robin', 30)
#
# def player_attack(char):
#     char.attack()
#
# player_attack(wizard1)
# player_attack(archer1)
#
#
# class User(object):
#     def __init__(self, email):
#         self.email = email
#
#     def sign_in(self):
#         print('Ok')
#
#
#
#
# class Wizard(User):
#     def __init__(self, name, power, email):
#         User.__init__(self, email)
#         self.name = name
#         self.power = power
#
#     def attack(self):
#         User.attack(self)
#         print(f'attacking with the power of {self.power}')
#
#
# wizard = Wizard('Merlin', 60, 'merlin@gmail.com')
# # print(wizard.sign_in())
# print(wizard.email)


# Using a super function
# class User(object):
#     def __init__(self, email):
#         self.email = email
#
#     def sign_in(self):
#         print('Ok')
#
#
#
#
# class Wizard(User):
#     def __init__(self, name, power, email):
#         super().__init__(email)
#         self.name = name
#         self.power = power
#
#     def attack(self):
#         User.attack(self)
#         print(f'attacking with the power of {self.power}')
#
#
# wizard = Wizard('Merlin', 60, 'merlin@gmail.com')
# # print(wizard.sign_in())
# print(wizard.email)


# Introspection it is use to determine type of an object when the code is running
# class User(object):
#     def __init__(self, email):
#         self.email = email
#
#     def sign_in(self):
#         print('Ok')
#
# class Wizard(User):
#     def __init__(self, name, power, email):
#         super().__init__(email)
#         self.name = name
#         self.power = power
#
#     def attack(self):
#         User.attack(self)
#         print(f'attacking with the power of {self.power}')
#
# # Introspection
# wizard = Wizard('Merlin', 60, 'merlin@gmail.com')
# # print(wizard.sign_in())
# print(dir(wizard))


# Dunder Methods or magic methods: they allow us to use python specific functions on object created to our class

# class Toy():
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age
#         self.my_dict = {
#             'name': 'Yoyo',
#             'has_pets': False
#         }
#
#     def __str__(self):
#         return f'{self.color}'
#
#     def __len__(self):
#         return 5
#
#
#     # def __del__(self):
#     #     print('deleted')
#
#
#     # def __call__(self):
#     #     return ('Yes')
#
#
#     def __getitem__(self, i):
#         return self.my_dict[i]
#
# action_figure = Toy('red', 0)
# # print(action_figure.__str__())
# # print(str(action_figure))
# # print(str('action_figure'))
# # print(len(action_figure))
# # del action_figure
# # print(action_figure())
# print(action_figure['name'])
#
#
# class SuperList(list):
#     def __len__(self):
#         return 1000
#
# super_list1 = SuperList();
#
#
# print(len(super_list1))
# super_list1.append(5)
# print(super_list1[0])
# print(super_list1)

# print(issubclass(SuperList, list))
# print(issubclass(list, object))

# Multiple Inheritance

# class User(object):
#     def sign_in(self):
#         print('logged in')
#
# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#
#     def attack(self):
#         print(f'attacking with the power of {self.power}')
#
# class Archer(User):
#     def __init__(self, name, arrows):
#         self.name = name
#         self.arrows =arrows
#
#     def check_arrows(self):
#         print(f'{self.arrows} remaining')
#
#     def run(self):
#         print('ran really fast')
#
#
# class HybridBorg(Wizard, Archer):
#     def __init__(self, name, power, arrows):
#         Archer.__init__(self, name, arrows)
#         Wizard.__init__(self, name, power)

# hb1 = HybridBorg('borgie', 50, 100)
# print(hb1.run())
# print(hb1.attack())
# print(hb1.check_arrows())
# print(hb1.sign_in())

# class SoftwareEngineer:
#
#     def __init__(self, name, age):
#         # Instance attributes
#         self.name = name
#         self.age = age
#         self._salary = 8000
#         self._num_bugs_solved = 0
#
#     def  code(self):
#         self._num_bugs_solved += 1
#
#     def get_salary(self):
#         return self._salary
#
#     def set_salary(self, value):
#         if value < 1000:
#             self._salary = 1000
#         if value > 20000:
#             self._salary = 20000
#         self._salary = value
#
#
#     def _calculate_salary(self, base_value):
#         if self._num_bugs_solved <
#
# se = SoftwareEngineer("Ibraheem", 20)
# print(se.age, se.name, se._salary)
#
# se.set_salary(6000)
# print(se.get_salary())

# class Myclass:
#     x = 5
#
# p1 = Myclass()
# print(p1.x)
#
#

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# # name = input('Enter your name: ')
# # age  = input('Enter your age: ')
# # p1 = Person(name, age)
# p1 = Person("Ibraheem", 20)
# # del p1
# # print(p1)
# # print(p1.name)
# # print(p1.age)


class Student():
    name: "Ibraheem"
    age: 20
    gender: "male"
