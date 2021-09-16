# myFile = open('open.py', 'w')


# print('Name: ', myFile.name)
# print('Is Closed : ', myFile.closed)
# print('Opening Mode: ', myFile.mode)


# myFile.write(' Am Ibraheem  Omikunle')
# myFile.write(' And i love Javascript.')
# myFile.close()


# Python has function for creating, reading, updating and deleting files.


# Open a file

# myFile = open('myFile.txt', 'w')


# # get some info

# print('Name', myFile.name)
# print('Is Closed', myFile.closed)
# print('Opening', myFile.mode)

# # Write to file

# myFile.write('I love Python')
# myFile.write(' and Javascript')
# myFile.close()

# # Append to file
# myFile = open('myFile.txt', 'a')
# myFile.write(' I also like PHP')
# myFile.close()


# # Read from file

# myFile = open('myFile.txt', 'r+')

# text = myFile.read(100)
# print(text)


employee_file = open("employees.txt", "r")

print(employee_file.readlines())

employee_file.close()
