total_init_num = 0
num_A = [11,5,17,18,23]
for numbers in range(0, len(num_A)):
    total_init_num += num_A[numbers]
print("Sum of all elements in given list: ", total_init_num)




list1 = [11, 5, 17, 18, 23]
# using sum() function
total = sum(list1)
# printing total value
print("Sum of all elements in given list: ", total)



list_of_numbers = [10, 20, 4, 45, 99]
list_of_numbers.sort()
smallest_number_in_the_list_A = list_of_numbers[0]
highest_number_in_the_list__B = list_of_numbers[-1]
print(f'The lowest number is {smallest_number_in_the_list_A}')
print(f'The highest number is {highest_number_in_the_list__B}')