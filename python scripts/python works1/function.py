# '''
# # You can pass an integer, all you need to do is to convert it into a string str()
# # A function can also take in parameters, You can pass anything you want into a function
# # A function is basically a collection of codes which perform a specific tasks
# '''


# def say_hi1(name, age):
#     print(f'Hello {name}, you are {age} years old')


# # print("top")
# say_hi1("Ibraheem", "20")
# say_hi1("Omikunle", "60")
# # print("bottom")


# def say_hi2(name, age):
#     print(f'Hello {name}, you are {age} years old')


# say_hi2("Abdullahi", 18)
# say_hi2("Samuel", 24)


# def say_hi3(name, age):
#     print('Hello ' + name, 'you are ' + str(age))


# say_hi3("Micheal", "35")
# say_hi3("John", "70")


# def cube(num):
#     return num*num*num


# print(cube(4))
# # or


# def multiply(times):
#     return times*times*times


# result = multiply(8)
# print(result)


# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:

#         return num2
#     else:
#         return num3


# print(max_num(300, 800, 5))


# drink = "Available"
# food = None


# def menu(x):
#     if x == drink:
#         print(drink)
#     else:
#         print(food)


# menu(drink)
# menu(food)

# a = 5
# print(a, "is of type", type(a))

# a = 2.0
# print(a, "is of type", type(a))

# a = 1+2j
# print(a, "is complex number?", isinstance(1+2j, complex))


# def multiplication_or_sum(num1, num2):
#     # calculate product of two number
#     product = num1 * num2
#     # check if product is less then 1000
#     if product <= 1000:
#         return product
#     else:
#         # product is greater than 1000 calculate sum
#         return num1 + num2


# # first condition
# result = multiplication_or_sum(20, 30)
# print("The result is", result)

# # Second condition
# result = multiplication_or_sum(40, 30)
# print("The result is", result)


# income = 45000
# taxPayable = 0
# print("Given income", income)

# if income <= 10000:
#     taxPayable = 0
# elif income <= 20000:
#     taxPayable = (income - 10000) * 10 / 100
# else:
#     # first 10,000
#     taxPayable = 0

#     # next 10,000
#     taxPayable = 10000 * 10 / 100

#     # remaining
#     taxPayable += (income - 20000) * 20 / 100

# print("Total tax to pay is", taxPayable)


# def greet_me(first_name, last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome back')


# print('start')
# greet_me('Coder', 'Javascript')
# greet_me('Ibraheem', 'Omikunle')
# print('finish')


# def square(number):
#     return number * number
#
#
# result = square(3)
# print(square(3))
# age = int(input('Age: '))
# print(age)


# def my_function(fname="Ibraheem", lname="Omikunle"):
#     print(fname + " " + lname)


# my_function()


# def my_function(*cars):
#     print("My favourite car is " + cars[2])


# my_function("Ford", "Toyota", "Benz", "Ford")


# def sayHello(name):
#     print(f'Hello {name}')


# sayHello('Ibraheem Omikunle')


# def getSum(num1, num2):
#     total = num1 + num2
#     return total


# num = getSum(10, 20)
# print(num)


# def getSum(num1, num2): return num1 + num2


# print(getSum(40, 40))
# function


# def course_func(name, course_name):
#     print("Hello", name, "Welcome to Boldlinks")
#     print("Your course name is", course_name)


# # call function
# course_func('Ibarheem', 'Python')

# function


# def calculator(a, b):
#     add = a + b
#     # return the addition
#     return add


# call function
# take return value in variable
# res = calculator(20, 5)

# print("Addition :", res)
# # Output Addition : 25


# def even_odd(n):
#     # check numne ris even or odd
#     if n % 2 == 0:
#         print('Even number')
#     else:
#         print('Odd Number')

# # calling function by its name
# even_odd(19)
# # Output Odd Number


# def factorial(x):
#     """This function returns the factorial of a given number."""
#     return x

# # access doc string
# print(factorial.__doc__)


# from random import randint

# # call randint function to get random number
# print(randint(10, 20))
# # Output 14

# def any_fun(parameter1):
#     """
#         Description of function

#     Arguments:
#     parameter1(int):Description of parameter1

#     Returns:
#     int value
# """
# print(any_fun.__doc__)


# def is_even(list1):
#     even_num = []
#     for n in list1:
#         if n % 2 == 0:
#             even_num.append(n)
#     # return a list
#     return even_num

# # Pass list to the function
# even_num = is_even([2, 3, 42, 51, 62, 70, 5, 9, 88, 98, 100, 200, 500, 60, 23, 20, 50, 43, 40, 99, 300, 308, 16, 8])
# print("Even numbers are:", even_num)


