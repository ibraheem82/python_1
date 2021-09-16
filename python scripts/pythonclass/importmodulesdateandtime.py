from mymodule1 import *
import datetime 
from datetime import datetime, timedelta
import math
from function import*
from mondayclasswork import*

# import function

print(greetings())
print(students)
print(students["name"])
# print(math)
a = datetime.now()
print(a)
print(a.year)
print(a.strftime("%Y"))
x = datetime(2018, 6, 1)

print(x.strftime("%B"))
print(x)
y = datetime.now()
print(y)

# Question 1
# convert string into a datetime objobject 
# output should be like 2020-02-25 16:20:00
date_strng = "feb 25 2020 4:20pm"
b = datetime.strptime(date_strng,"%b %d %Y %H:%M%p" )
print(b)

# Question 2
# print out a date in the following format 
# output should be like Tuesday 25 febuary 2020
c = datetime(2020, 4, 17)
print(c.strftime( "%A %d %B %Y"))

# Question 6. print out the current date in this format
# Tuesday 25 febuary 
e = datetime.now()
print(e.strftime("%A %d %B %Y"))

# Question 4: Find the day of week of a given date
give_date = "2020, 7, 26" 
f = datetime(2020, 7, 26)
print(f.strftime("%A"))

# Question 5
# subtract a week .. 7days from given date  in python
sub_date = datetime(2020, 2, 25)
sub = timedelta(7)
new = sub_date - sub
print(new)

# Assignment
# add 7 days and 12 hours to a given date 
# 2020 - 03 - 22 10:00:00
add_newdate = datetime(2020, 3, 22, 10, 0, 0)
add = timedelta(7.5)
new_add = add + add_newdate
print(new_add)


# content = dir(math)
# print(content)
sum_ave()
getSumAve("Toheeb",60, 73, 35, 69)
print(num)