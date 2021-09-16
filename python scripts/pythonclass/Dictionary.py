student1 = {
    "Name": "Ade",
    "Level": "100L",
    "Course": "CSC",
    "Matric No": 123654,
    "Course Duration": 5,
}

y = list(student1)
x = student1["Name"]
z = student1["Matric No"]
a = student1.keys()
b = student1.values()
student1["Matri No"] = "9001AB"
print(student1)
print(y)
print(len(student1))
print(type(student1))
print(x)
print(z)
print(a)
print(b)
print(student1)
print(student1.items())


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x)