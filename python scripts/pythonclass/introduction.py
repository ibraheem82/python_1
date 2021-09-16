a = 200
b = 60
print(a + b) 
print(a*b)
print(a/b)
print(a*b/b)   
print(a+b-b)

x, y, z, p = 30, 40, 50, "Ade" 
print (x,y,z)
print(a+b)
print(x+y)
print(p)
Fruits = ["Mango", "Guava", "Orange", "Water mellon", "Apple"]
print(Fruits)

Names = "ayo", "ade", "john"
print(Names)


Teacher = "Good morning class"
Class = "Good morning"
print(Teacher)
print(Class + " " + "Mr Aderibigbe")
print(Class *2)
print(Teacher[4:])
print(Teacher[4:12])


# python list
ade = [80, 100, 200, 300, 400, "Abu", "Sala", 500.2]
ayo = ["father", "mother", "age", 70, 90]
print(ade)
print(ade + ayo)
print(ade[2:3])
print(ade[1:4] + ayo[1:3])

# python Dictionary
anu = {}
anu[1] = "My daughter is two years"
anu["sister"] = "She is my daughter"

print(anu[1])
print(anu[1] + " " + anu["sister"])

# Addition, subtraction and if statement
num1 = 450
num2 = 250
num3 = 300
ans = num1 - num2
print(ans)
if ans > num3:
    print(ans,"is greater than",num3)
else: print(ans,"is less than",num3) 

# Question 2
num4 = 10
num5 = 6
val = 100
product = num4 * num5
print(product)
if product < val:
    print(product + val)
else: print(product, "is greater than",val)

# class work 3
# Return the number of times "Tope" apears in the following string 
# "Tope is a good developer. although Tope can also be a lazy"

developer = "Tope is a good developer. although Tope can also be a lazy"
Tope = developer.count("Tope") 
print( "Tope appears", Tope, "times" )

# OR
Programer = "Tope is a good developer. although Tope can also be a lazy"
txt = Programer.count("Tope") 
addtext = "Tope appers {} times "
print(addtext.format(txt))

# assignment
# str = "B@#o126at^&1SliN*ks"


# # a_string = "B@#o126at^&1SliN*ks"
# def numberfromstring(string_a):
#      n=list(string_a)
#      for i in n:
#          if i.isdigit():
#              k=int(i)
#              print(k)

# A="B@#o126at^&1SliN*ks"
# numberfromstring(A)

# # initializing string  
# test_string = "There are 2 apples for 4 persons"
  
# # printing original string  
# print("The original string : " + test_string) 
  
# # using List comprehension + isdigit() +split() 
# # getting numbers from string  
# res = [int(i) for i in test_string.split() if i.isdigit()] 
  
# # print result 
# print("The numbers list is : " + str(res)) 


stringA =  "B@#o126at^&1SliN*ks"
# Given string
print("Given string : ", stringA)
# Find characters
letter = ""
for i in stringA:
    if i.isalpha():
        letter= "".join([letter, i])
counter = 0
for i in stringA:
      counter = counter+1
letterNo = 0
for i in letter:
    letterNo = letterNo+1
# Result
print("Length of the input string is:", counter)
print("letters: ", letter)
print("Number of letters is",letterNo)

# Digits
stringA =  "B@#o126at^&1SliN*ks"
# Given string
print("Given string : ", stringA)
# Find digits
res = ""
for i in stringA:
    if i.isnumeric():
        res = "".join([res, i])
        digitCounter = 0
for i in res:
     digitCounter = digitCounter+1
# Result
print("Digits: ", res)
print("Number of digits is",digitCounter)

# special characters
stringA =  "B@#o126at^&1SliN*ks"
# Given string
print("Given string : ", stringA)
# Find digits
res = ""
for i in stringA:
    if not i.isnumeric() and not i.isalpha():
        res = "".join([res, i])
        special = 0
        for i in res:
            special = special+1        
print("special characters: ", res)
print("Number of special characters is",special)

# Question2 (reverse string)
school = "BoldlinksAcademy" [::-1] 
print(school)

# Quuestion 3 
course = "PHP = 78 Python = 89 Ruby = 63 Perl = 60 Javascript = 90"
new = dict(enumerate(course))
print(new)
scores = {'PHP':78, "Python":89, "Ruby":63, "Perl":60, "javascript":90}
value1 = scores.values()
subjects = scores.keys()
total = sum(value1)
average = total/len(value1)
print(value1)
print(total)
print(average)
print(subjects)


# correction
stmt = "B@#o126at^&1SliN*ks"
alphalCount = 0
digitCount  = 0
symCount    = 0

for char in stmt:
    if char.isalpha():
        alphalCount+= 1
    elif char.isnumeric():
       digitCount+= 1
    else:
        symCount+= 1
print("letters =",alphalCount)
print("Numbers =",digitCount)
print("symbol =",symCount)
                
            # Correction 2
courses = "PHP = 78 Python = 89 Ruby = 63 Perl = 60 Javascript = 90"
courses_split = courses.split(" ")
sumNum = 0
sumLen = 0
for numItem in courses_split:
    if (numItem.isnumeric()):
        sumNum += int(numItem)
        sumLen += 1
averageScore = sumNum / sumLen
print(sumNum) 
print(averageScore)        


StudentsNames = "suliat, tope, pelumi,toheeb"
Capital = StudentsNames.capitalize()
print(Capital)


randChar = "SOLIAH 20 lady"
randCharsplit = randChar.split(" ")
for capi in randCharsplit:
    if(capi.isupper()):
        print(capi)
    elif(capi.islower()):
        print(capi)
    else:
        print(capi)


