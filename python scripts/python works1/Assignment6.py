# listA = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = []
# for g in listA:
#     c = g**2
#     b.append(c)
# print(b)


my_list = list([2, 4, 6, 8])
# change value of all items
for i in range(len(my_list)):
    # calculate square of each number
    square = my_list[i] * my_list[i]
    my_list[i] = square

print(my_list)


# names_of_people_in_the_list = ["Abu", "Ibrahim", "John", '', "Ade", '', "Ayo"]
# print(f'The Original :  {names_of_people_in_the_list}')
# the_extracted_names_of_people_in_the_list= list(filter(None, names_of_people_in_the_list))
# print(f'The extracted names of people is the list are : {the_extracted_names_of_people_in_the_list}')



# new_list  = ["John", "", "Ayo", "Jide", "", "Tosin"]
# e = []
# for l in new_list:
#     if l != "":
#         e.append(l)
# print(e)


# # the_real_numbers_in_list= [20, 40, 10, 20, 70, 90, 20, 50]
# # remove_duplicate_the_duplicates_numbers_from_list = set(the_real_numbers_in_list)
# # print(remove_duplicate_the_duplicates_numbers_from_list)


# list_B = [23, 30, 90, 30, 15, 30, 59, 43, 35, 45, 30, 23, 45, 67, 30]
# j = []
# for d in list_B:
#     if d != 30:
#         j.append(d)
# print(j)

# num3 = [10, 20, 40, [70, 80, 90], 200, 300 ]
# num3[3].append(100)
# print(num3)




# list_c  = [10, 20, [300, 400, [5000, 6000],500], 30, 40]
# list_c[2][2].append(7000)
# print(list_c)


# add = [20, 20, [40, 30, 40], 50, 60]
# add[2].append(45)
# print(add)


add1  = [40, 60,[70, [80, 90, 100], 120, 130], 140, 150]
# add1.append(160)
add1[2][1].append(135)

# add1[2][1].append(125)
print(add1)
