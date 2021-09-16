statement1 = "Python is a dynamic and interpreted language, it is very easy to learn. Python is a multipurposelanguage"
statement2 = "It can be used for various programming jobs like web development, data science, machine learning & Python can be used for artificial intelligence"

# Class work
# 1: check str1 and change "dynamic" to "interpreted"

print(statement1.replace("dynamic","interpreted"))

# 2: check str1 and  find the last occurence of "python"

print(statement1.rfind("Python"))

# 3: check if the word python is present in str1
present = "Python" in statement1
print(present)

# 4: check if the word Golang  is present in str1
present2 = "Golang" in statement1
print(present2)

# 5: inside str2 slice out the phrase "It can be used for various programming jobs"
print(statement2[0:43])

# 6: check str2 and change "artificial intelligence" to "AI"
print(statement2.replace("artificial intelligence","AI"))

# Concatenate str1 and str2 to form a single string
print(statement1 + " " + statement2)

# part 2 
# Insert the new word into the space between Boldlink Academy
Sch_name = "Boldlink  Academy"
new_word = "Coding"
my_new_word = Sch_name[:10] + new_word + Sch_name[9:]
print(my_new_word)

