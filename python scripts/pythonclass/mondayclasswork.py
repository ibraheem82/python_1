# Question 1
# Print out first ten natural numbers using while loop
a = 1
while a <= 10:
    print(a)
    a += 1

# Question 2
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
c = []
for b in list1:
    if b % 5 == 0 and b <= 150:
        c.append(b)
print("Multipls of fives and less or equal to 150:", c)        

# Question 3
f = []
for d in range(1, 6 + 1):
    e = x = pow(d, 3)
    f.append(e)
print(f)

# # Question 4
# # to display even position
g = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for h in range(1, len(g), 2):    
    print(g[h])   

# Question 5
for j in range(-10, 0, 1):
    print(j, end= " ")

    # Question 6
my_string = "Boldlinks"
for n in my_string:
    if (my_string.index(n) % 2 == 0):
     print(n, end=" ")


# Question 7: 
for i in range(7):
    print(i)
print("done")   


# Question 8: Display all prime numbers whithin 25 and 50
start = 25
end = 50

for num in range(start,end + 1):
    if(num > 1):
        for x in range(2,num):
            if(num % x == 0):
                break
        else:
            print(num)

