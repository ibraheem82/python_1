''' 
# You can also loop through a series of numbers
# To loop through arrays or inside of a string or series of numbers
# For loops allows us to loop through collections of items
# while loops is a structure in python which allows us to loop through and executes a blocks of code Multiple times
# it will execute the code repeatedly until a certain condition is false or met.
# Range is use for creating a range of numbers 
# 
'''
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# print("Done looping ! ")

# for letters in "Omikunle Ibraheem":
#     print(letters)


# friends = ["Jim", "Karen", "Kevin"]
# for name in friends:
#     print(name)
# friends = ["Jim", "Karen", "Kevin"]
# for index in range(len(friends)):
#     print(friends[index])

# friends = ["Jim", "Karen", "Kevin"]
# for index in range(8):
#     if index == 0:
#         print("first Iteration")
#     else:
#         print("Not first")


# for name in friends:
#     print(name)

# for index in range(10):
#     print(index)

# for index in range(10):
#     print(index)


# for name in 'Javascript':
#     print(name)


# for item in ['Ibraheem', 'Omikunle', 'Adisa', 'Ayomide']:
#     print(item)


# for ranger in range(5,80):
#     print(ranger)

# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
#     # or total = total + price
# print(f'Total: {total}')

# # '''
# # # nested loops

# # '''


# for x in range(4):
#     for y in range (3):
#         print(f'({x}, {y})')

# numbers = [5, 2, 5, 2, 2]
# for  number_loops in numbers:
#     print('x' * number_loops)


# numbers = [5, 2, 5, 2, 2]
# for  x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'

#     print(output)

# for four in range(4):
#     print(four)


# i = 1
# while i < 6:
#     print(f'.{i}')
#     i += 1


# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(f'.{i}')


# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 6")


# for i in (0, 1, 2, 3, 4, 5):
#         if i == 2 or i == 4:
#             continue
# print(i)


# for x in range(16):
#     print(x)


# for i in range(0, 30):
#         print(i * 3)
#         i += 1


# def findMultiples(x):
#         for x in range(0, x + 1):
#             if x % 3 == 0 and x % 5 == 0:


#                 print(x);

# findMultiples(120);

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
# num = 30
# for x in num:
#     multiple =  x * 3
# print("Square of:", x, "is:", square)

# # iterate over each element in list num
# for i in numbers:
#     # ** exponent operator
#     square = i * 2
#     print("Square of:", i, "is:", square)


# a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# for x in a:
#     if (x > 100):
#     break


# b = []
# for c in list1:
#     if c % 5 == 0 and c <= 150:
#         b.append(c)
# print(b)


# today = "monday"
# if (today == "monday"):
#     print("Today is monday")
# else:
#     print("Insert correct day")

# principal = 4000
# rate = 2.5
# time = 3
# simpleInterest = (principal * rate * time)/100
# print("1")
# print("a)The simple interest is", simpleInterest)

# principal = 5000
# rate = 3.2
# time = 2
# simpleInterest = (principal * rate * time)/100
# print("b)The simple interest is", simpleInterest)

# print("2")
# x = 3
# y = 2

# meme = (x + 2.5 + (8 * x) - 3 * (4 * y))
# print("a)", meme)
# mama = ((2 * (x * x)) * (3 * x) - (4 * y))
# print("b)", mama)

# boldlinks = "javascript, python"
# print(boldlinks[12:18].upper())

# a = "  ASSIGNMENT 1  "
# print(a)

# b = "lython, java"
# print("1) ",b.replace("lython", "python"))

# txt = "Ade is a good programmer; Although ade can be lazy sometimes"
# x = txt.count("Ade")
# y = txt.count("ade")
# z = x + y
# print("2) ",z)

# x = 300
# y = 400
# product = x * y
# sam = x + y
# if (product > 1000):
#     print("3) ",sam)
# else:
#     print("3) ",product)

# a = "  ASSIGNMENT 2  "
# print(a)

# txt = "Python is one of the best programming languages"
# print("1) ",len(txt))

# assign = "Welcome to the programming class"
# print("2) ",assign[0:8])

# txt = "Python"
# print("3) ", txt[3:6])

# pest = "javascript"
# print("4) ", pest.upper())

# txt = "Umbrella"
# x = "e" in txt
# print("4) ", x)

# tame = [ 11, 5, 17, 18, 23]
# tam = sum(tame)
# print("1) ",tam)


# bet = "  ASSIGNMENT 3  "
# print(bet)

# languages = ["python", "java", "php", "html"]
# languages.append("javascript")
# print("1) ",languages)
# languages[0] = "visual basic"
# print("2) ",languages)
# languages.remove("java")
# print("3) ",languages)


# cars = [100, 200, 50, 60, 70, 90]
# cars.sort()
# print(cars)