# def arithmetic(num1, num2):
#     add = num1 + num2
#     sub = num1 - num2
#     multiply = num1 * num2
#     division = num1 / num2
#     # return four values
#     return add, sub, multiply, division

# # read four return values in four variables
# a, b, c, d = arithmetic(10, 2)

# print("Addition: ", a)
# print("Subtraction: ", b)
# print("Multiplication: ", c)
# print("Division: ", d)


# global_lang = 'DataScience'

# def var_scope_test():
#     local_lang = 'Python'
#     print(local_lang)

# var_scope_test()
# # Output 'Python'

# # outside of function
# print(global_lang)
# Output 'DataScience'

# NameError: name 'local_lang' is not defined
# print(local_lang)


# def function1():
#     # local variable
#     loc_var = 888
#     print("Value is :", loc_var)

# def function2():

#     print("Value is :", loc_var)

# function1()
# function2()

# global_var = 999

# def function1():
#     print("Value in 1nd function :", global_var)

# def function2():
#     print("Value in 2nd function :", global_var)

# function1()
# function2()


# Global variable
# global_var = 5

# def function1():
#     print("Value in 1st function :", global_var)

# def function2():
#     # Modify global variable
#     # function will treat it as a local variable
#     global_var = 555
#     print("Value in 2nd function :", global_var)

# def function3():
#     print("Value in 3rd function :", global_var)

# function1()
# function2()
# function3()

# x = 5

# # defining 1st function
# def function1():
#     print("Value in 1st function :", x)

# # defining 2nd function
# def function2():
#     # Modify global variable using global keyword
#     global x
#     x = 555
#     print("Value in 2nd function :", x)

# # defining 3rd function
# def function3():
#     print("Value in 3rd function :", x)

# function1()
# function2()
# function3()


# def outer_func():
#     x = 777

#     def inner_func():
#         # local variable now acts as global variable
#         nonlocal x
#         x = 700
#         print("value of x inside inner function is :", x)

#     inner_func()
#     print("value of x inside outer function is :", x)

# outer_func()


# def add(a, b):
#     print(a - b)

# add(50, 10)
# # Output 40
# add(10, 50)
# # Output -40


# def message(name, surname):
#     print("Hello", name, surname)

# message(name="John", surname="Wilson")
# message(surname="Ault", name="Kelly")


# def addition(*numbers):
#     total = 0
#     for no in numbers:
#         total = total + no
#     print("Sum is:", total)


# # 0 arguments
# addition()

# # 5 arguments
# addition(10, 5, 2, 5, 4)


# # 3 arguments
# addition(78, 7, 2.5)


# def factorial(no):
#     if no == 0:
#         return 1
#     else:
#         return no * factorial(no - 1)

# print("factorial of a number is:", factorial(5))


# def even_numbers(nums):
#     even_list = []
#     for n in nums:
#         if n % 2 == 0:
#             even_list.append(n)
#     return even_list

# num_list = [10, 5, 12, 78, 6, 1, 7, 9]
# ans = even_numbers(num_list)
# print("Even numbers are:", ans)


# l = [10, 5, 12, 78, 6, 1, 7, 9]
# even_nos = list(filter(lambda x: x % 2 == 0, l))
# print("Even numbers are: ", even_nos)


# l = [-10, 5, 12, -78, 6, -1, -7, 9]
# positive_nos = list(filter(lambda x: x > 0, l))
# print("Positive numbers are: ", positive_nos)


# list1 = [2, 3, 4, 8, 9]
# list2 = list(map(lambda x: x*x*x, list1))
# print("Cube values are:", list2)


# from functools import reduce
# list1 = [20, 13, 4, 8, 9]
# add = reduce(lambda x, y: x+y, list1)
# print("Addition of all list elements is : ", add)


# def func1(*args):
#     for i in args:
#         print(i)

# func1(20, 40, 60)
# func1(80, 100)


# def calculation(a, b):
#     return a+b, a-b

# res = calculation(40, 10)
# print(res)


# def showEmployee(name, salary=9000):
#     print("Employee", name, "salary is:", salary)

# showEmployee("Ben", 9000)
# showEmployee("Ben")


# def outerFun(a, b):
#     square = a**2
#     def innerFun(a,b):
#         return a+b
#     add = innerFun(a, b)
#     return add+5

# result = outerFun(5, 10)
# print(result)


# def calculateSum(num):
#     if num:
#         return num + calculateSum(num-1)
#     else:
#         return 0

# res = calculateSum(10)
# print(res)


