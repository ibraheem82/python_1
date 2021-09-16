
# # # # Assignment
# # Question1
# def countvowel(str):
#         num_vowel = 0
#         for char in str:
#             if char in "aeiouAEIOU":
#                num_vowel = num_vowel + 1
#         return num_vowel
# student_Name = ["ibrahim", "joy", "pelumi", "jayeola", "adam", "shukrah", "isha", "tope", "adeola", "tohib",]
# vowel_count = {}
# for str in student_Name:
#         vowel_count[str] = countvowel(str)
# print(vowel_count)

# # Question 2
# class_list = [["Pelumi", "Male","Teen"],["Friday","Male", "Adult",],["Daji","Male","Adult"],["Soliah", "Female","Teen"]]
# teen = adult =  0
# teens = "Teen"
# adults = "Adult"
# for i in class_list:
#     if i.count(teens):
#         teen = teen + 1
#     else:
#         adult = adult + 1
# print("Number of teenagers are:",teen)
# print("Number of teenagers are:",adult)

# male = female =  0
# no_male = "Male"
# no_female = "Female"
# for y in class_list:
#     if y.count(no_female):
#         female = female + 1
#     else:
#         male = male + 1
# print("Number of female are:",female)
# print("number of male are:",male)

# # # Question 3
# # for x in class_list:
# #  print(class_list)    

# # Assignment correction
# className = ["ibrahim", "joy", "pelumi", "jayeola", "adam", "shukrah", "isha", "tope", "adeola", "tohib",]
# volwels = ["a","e","i","o","u","A","E","I","O","U"]
# for i in className:
#     no_of_occur = 0
#     for j in volwels:
#         if j in i:
#             no_of_occur = no_of_occur + i.count(j)
#     print("No of vowels in ", i,"is", no_of_occur)
   
# # Question 2
# class_level = [
#     ["Pelumi", "Male","Teen"],
#     ["Friday","Male", "Adult"],
#     ["Daji","Male","Adult"],
#     ["Soliah", "Female","Teen"],
#     ["Adam", "Male","Teen"],
#     ["Solomon","Male", "Adult"],
#     ["Damilola","Male","Adult"],
#     ["Shukrah", "Female","Teen"],
#     ["Toheeb", "Male","Teen"],
#     ["Larry","Male", "Adult"],
#     ["Sahad","Male","Adult"],
#     ["Isha", "Female","Teen"]
#     ]

# # Find those who are adults, teens, female, and male 
# male_list = []
# female_list = []
# adult_list = []
# teen_list = []
# for x in class_level:
#     if "Male" in x:
#         male_list.append(x[0])
#     if "Female" in x:
#          female_list.append(x[0])
#     if "Adult" in x:
#          adult_list.append(x[0])
#     if "Teen" in x:
#          teen_list.append(x[0])

# print("The male list consist of", male_list, "with total number of ", len(male_list),"student")
# print("The female list consist of", female_list, "with total number of ", len(female_list),"student")
# print("The adult list consist of", adult_list, "with total number of ",len(adult_list),"student")
# print("The teen list consist of", teen_list, "with total number of ",len(teen_list),"student")

# # class work
# numlist = [4, 5, 6, 7, 8, 9, 10, 11, 12]
# all_even = []
# total_sum = 0
# for item in numlist:
#     if item % 2 == 0:
#         all_even.append(item)
#         total_sum += item
# print(all_even)
# print("Total sum of all even nos which are", all_even, "is", total_sum)

# # Assignment (Monday Assignment)
# print("Assignment (Monday Assignment)")

# for n in range(1,101):
#     print(n)  
# p = []
# sumP = 0
# for m in range(1,101):
#     if m % 7 == 0:
#         p.append(m)
#         sumP += m
# print("Multiples of seven are:",p)
# print("Sum of multiples of seven within 1-100 are: ",sumP)

