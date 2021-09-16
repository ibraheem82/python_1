def new_list(name):
    for i in name:
        print(i)


num_count = [1, 2, 3, 4, 5, 6]
new_list(num_count)


#  Question 6:  simple interest
def si(p, t, r):
    print("Simple interet = ", (p * t * r) / 100)


si(450, 5, 6)


# Question 1
def addsub(a, b):
    print((a + b), (a - b))


addsub(50, 30)


# Question 3

def evens(i):
    if i > 30:
        return
    print(i)
    evens(i + 2)


evens(4)

# # method 2
range_num = range(4, 30, +1)


def even_num(start, end):
    even = []
    for q in range(start, end):
        if q % 2 == 0:
            even.append(q)
    print(even)


even_num(4, 30)


# Question 4
def large_num():
    a_list = [4, 6, 8, 24, 12, 2]
    print("highest number: = ", max(a_list))


large_num()


# Question 5
def display_student(name, age):
    print(name, age)


display_student("john", 34)
show_student = display_student
show_student("john", 34)


# question 2
def showEmployee(name, salary=9000):
    print("my name is ", name, "and as a spolt child I stole", salary, "naira")


showEmployee("Adeeyo")

# def addSub(a,b):
#     print((a+b),(a-b))
# addSub(50,30)

# Assignmen function
print("Assignment")


def sum_ave():
    Tope = [75, 60, 65, 79]
    Salam = [62, 43, 50, 86]
    Soliah = [46, 72, 53, 76]
    Damy = [55, 39, 67, 70]
    Toheeb = [60, 73, 35, 69]
    print("Tope total score:", sum(Tope), "ave:", sum(Tope) / len(Tope))
    print("Salam total score:", sum(Salam), "ave:", sum(Salam) / len(Salam))
    print("Soliah total score:", sum(Soliah), "ave:", sum(Soliah) / len(Soliah))
    print("Damy total score:", sum(Damy), "ave:", sum(Damy) / len(Damy))
    print("Toheeb total score:", sum(Toheeb), "ave:", sum(Toheeb) / len(Toheeb))


# Method 2
print("Method2")


def getSumAve(name, html, css, js, python):
    sumNo = html + css + js + python
    aveNum = sumNo / 4
    print(name, "Total sum is:", sumNo, "and the average is:", aveNum)


getSumAve("Tope", 75, 60, 65, 79)
getSumAve("Salam", 62, 43, 50, 86)
getSumAve("Soliah", 46, 72, 53, 76)
getSumAve("Damy", 55, 39, 67, 70)
getSumAve("Toheeb", 60, 73, 35, 69)

# Lambda function
addNum = lambda a, b: a + b
print(addNum(45, 90))


# Example2
def num(i):
    return lambda a: a * i


res = num(5)
print(res(10))

# Example 3
# print out even number
mylist = [1, 2, 3, 4, 5, 6, 7, 8]
evens = filter(lambda num: num % 2 == 0, mylist)
print(list(evens))

# class work
newList = [2, 4, 5, 7, 10, 15, 18, 25]
below = lambda r: r < 18
result = filter(below, newList)
print(list(result))

# question 2
# using a normal function return the numbers equal to or above 18 inside a new list

# myList = [2, 14, 5, 17, 20, 15, 18, 25, 30, 12, 45]
# def greater(myList):
#   for item in myList:
#     if item >= 18:
#       y = filter(item, myList)
# print(list(y))         
# greater(myList)

# print(result)
# greater()
