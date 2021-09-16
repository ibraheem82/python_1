# Strings in python are surrounded by either single or double quotation marks. Lets look at string formatting and some string methods

# name = 'Ibraheem'
# age = 20

# Concatenate
# print('Hello, my name is ' + name + ' and I am ' + str(age)) 

# String Formatting

# Argument by position
# print('My name is {name} and I am {age}'.format(name=name, age=age))


# F-Strings (3.6+) 

# print(f'Hello, my name is {name} and I am {age}')
# String Methods

# s = 'hello world'

# # Capitalize string

# print(s.capitalize())

# To create a new line inside of a string it will insert a line line in the string
print("Ibraheem\nOmikunle")

# To Use a Quotetation mark inside of a string
# Use the escape character or escape sequence
print("Omikunle\"Ibraheem")


phrase = "Ibraheem Omikunle"
print(f'{phrase} is cool.')
print(phrase.upper())
print(phrase.lower())
# To check if a string is in upper case
print(phrase.upper().isUpper())

# To know the length using the length function
print(len(phrase))


# To get the characters in a string
# It start counting from zero
# print(phrase[3])
#
# # To get index, to tell us where a particular character is located
# print(phrase.index("I"))
#
#
# print(phrase.index("Ibrah"))
#
# print(phrase.replace("Omikunle", "Boldlinks"))


# # Python strings
# course = "Python's course for Beginner"
# print(course)
#
# course = 'Python  for "Beginner"'
# print(course)
#
# course = "Python's course for Beginner"
#
# print(course[2])
# print(course[-2])
#
# # To extract strings in python
# # starting from the first index
# # to the end index
# course = "Python's course for Beginner"
# print(course[0:5])
# print(course[1:])
# print(course[:5])
# name = 'jennifer'
# print(name[1:-1])
#
# # Strings concatenation in python
# first = 'Ibraheem'
# last = 'Omikunle'
# msg = f'{first} [{last}] is a coder'
# print(msg)
#
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))

# Strings method in python
# course = 'Python for beginners'
# print(len(course))
# course = 'Python for beginners'
# print(course.upper())
# course = 'Python for beginners'
# print(course.lower())
# course = 'Python for beginners'
# print(course.find('P'))
# print(course.find('o'))
# print(course.find('beginners'))
# print(course.replace('beginners', 'Absolute beginners'))
# print('Python' in course)
# print(course.('P'))

# print("   / |")
# print("  /  |")
# print(" /   |")
# print("/____|")
#
# x = 7
#
# y = "John"
#
# print(x, y)
#
# character_name = "John"
# character_age = "35"
#
# print("There once was a man named ")
# print("he was 35 years old.")
# print("He really liked the name John ")
# print("but didn't like being 35.")