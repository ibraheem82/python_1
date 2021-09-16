'''
This is a 
multiline comment
or docstring (used to define function purpose)
can be single or double quotes
'''

'''
VARIABLE RULES:
- Variable names are case sensitive (name and NAME are different variable)
- Must start with a letter or an underscore
- Can have numbers but can not start with one
'''

# x = 1          # int
# y = 2.5         # float
# name = 'John'    # str
# is_cool = True    # bool

# Multiple assignment
x,  y, name, is_cool = (1, 2.5, 'John', True)

# # Basic math
# a = x + y

# Casting 
# x = str(x)
# y = int(y)
# z = float(y)

# # print(x, y, name, is_cool, a)

# print(type(z), z)

# x = 1
# y = 2.5
# name = 'John'
# is_cool = True


# print('Ibraheem Omikunle')
# print('o----')
# print(' ||||')
# print('*' * 10)

# price = 10
# rating = 4.9
# name = 'Mosh'
# is_published = True
# price = 20
# print(price)


# full_name = 'John Smith'
# age = 20
# is_new = True


# name = input('What is your name? ')
# favorite_color = input('What is your favorite color? ')
# print(name + ' likes ' + favorite_color)

# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2021 -int(birth_year)
# print(type(age))
# print(age)

# weight_lbs = input('Weight (lbs): ')
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)


# Strings

# course = "Python's Course for Beginners"
# course = 'Python for "Beginners"'
# print(course)

# course = '''
# Hi John,

# Here is our first email to you.

# Thank you,
# The support team 

# '''
# print(course)

# Index numbers in python, it counts from zero

# You can also you the negative index, with the negative index you can get the character from starting from the end 

# course = 'Python for Beginners'
# print(course[0])

# course = 'Python for Beginners'
# print(course[-2])


#we can also use python to extract character
#   it will return the index starting point to the last point
# but it wont show the last index entered

# course = 'Python for Beginners'
# print(course[0:3])

course = 'Python for Beginners'
another = course[:]

print(another)