# dogs = [12, 15, 32, 42, 55, 75, 112, 132, 150, 180, 200]
# bat = []
# for c in dogs:
#     if c % 5 == 0 and c <= 150:
#         bat.append(c)
# print(bat)

# bet = "  ASSIGNMENT 4  "
# print(bet)
# bet = "  PART1  "
# print(bet)

# Statement1 = "Python is a dynamic and intrepreted language, it is very easy to learn, python is multipurpose language. "
# Statement2 = "It can be used for various programming jobs like web development, data science, machine learning & pyhton can be used for artificial intelligence"
# Statement3 = Statement1 + Statement2
# print("1) ",Statement1.replace("dynamic", "interpreted"))
# print("2) ",Statement1.index("python"))
# x = "Python" in Statement1
# print("3) ", x)
# x = "golang" in Statement1
# print("4) ", x)
# print("5) ",Statement2[0:42])
# print("6) ",Statement2.replace("artificial intelligence", "AI"))
# print("7) ",Statement3)

# bet = "  PART2  "
# print(bet)
# wema = "boldlinks academy"
# u = wema.split()
# u.insert(1, "coding")
# demi = " ".join(u)
# gr = demi.upper()
# print(gr)

# import math

# tame = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# goat = []
# for boat in tame:
#     cat = boat**2
#     goat.append(cat)
# print(goat)

# names1 = ["abu", "ibrahim", "john", "", "ade", "", "ayo"]
# manes = list(filter(None, names1))
# print(manes)
# # w = []
# # for o in names1:
# #     if o is not "":
# #         w.append(o)
# # print(w)


# num = [20, 40, 10, 20, 70, 90, 20, 50]
# mun = list(filter((20).__ne__, num))
# print(mun)
# # w = []
# # for o in num:
# #     if o is not 20:
# #         w.append(o)
# # print(w)

# number = [10, 20, 40, [70, 80, 90], 200, 300]
# number[3].append(100)
# print(number)


# bet = "  CLASSWORK  "
# print(bet)
# u = [20, 10,[40, 30, 40], 50, 60]
# u[2].append(45)
# print("1) ",u)

# u = [40, 60, [70, [80, 90, 100], 120, 130], 140,150]
# u.append(160)
# print("2) ",u)
# u[2].append(135)
# print("3) ", u)

# bet = "  CLASSWORK 2  "
# print(bet)
# tayo = [4, 5, 6, 7, 8, 9, 10, 11, 12]
# tab = []
# for c in tayo:
#     if c % 2 == 0:
#         tab.append(c)
# tami = sum(tab)
# print("1)  The sum of the even numbers in the list is",tami)

# colour = ["red", "white", "blue", "green", "orange"]
# colourlib = colour[0],colour[-1]
# print("2) ",colourlib)

# colur = ("red", "white", "blue", "green", "orange", "brown")
# y = list(colur)
# y[1] = "gray"
# colur = tuple(y)

# print("3) ",colur)


# bet = "  ASSIGNMENT  "
# print(bet)

# # How many time does 777 occur?. tt = (55, 6, 777, 54, 6, 76, 7777, 777, 84)
# tt = (55, 6, 777, 54, 6, 76, 7777, 777, 84)
# x = tt.count(777)
# print("1) ",x)


# # change plato's birth year 1985 to 1995.
# platos =	{
#   "name":"plato",
#   "country":"nigeria",
#   "birth":1985,
#   "status":"single"
# }
# platos["birth"] = 1995
# print("2) ",platos)


# bet = "  CLASSWORK  "
# print(bet)

# sentence1 = {"name":"Ade"}
# # x = sentence1.get("name")
# # print("1) ",x)
# print("1) ",sentence1["name"])

# sentence2 = {"name":{"level":"No1"}}
# # x = sentence2.get("name")
# # y = x.get("level")
# # print("2) ",y)
# print("2) ",sentence2["name"]["level"])

# sentence3 = {
#     "class":{
#         "student":{
#             "name":"mike"
#         }
#     }
# }
# # x = sentence3.get("class")
# # y = x.get("student")
# # z = y.get("name")
# # print("3) ",z)
# print("3) ",sentence3["class"]["student"]["name"])

# family = {"child":{"name":"Emi"}}
# # x = family.get("child")
# # y = x.get("name")
# # print("4) ",y)
# print("4) ",family["child"]["name"])

# bet = "  ASSIGNMENT  "
# print(bet)

# mydictionary = {"math":100, "english":54, "physics":247, "chemistry":70}
# x = mydictionary.values()
# y = sum(x)
# print("1) ",y)

# answer = 1
# for x in mydictionary:
#     answer = answer*mydictionary[x]
# print("2) ",answer)