# # Question 2
# print("Question 2")
# R = [23, 18, 90, 20, 15, 35, 59, 43, 35, 45]
# u = []
# sum_u = 0
# print("The items in the list are:",len(R))
# for t in R:
#     if t >= 20 and t <= 40:
#         u.append(t)
#         sum_u += t
# print("Numbers within 20-40 in the list above are:",u)
# print("The sum of number are:",sum_u)
# print("The numbers that in the range of 20-40 are:",len(u)) 

# # class work
# print("Question ")
# v = [23, 18, 90, 20, 15, 35, 59, 43, 35, 45]
# w = []
# for q in v:
#     if  q % 5 == 0:
#         w.append(q)
# print(w)

# y =[z for z in v if z % 5 == 0]
# print(y)

# # Question 2
# # add 7000 after 6000
# # numList [10, 20, [300, 400, [5000, 6000],500], 30, 40]
# # # in the list below print out the squre of each number
# # numSqr [1, 2, 3, 4, 5, 6, 7, 8, 9,]
# # # in the list below remove the empty strings and return the remaining list
# # nwe_list = ["John", " ", "Ayo", "Jide", " ", "Tosin"]

# # Question 2
# numSqr = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
# b = []
# for g in numSqr:
#     c = g**2
#     b.append(c)
# print(b)

# # Question 3
# new_list = ["John", "", "Ayo", "Jide", "", "Tosin"]
# e = []
# for l in new_list:
#      if l != "":
#       e.append(l)
# print(e)         

# # Method 2 question 3
# new_list = list(filter(None,new_list))
# print(new_list)


# # Question 1
# numList = [10, 20, [300, 400, [5000, 6000],500], 30, 40]
# numList[2][2].append(7000)
# print(numList)

# # Assignment
# # Question 1: in the list below remove all occurece of 30
# listA = [23, 30, 90, 30, 15, 30, 59, 43, 35, 45, 30, 23, 45, 67, 30]
# j = []
# for d in listA:
#     if d != 30:
#      j.append(d)
# print(j)

# #  Question 2
# # in this list below add the missing "h", "i", "j" to make complete
# alpha1 = ["a", "b", ["c",["d", "e",["f,","g"],"k"], "l"],"m", "n"] 
# alpha1[2][1][2].extend("h" "i" "j")
# print(alpha1)


# class work
# create a tuple with a single item 100

# tuple1 = ("100",)
# print(type(tuple1))

# # print out the the number 50  from the tupple below
# rtype = ("orange",[20, 30, 50],(5, 20, 23))
# nlist = rtype[1][2]
# print(nlist)

# # count the number of the 50 occurs in this turple
# tCount = (50, 10, 60, 70, 50)
# lCount = tCount.count(50)
# print(lCount)

# # in the tuple below copy element 44 and 55 in to new tuple
# tuple2 = (11, 22, 33, 44, 55, 66)
# tuple3 = tuple2[3:-1]
# print(tuple3)


# class work
# Question 1: add a list of items into a given set
set1 = {"Black", "Orange", "Yellow"}
set2 = {"Green", "Blue", "Red"}

setA = set1.union(set2)
print(setA)

# Question 2 return thhe identical items in the following set
set3 = {10, 20 ,30, 40, 50}
set4 = {30, 40 ,50, 60, 70}

setB = set3.intersection(set4)

print(setB)


# Question 3 return new sets by removing duplication
set5 = {10, 20 ,30, 40, 50}
set6 = {30, 40 ,30, 40, 50, 60, 70,}

setC = set5.union(set6)
print(setC)


# Question 4 update new sets by adding, items newset8  except common
set7 = {10, 20 ,30, 40, 50}
set8 = {30, 40 ,30, 40, 50, 60, 70,}

set7.symmetric_difference_update(set8)

print(set7)


# question6 
# Remove 10, 20, 30 element from the following set  at once showing only 40, 50

mainset1 = {10, 20 ,30, 40, 50}

mainset2 = {10, 20 ,30,}
mainset1.difference_update(mainset2)

print(mainset1)



