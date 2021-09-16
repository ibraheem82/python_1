# # x = 15
# # y = 2

# # print(x // y)
# x = 5

# print(x > 3 and x < 10)


# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()

# mylist.append('Pineapple')
# print(mylist)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#     list1.append(x)

# print(list1)

x = ("apple", "banana", "cherry", "pineapple", "mango")
y = list(x)
y.insert(-3, "cucumber")
x = tuple(y)
print(x)

# cars_name = ("benz", "jeep", "venza", "toyota")
# # for x in cars_name:
# #     print(x)
# print(len(cars_name))
# print(type(cars_name))
# if "benz" in cars_name:
#         print(f'benz is in cars_name')