# def displayStudent(name, age):
#     print(name, age)

# displayStudent("Emma", 26)

# showStudent = displayStudent
# showStudent("Emma", 26)


# print(list( range(4, 30, 2)))


# aList = [4, 6, 8, 24, 12, 2]
# print(max(aList))


# print("My name is", "Python.", end=" ")
# print("Monty Python.")


# def myFullName(fname, lname, mname):

#     print(f'my name is  {fname} {lname} {mname}')


# myFullName("Ibraheem", "Omikunle", "Adisa")


# def simpleInterest(p, r, t):
#     print((p*r*t)/100)


# simpleInterest(400, 20, 5)

# def sumAnddifference_1(a, b):
#     print(a + b)
#     print(a - b)


# sumAnddifference_1(7, 6)


# def sumAnddifference_2(a, b):
#     if a and b > 0:
#         return a + b
#         return a - b
#     else:

#         return 0


# print(sumAnddifference_2(10, 20))
# print(sumAnddifference_2(80, 32)


# def check_age(age):
#     if age < 18:
#         print('ooops not an adult')
#     else:
#         print('hooray I am an adult')
# print("Ibraheem".endswith("M"))
# print("Ibraheem".endswith("m"))


# check_age(18)
# check_age(17)
# check_age(99)


# def max_num_in_list(list):
#     max = list[0]
#     for a in list:
#         if a > max:
#             max = a

#     return max


# print(max_num_in_list([20, 10, 60, 80, 5, 30, 100]))

#
# def message(name, age):
#     print(f'Her name is {name} and she is {age} years old')
#
#
# message(name="Mary", age=30)
#
#
# def showEmployee(name, salary):
#     print(f'Mr {name} salary is: {salary}')
#
#
# showEmployee("John", 10000)
#
#
# def my_function(*my_stack):
#     print(f'The language i love most is {my_stack[8]}')
#
#
# my_function("Php", "Typscript", "Sass", "Python", "C#", "C",
#             "C++", "Cobol", "Javascript", "Golang", "Rust")
#
#
# def my_frameworks(frame2, frame3, frame1, frame4, frame5, frame6):
#     print(f'My favourite framework is  {frame4}')
#
#
# my_frameworks(frame1="Angular.js", frame2="Sweetalert.js", frame3="Jquery",
#               frame4="React.js", frame5="Vue.js", frame6="Hammer.js")
#
#
# def my_frameworks_css(**css):
#     print("My favourite framework is " + css["frame1"])
#
#
# my_frameworks_css(frame1="Bootstrap", frame2="Tailwind",
#                   frame3="Bulma", frame4="Materialize", frame5="Foundation")
#
#
# def my_function(country="Canada"):
#     print("I am from " + country)
#
#
# my_function("Nigeria")
# my_function("America")
# my_function()
# my_function("London")
#
#
# def my_function(programming):
#     for stack in programming:
#         print(stack)
# softwares = ["Php", "Laravel", "Django", "Flask",
#              "React", "Javascript", "Css", "C#", "Rust", "Mvc"]
# my_function(softwares)


# def my_multiplier(x):
#     return 2 * x


# print(my_multiplier(8))
# print(my_multiplier(16))
# print(my_multiplier(32))


# def do_math(*args):
#     for n in args:
#         print(n)


# do_math(1, 2, 3)


# def func(**name):
#     for i, value in name.items():
#         print(i, value)


# func(value1=1, value2=2, value3=3)


# def greeting():
#     return "Good-day  Coder_Javascript"


# print(greeting())

# print(strip_and_upper_case())


# def strip_and_upper_case(s): return s.strip().upper()


# strip_and_upper_case("   Javascript   ")


# def find_student_score():
#     olaniyi = [60, 75, 53, 44, 98]
#     abdullahi = [55, 60, 46, 78, 75]
#     adebisi = [45, 98, 65, 76, 35]
#     olayinka = [47, 64, 43, 57, 87]

#     print("Olaniyi total score:", sum(olaniyi),
#           "average score is ", sum(olaniyi)/len(olaniyi))
#     print("Abullahi total score:", sum(abdullahi),
#           "average score is ", sum(abdullahi)/len(abdullahi))
#     print("Adebisi total score:", sum(adebisi),
#           "average score is ", sum(adebisi)/len(adebisi))
#     print("Olayinka total score:", sum(olayinka),
#   "average score is ", sum(olayinka)/len(olayinka))


# find_student_score()


# myList = [2, 14, 5, 17, 20, 15, 18, 25, 30, 12, 45]

# t = []

# def greater(myList):
#     for item in myList:
#         if item >= 18:
#             t.append(item)