# print("Grade")
# mark = 75
# if mark < 25:
#     print("F")
# elif mark >= 25 and mark <= 45:
#     print("E")
# elif mark >= 46 and mark <= 50:
#     print("D")
# elif mark >= 51 and mark <= 60:
#     print("C")
# elif mark >= 61 and mark <= 80:
#     print("B")
# else:
#     print("A")

# morn = int(5)
# if morn == 1:
#     print("SUNDAY")
# elif morn == 2:
#     print("MONDAY")
# elif morn == 3:
#     print("TUESDAY")
# elif morn == 4:
#     print("WEDNESDAY")
# elif morn == 5:
#     print("THURSDAY")
# elif morn == 6:
#     print("FRIDAY")
# elif morn == 7:
#     print("SATURDAY")


#  ASSIGNMENT
#                    Write a python code
# 1) To check maybe a number entered is even or odd number
# 2) To check whether a number is divisible by seven or not
# 3) To check if a person is eligible for voting or not
# 4) To accept the age of four people and display the oldest
# print("  ASSIGNMENT   ")
# mars = 15
# if mars % 2 == 0:
#     print("1) ",mars,"is even number")
# else:
#     print("1) ",mars,"is odd number")

# sars = 84
# if sars % 7 == 0:
#     print("2) ",sars,"can be divided by seven")
# else:
#     print("2) ",sars,"cannot be divided by seven")

# cans = 18
# if cans < 18:
#     print("3) ",cans,"years of age is not allowed to vote")
# else:
#     print("3) ",cans,"years of age is allowed to vote")

# ages = [ 12, 50, 17, 18]
# maximum = max(ages)
# print("4) ",maximum)

# A = 40
# B = 45
# C = 60
# D = 55
# if A > B and A > C and A > D:
#     print("5) A is the oldest")
# if B > A and B > C and B > D:
#     print("5) B is the oldest")
# if C > A and C > B and C > D:
#     print("5) C is the oldest")
# if D > A and D > B and D > C:
#     print("5) D is the oldest")


# # CLASSWORK
# #                    Write a python code

# #1) To check if a year is a leap year or not
# #2) To check if the character is vowel
# #3) To accept age and number of days and display the wages accordingly i.e
# # 18yrs - 30yrs = 700
# # 31yrs - 40yrs = 800

# # Get prime number ranging from 25 to 50

# print("Prime numbers between", 25, "and", 51, "are:")

# for num in range(25, 51):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

# print("  CLASSWORK  ")
# print("  NUMBER 1  ")
# print 1 to 15
# tat = []
# for x in range(1,16):
#     tat.append(x)
# print(tat)

# print("  NUMBER 2  ")
# #print out multiple of 3 btw 1 - 30
# bob = []
# for x in range(1,31):
#     if x % 3 == 0:
#         bob.append(x)
# print(bob)
# print("  NUMBER 3  ")
# #print out the even position
# a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# tab = []
# for c in a:
#     if c % 20 == 0:
#         tab.append(c)
# print(tab)
# print("  ASSIGNMENT  ")
# #print out the even postion
# a = [10, 25, 30, 45, 50, 65, 70, 80, 90, 100]
# tab = []
# for c in a:
#     if c % 5 == 0:
#         tab.append(c)
# print(tab)


# i = 0
# b = []
# while i <= 15:
#     b.append(i)
# print(b)
# i += 1


# num = 0, 1, 2, 3, 4, 5

# for i in num:
#     if i == 2 or i == 4:
#         continue
# print(i)


# cars = ['bwm', 'tesla', 'mercedes', 'toyota']


# for car in cars:
#     if car == 'tesla':
#         print(car.upper())
#     else:
#         print(car.capitalize())
#
# number = 0
#
# while number <= 10:
#     print(number)
#
#     number += 1
# else:
#     print('while loop ended and value of nmber is ' + str(number))
#
#     count = 0
# while count <= 10:
#     print(f'Count: {count}')
#     count += 1


# # loops in python
#
# my_Names = ['Ibraheem', 'Adisa', 'Ayomide', 'Omikunle', 'Olamilekan', 'Oluwadamilare']
#
# for name in my_Names:
#     print(name)
#

#
# for i in [2, 1, 5]:
#     print(i)
#
#     smallest = None
# print("Before:", smallest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#         break
#     print("Loop:", itervar, smallest)
# # print("Smallest:", smallest)

# mylist = ["ji", 'ju', 'jo']
#
# for values in mylist:
#     print(values)
#     if values == 'ju':
#         break
#
# for values in mydict:
#     print(values)
# for x in range(10):
#     print(x)

# for x in range(3, 7):
#     print(x)

#
# for x in range(7):
#     print(x)
# else:
#     print('Finished Looping!!!')





