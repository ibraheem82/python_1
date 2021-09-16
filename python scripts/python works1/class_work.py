# today = "nSunday"

# if today == "Monday":
#     print('Happy', today, 'Morning')
# elif today == "Tuesday":
#     print('Happy', today, 'Morning')
# elif today == "Wednesday":
#     print('Happy', today, 'Morning')
# elif today == "Thursday":
#     print('Happy', today, 'Morning')
# elif today == "Friday":
#     print('Happy', today, 'Morning')
# elif today == "Saturday":
#     print('Happy', today, 'Morning')
# elif today == "Sunday":
#     print('Happy', today, 'Morning')
# else:
#     print("Happy days ahead")



# for x in range(-3,2):
#     print(x)
    
    
    
    
# P = 200000
# R = 5
# T = 3
# Simple_interest = (P * R * T) / 100
# print("The simple interest is:", Simple_interest)

# '''
# Solutions For simple interest
# '''

# p1 = 4000
# r1 = 2.5
# t1 = 3
# simple_interest1 = p1 * r1 * t1

# product = simple_interest1/100
# print(f'The simple interest is {product}')


# p2 = 5000
# r2 = 3.2
# t2 = 2
# simple_interest2 = (p2 * r2 * t2)/100
# print(f'The simple interest is {simple_interest2}')


# '''
# Solution for evaluate
# '''
# x = 3
# y = 2
# evaluate1 = (((x + 2.5) +((8 * x) - 3))*(4 * y))
# evaluate2 = (((2 + (x ** 2)) * (3 *x)) - (4 * y))

# print('The result is ', evaluate1)
# print('The result is ', evaluate2)





# # Python3 code to demonstrate working of
# # Expression evalution in String
# # Using eval()

# # initializing string
# test_str = "45 + 98-10"
# # printing original string
# print("The original string is : " + test_str)
# # Expression evalution in String
# # Using eval()
# res = eval(test_str)

# # printing result
# print("The evaluated result is : " + str(res))

# bold = "Javascript, python"
# print(bold[11:18])


# avaliableClasses = "python, java, ruby, php"
# print(avaliableClasses.replace("java", "Javascript"))



# principal = 10000
# rate = 10
# time = 0.5
# the_simple_interest_of = principal * rate * time

# answer_of_simple_interest =  the_simple_interest_of/100

# print(f'The simple interest of {principal}, {rate} and {time}  = {answer_of_simple_interest}')





# a = [80, 100, 'Ade', 'abu', 20]
# b = ['Father', 'Bola', 60, 'Ayo']
# c = a + b

# print(c)


# print(a[2:4])

# natural = [100, 200, 50, 60, 70, 90]
# sorted_numbers = sorted(natural)
# print(sorted_numbers)

list1 = [1, 15, 32, 42, 55, 75, 122, 132, 150, 100, 200]

b = []
for c in list1:
    if c % 5 == 0 and c <= 150:
        b.append(c)
print(b)



# Given a list, in a list
# (1)num1 = [4, 5, 6, 7, 8, 9, 10, 11, 12]
# find the sum of the even number in he list


# the_numbers_in_the_list = [4, 5, 6, 7, 8, 9, 10, 11, 12]

# for even_numbers in the_numbers_in_the_list:
#     if even_numbers % 2 ==0:
#         print(even_numbers, end = " ")

the_numbers_in_the_list = [4, 5, 6, 7, 8, 9, 10, 11, 12]
print(f'The numbers in the list : {the_numbers_in_the_list}')
The_sum_of_the_even_numbers_in_the_list = 0
for item in the_numbers_in_the_list:
    if not item%2:
            The_sum_of_the_even_numbers_in_the_list += item
print(f'The sum of the even numbers in the list is : {The_sum_of_the_even_numbers_in_the_list}')


# in the color list below
# print out the first and the last color
list_of_colors = ["red", "white", "blue", "green", "orange"]
# print(f'the first color in the list is : {list_of_colors[0]}')
# print(f'the last color in the list is : {list_of_colors[4]}')
# print(f'the first color in the list is : {list_of_colors[0]} and the last color in the list is : {list_of_colors[4]}')
list_of_colors.remove("white")
list_of_colors.remove("blue")
list_of_colors.remove("green")
print(f'The first and last color in the list is : {list_of_colors}')


colorList = ["red", "white", "blue", "green", "orange"]
c = []
a = colorList[1],colorList[-1]
c.append(a)
print(c) 



# in the tuple below in my tuple replace white with gray 

color_tuple = ("red", "white", "blue", "green", "orange", "brown")

color1 = list(color_tuple)
color1[1] = "gray"
color_tuple = tuple(color1)
print(color_tuple)