#     print(t)


# greater(myList)


# def getSumAve(name, html, css, js, python, django):
#     sumNo = html + css + js + python + django

#     aveNum = sumNo / 5
#     print(name, "Total sum is ", sumNo, "and the average is :", aveNum)


# getSumAve("Olanyi", 60, 75, 53, 44, 98)
# getSumAve("Abdullahi", 55, 60, 46, 78, 75)
# getSumAve("Olayinka", 45, 98, 65, 76, 35)
# getSumAve("Adebisi", 47, 64, 43, 57, 78)


# def greet(*names):
#     """This function greets all
#     the person in the names tuple."""
#
#     # names is a tuple with arguments
#     for name in names:
#         print("Hello", name)
#
#
# greet("Monica", "Luke", "Steve", "John")
#
#
# print("My", "name", "is", "Ibraheem", "Omikunle", sep="+")
#
#
# print("My name is ", end="")
# print("Coder Javascript.")
#
#
# print("My", "name", "is", sep="_", end="*")
# print("Monty", "Python.", sep="*", end="*\n")
#
# def multiplyList(myList):
#     # Multiply elements one by one
#     result = 1
#     for x in myList:
#         result = result * x
#     return result
#
# # Driver code
# list1 = [8, 2, 3, -1, 7]
# print(multiplyList(list1))
#
#
#
#
# def even_numbers(nums):
#     even_list = []
#     for n in nums:
#         if n % 2 == 0:
#             even_list.append(n)
#     return even_list
#
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ans = even_numbers(num_list)
# print("Even numbers are:", ans)
#
#
# import math
#
# def square_of_numbers():
#     numbers = range(1,31)
#     append_numbers = []
#     for range_of_numbers in numbers:
#         numbers_squares = range_of_numbers * range_of_numbers
#         append_numbers.append(numbers_squares)
#     print(append_numbers)
# square_of_numbers()
#
#
#
#
# def string_test(s):
#     d={"UPPER_CASE":0, "LOWER_CASE":0}
#     for c in s:
#         if c.isupper():
#            d["UPPER_CASE"]+=1
#         elif c.islower():
#            d["LOWER_CASE"]+=1
#         else:
#            pass
#     print ("Original String : ", s)
#     print ("No. of Upper case characters : ", d["UPPER_CASE"])
#     print ("No. of Lower case Characters : ", d["LOWER_CASE"])
#
# string_test('The quick Brown Fox')


# def print_factors_of_300(number):
#     factorised_numbers = []
#     print(f"The factors of {number} are:")
#     for factors in range(1, number + 1):
#         if number % factors == 0:
#             factorised_numbers.append(factors)
#     print(factorised_numbers)


# The_number = 300
# print_factors_of_300(The_number)

# a = lambda b, c, d: b - c + d
# print(a(20, 10, 15))
#
# x = lambda z: z + 15
# print(x(40))
#
#

# def sum_of_two_integers(x, y):
#     sum_of_numbers = x + y
#     if sum_of_numbers in range(15, 20):
#         return 20
#     else:
#         return sum_of_numbers
#
#
# print(sum_of_two_integers(10, 9))
# print(sum_of_two_integers(10, 2))
# print(sum_of_two_integers(8, 12))

# def double(my_number, triple, quad):
#     return f"double number: {my_number * 2} \ntriple number: {triple * 3} \nquadrauple number: {quad * 4}"
#
#
# my_var = double(30, 30, 30)
# print(my_var)
#
# models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
#           {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# print("Original list of dictionaries :")
# print(models)
# sorted_models = sorted(models, key=lambda x: x['color'])
# print("\nSorting the List of dictionaries :")
# print(sorted_models)

# def greetings_function(name, age):
#     print('Welcome ' + name + ' You are ' + str(age) + ' years old.')
#
# greetings_function('Ibraheem', 20)


# def greetings_function(name, age):
#     print('Welcome ' + name + ' You are ' + str(age) + ' years old.')
# name = input('Enter your name: ')
# age = input('Enter your age: ')
# greetings_function(name, age)


# def greetings_function(name, age):
#     print('Welcome ' + name + ' You are ' + str(age) + ' years old.')
#
# greetings_function(name = 'Ibraheem', age = 20)

# def greetings_function(*names):
#     print('Welcome ' + names[1])
#
# greetings_function('Ibraheem', 'Coder', 'Brad')

# Return statements in python
# def my_function():
#     return 5 + 4
#
#
# print(my_function())

# def add_numbers(num1, num2):
#     print('Your answer is :')
#     return num1 + num2
#
# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# print(add_numbers(num1, num2))