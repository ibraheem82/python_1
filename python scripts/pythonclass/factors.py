
# question 1: factors of numbers
def print_factors(x):
    y = []
    print("The factors of", x , "are:")

    for i in range(1, x + 1):
        if x % i == 0:
            y.append(i)
    print(y)

num = 250
print_factors(num)

# Question 2: random number generation

import random
b = []
a = -1
while a != 5999:
    a = random.randint(5999, 6020)
    b.append(a)
print(b)