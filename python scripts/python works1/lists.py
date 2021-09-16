# # A List is a collection which is ordered and changeable. Allows duplicate members.
# # Create list

# numbers = [1, 2, 3, 4, 5]
# fruits = ['Apples', 'Orange', 'Grapes', 'Pears']

# # # Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# # # Get a value
# print(fruits[1])
# # print(numbers, numbers2);

# # # Get length 
# print(len(fruits))

# # # Append to list
# fruits.append('Mangos')

# # # Remove from list

# fruits.remove('Grapes')

# # # Insert into position 
# fruits.insert(2, 'strawberries')

# # # Change value

# fruits[0] = 'Blueberries'

# # # Remove with pop 

# fruits.pop(2)

# # # Reverse list
# fruits.reverse()

# # Sort list
# fruits.sort()

# # # Reverse sort
# fruits.sort(reverse=True)

# print(fruits)

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# print(names[3])
# print(names[-2])
# print(names[1:3])
# names[0] = 'Ibraheem'
# print(names)


# # How to find the largest number in a list
# numbers = [3, 6, 2, 4, 10]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
#         print(max)

# # List methods
# numBers = [5, 2, 7, 7, 7, 1, 7, 4,]
# numBers.append(80)
# numBers.insert(1, 20)
# numBers.remove(1)
# numBers.pop(4)
# print(numBers)
# print(numBers.index(80))
# print(numBers.index(100))
# print(80 in numBers)
# print(numBers.count(7))
# numBers.sort()
# numBers.reverse()
# number1 = numBers.copy()
# numBers.append(88)
# print(number1)


# # Remove a duplicate in a list

# duplicate1 = [2, 2, 4, 6, 3, 4, 6, 1]
# duplicate2 = []
# for number in duplicate1:
#     if number not in duplicate2:
#         duplicate2.append(number)
#         print(duplicate2)

'''
# Working with lists in python
# the insert will add to the end of the list
# list is when you are able to store multiple values in an item
# you an also modify the values by i.e friends[1] = 'Mike'
# when you grab [1:] it will grab the item followed by the other items.
# when you grab [1:3] it will grab the item from index one to 2, and it will stop at two without accessing index three  by the other items.
# You an also access the index from the back of the list using [-1 or any other values you want to access]
in order to get a value in a list you have to use the opening and close brackets moreover note that the index start counting from one. 
# When you want to create a list you should use the opening a close square brackets
'''
# lucky_numbers = [4, 8, 15, 16, 23, 42]
# friends = ['Kelvin', 'Karan', 'Jim', 'Oscar', 'Toby']
# print(lucky_numbers)
# friends[1] = "Mike"
# friends.extend(lucky_numbers)
# print(friends)
# friends.append("Ibraheem")
# friends.insert(1, "Omikunle")
# friends.remove("Jim")
# friends.pop()
# lucky_numbers.sort()
# print(lucky_numbers)
# print(friends)
# print(friends[1])
# print(friends)
# print(friends[0])
# print(friends[2])
# print(friends[-2])
# print(friends[1:3])

# a = [5,10,15,20,25,30,35,40]

# a[2] = 15
# print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
# print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
# print("a[5:] = ", a[5:])


# Lists are mutable, meaning, the value of elements of a list can be altered.

# a = [1, 2, 3]
# a[2] = 4
# print(a)

# a = [80, 100, 'Ade', 'abu', 20]
# b = ['Father', 'Bola', 60, 'Ayo']
# c = a + b

# print(c)


# print(a[2:4])


# x = [1, 2, [3, 4, 5], 6, 7]  # this is nested list
# print(x[4])
#
# remove_first_items = ["Ade", "Joy", "Blessing", "Abdullahi", "Dauda"]
# print(f'The orignal items in the list are : {remove_first_items}')
# print(f'we are to remove the first item in the list which is : {remove_first_items[0]}')
# remove_first_items.remove("Ade")
# print(f'The remaining lists items after removing the first item from the list are :{remove_first_items}')
#
# list_items = ["Tiger", "Goat", "Chicken", "Lion"]
# print(list_items[-1], list_items[0])
# # print(list_items[0])


# Position, name, age, level, salary
# se1 = ["Software Engineer", "Ibraheem", 20, "Junior", 5000]
# se2 = ["Software Developer", "Brad", 40, "Senior", 7000]
# d1 = ["Designer", "Philip"]
# def code(se):
#     print(f"{se[1]} is busy writing codes <>...</>💻")
#
# code(se1)
# code(se2)
# print('hi. \nhow are you')


# countries = ['United Kingdom', 9, 'Ghana', 'Nigeria', 2, 'Australia', True, 'New Zealand', 'Saudi Arabia', 'Egypt', 'Mexico',
#              'South Africa', 'Turkey']
# print(countries[2][0])
# countries = list(('Nigeria', 34, False))
# print(countries)
# print(countries[1:])
# print(countries[1:4])
# print(type(countries))
# countries[0] = 'United States'
# print(countries)
# countries[3] = 'Canada'
# print(countries)
# print(countries[-1])
# print(countries[-2])
# print(len(countries))
# print(type(countries[1]))
# print(countries)
# print(type(countries))
# list1 = [56, 8, 3, 4, 53, 1, 3, 4, 9]
# list2 = ['orange', 'apples', 'mango', 'banana']
# list3 = list2.copy()
# print(list3)
# list2.pop()
# list2.pop(1)
# del list2
# print(list2)
# list1.extend(list2)
# list2.append('cherry')
# print(list2)
# print(len(list2))
# list2.insert(1, 'cherry')
# print(list2)
# list2.remove('banana')
# print(list2)
# list2.clear()
# print(list2.index('mango'))
# print(list2.count('mango'))
# print(list2)
# list1.sort()
# print(list1)
# list2.reverse()
# print(list2)

# number_grid = [
#     [1, 2, 3,],
#     [4, 5, 6,],
#     [7, 8, 9,],
#     [0]
# ]
#
#
#
#
#
# print(number_grid[0][0])
# print(number_grid[2][1])
'''
# Nested for loop
'''


# for row in number_grid:
#     print(row)
#
#
#
# for row in number_grid:
#     for col in row:
#         print(col)

# my_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(my_list)


my_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print(my_list[0][0])
# print(my_list[1][1])

# for lists in my_list:
#     print(my_list)



for lists in my_list:
    for row in lists:
        print(row)
