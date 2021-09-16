'''
# if Statement in python allows python to make decisions
# carrying out different conditions
# to check true or false in a progarm
'''
# is_male = False

# is_tall = False

# if is_male or is_tall:
#     print("You are a male or tall or both")

# else:
#     print("You neither male nor tall")


'''
# If statement and comparisions 
# To compare different data types
# 
'''

# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3

# print(max_num(30, 40, 89))

# is_hot = False

# if is_hot:
#     print('Its a hot day')
#     print('Enjoy your day')
#     print('Drink plenty water')

# else:
#     print('It  a cool day')
#     print('Wear warm clothes')


# name ="Ibraheem Omikunle"

# if len(name) < 3:
#     print("Name mst be at least 3 characters")
# elif len(name) > 50:
#     print("Name must be a maximum of 50 characters")
# else:
#     print("Name looks good!")


# stock = 200
# jeans_sold = 8000
# target = 500


# target_hit = jeans_sold = target
# print("Hit jeans sale target: ")
# print(target_hit)


# current_stock = stock * jeans_sold
# in_stock = current_stock != 0
# print("Jeans in stock: ")
# print(in_stock)
# print(current_stock)

# num = float(input("Enter a number: "))
# if num >= 0:
#     if num == 0:
#         print("Zero")
#     else:
#         print("Positive number")
# else:
#     print("Negative number")


# try:
#     age = int(input('Age: '))
#     income= 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be 0.')
# except ValueError:
#     print('Invalid value')

# people = ['John', 'Paul', 'Sara', 'Susan']

# for i  in range(len(people)):
#     print(people[i])


# for i in range(0, 11):
#     print(f'Number: {i}')

# age = 18
# numdays = 2
# if age  < 18:
#     print("3) Younger than wanted age")
# elif age  >= 18 and age <= 30:
#     print("3) The wage is",700 * numdays)
# elif age  >= 31 and age <= 40:
#     print("3) The wage is",800 * numdays)
# elif age  > 40:
#     print("3) Above wanted age")


# print("  CLASSWORK   ")

# cow = "i"
# vowel = "aeiouAEIOU"
# if cow in vowel:
#     print("2) Its a vowel letter")
# else:
#     print("2) Its a consonant letter")

# if cow == "a" and "e" and "i" and "o" and "u" and "A" and "E" and "I" and "O" and "U":
#     print("2) Its a vowel letter")
# elif cow == "a" and "e" and "i" and "o" and "u" and "A" and "E" and "I" and "O" and "U":
#     print("2) Its a vowel letter")
# else:
#     print("2) Its a consonant letter")
#
# user_added = True
# user = "Ibraheem"
#
# if user_added == False:
#     print(f"Adding {user} to database")
#     user_added = True
# print(f"Database has user: {user}")
#
# upper_limit = 91
# lower_limit = 24
# outlier = False
# number = 8
#
# if number > upper_limit:
#     outlier = True
# if number < lower_limit:
#     outlier = True
# if outlier == True:
#     print(f"{number} is an outlier")
#
# minimum_points = 100
# data_points = 150
#
# if data_points >= minimum_points:
#     print("There are enough data points!")
# if data_points < minimum_points:
#     print("Keep collecting data.")
#
# ride_type = "Black"
# credits = 4
#
# ride_price = 0
# final_price = 0
#
# if ride_type == "DooberX":
#     ride_price = 20.5
# elif ride_type == "Black":
#     ride_price = 40.9
# else:
#     ride_price = 18.7
#
# print("Ride price:")
# print(ride_price)
#
# if credits > 0:
#     final_price = ride_price - credits
#
# print("Final price:")
# print(final_price)
#
# var1 = 1 + 2j
# if (type(var1) == int):
#     print("Type of the variable is Integer")
# elif (type(var1) == float):
#     print("Type of the variable is Float")
# elif (type(var1) == complex):
#     print("Type of the variable is Complex")
# elif (type(var1) == bool):
#     print("Type of the variable is Bool")
# elif (type(var1) == str):
#     print("Type of the variable is String")
# elif (type(var1) == tuple):
#     print("Type of the variable is Tuple")
# elif (type(var1) == dict):
#     print("Type of the variable is Dictionaries")
# elif (type(var1) == list):
#     print("Type of the variable is List")
# else:
#     print("Type of the variable is Unknown")

#
# age = 38
# if (age >= 11):
#     print("You are eligible to see the Football match.")
#     if (age <= 20 or age >= 60):
#         print("Ticket price is $12")
#     else:
#         print("Tic kit price is $20")
# else:
#     print("You're not eligible to buy a ticket.")

# create a string
# s = 'jQuery'
# # create a list
# l = ['JavaScript', 'jQuery', 'ZinoUI']

# # in operator is used to replace various expressions that use the or operator
# if s in l:
#     print(s + ' Tutorial')

# # Alternate if statement with or operator

# if s == 'JavaScript' or s == 'jQuery' or s == 'ZinoUI':
#     print(s + ' Tutorial')


# text = input('Username: ')
# try:
#     number = int(text)
#     print(number)
# except:
#     print('Invalid Username')


# # Conditional statement in python
#
#
# a = 200
# b = 33
#
# if b > a:
#     print("b is greater than a")
# else:
#     print("b is not greater than a")
#
# x = "Hello"
# y = 0
#
# print(bool(x))
# print(bool(y))
#

# grade = 100
#
# if grade >= 65:
#     print("Passing grade")
# else:
#     print("Failing grade")

# a = 5
# b = 3
#
# if a > b:
#     print(str(a) + ' is greater than ' + str(b))


# a = 5
# b = 5
#
# if a == b:
#     print(str(a) + ' equals ' + str(b))

# value = int(input('Input a value: '))
#
# if type(value) == str:
#     print(value, ' is a string')
#
# # elif type(value) == int:
# #     print(value + ' is an integer')
# #
# # elif type(value) == list:
# #     print(value + ' is a list')
#
# else:
#     print(value, ' is not a string')



# value = int(input('Input a number: '))
#
# if value % 5 == 0:
#     print(value, 'can be divided by 5')
#
# else:
#     print(value, 'can not be divided by 5')




# value = int(input('Input a number: '))
#
# if value < 10:
#     print(value, 'can be divided by 10')
#
#
# else:
#     print(value, 'is more than 10')

# num = int(input('Enter a number: '))
#
#
#
# if num % 2 == 0:
#     print('Even number')
#
# else:
#     print('odd number')

# try:
    # x = int(input('Input an integer: '))
    # print(x)
# except ValueError:
    # print('value not an integer' )





