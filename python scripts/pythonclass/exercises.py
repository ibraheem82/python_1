# Question 1
# Question 1: Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum
A = 60
B = 100
product = A * B
if product > 1000:
  print (A + B)
else:
  print(product)     
    

# Question 2: Given a range of first 10 numbers, Iterate from start number to the end number and print the
# sum of the current number and previous number

# def sumNum(num):
#     previousNum = 0
#     for i in range(num):
#         sum = previousNum + i
#         print("Current Number", i, "Previous Number ", previousNum," Sum: ", sum)
#         previousNum = i

# print("Printing current and previous number sum in a given range(10)")
# sumNum(10)
 

# Question 3: Given a string, display only those characters which are present at an even index number.
# str = "pynative"

# Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5s

# Boolean Practices
numA = 450
numB = 900
if numA > numB:
  print("numA is greater than numB")
else:
  print("numA is less than numB ")

a = 0
b = ()
c = {}
d = []
e = 1
f = "ade"
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))

char =["ade", "abu", "ayo", "toheeb", "solihat"]
char.remove("ade")
char.append("sala")
print(char)

names1 =["ade", "abu", "ayo", "toheeb", "solihat"]
names2 = ["Abudsalam", "Pelumi", "Kafayat", "Raheemat", "Pelumi"]
names1.extend(names2)
print(names1)

studentNames = ["ade", "abu", "ayo", "toheeb", "solihat", "Kafayat", "Raheemat", "Pelumi"]
studentNames[2:3] = ["Rasheedat", "Ishat", "Shukra", "Rukayat"]
print(studentNames)

classname = ["ade", "abu", "ayo", "toheeb", "solihat", "kafayat", "raheemat", "pelumi"]
classname.sort()
print(classname)

numSet = [45, 67, 98, 54, 34, 100, 76, 12]
numSet.sort()
print(numSet)