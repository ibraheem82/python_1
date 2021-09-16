'''
# A Dictionary is the collection which is unordered, changeable and indexed. No duplicate members.
# similar to object litaral in javascript
# They are always enclosed in an open an close curly bracket
# It allows us to store key, value and pairs
# You must make sure the keys are unique
# The keys can also be numbers
# You can refers to keys and it will bring out the values that is associated with the keys
'''
# person = {
#     'first_name': 'John',
#     'last_name': 'Doe',
#     'age': 30
# }

# Use constructor
# person2 = dict(First_name = 'sara', last_name = 'Williams')


# Get value

# print(person['first_name'])

# # Another way to get value in dictionary
# print(person.get('last_name'))
# # print(person2, type(person2))

# # Add Key/value

# person['phone'] = '081-026-739-64'

# # Get dict keys
# print(person.keys())


# # print(person)


# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December",
# }

# # You can pass in the name of the keys in dictionary.
# print(monthConversions["Nov"])
# print(monthConversions.get("Nov"))
# print(monthConversions.get("hhh"))
# # You can use a default value when the key specified is not found


# print(monthConversions.get("Mon", "Not a valid key"))

# customers = {
#     'name': 'Ibraheem Omikunle',
#     'age': 30,
#     'is_verified': True
# }
# customers['name'] = ['Coder Mern']
# # print(customers['name'])
# # print(customers.get('birthDay', 'May 1 2000'))
# print(customers['name']) 

# phone_numb = input("Phone: ")
# digits_mapping = {

#     '1': 'One',
#     '2': 'Two',
#     '3': 'Three',
#     '4': 'Four',
#     '5': 'Five'

# }
# output = ''
# for characters in phone_numb:
#     output +=  digits_mapping.get(characters, '!') + ' '
# print(output)

# person = {"name": "Jessa", "country": "USA", "telephone": 1178}
# # print(person)
# print(len(person)) 
# print(person.get('telephone'))
# print(person.keys())
# print('key', ':', 'value')
# for key in person:
#     print(key, ':', person[key])
# person1 = dict({"name": "Jessa", "country": "USA", "telephone": 1178})
# print(person1)

# person = dict([("name", "Mark"), ("country", "USA"), ("telephone", 1178)])
# print(person)

# sample_dict = {"name": "Jessa", 10: "Mobile"}
# print(sample_dict)

# person = {"name": "Jessa", "telephones": [1178, 2563, 4569]}
# print(person)
# print(person['name'])
# emptydict = {}
# print(type(emptydict)) 

#  get key value using key name in get()


# person = {"name": "Jessa", 'country': "USA", "telephone": 1178}

# # update dictionary by adding 2 new keys
# person["weight"] = 50
# person.update({"height": 6})

# # print the updated dictionary
# print(person)


# person = {"name": "Jessa", 'country': "USA"}

# # Adding 2 new keys at once
# # pass new keys as dict
# person.update({"weight": 50, "height": 6})
# # print the updated dictionary
# print(person)
# # output {'name': 'Jessa', 'country': 'USA', 'weight': 50, 'height': 6}

# # pass new keys as as list of tuple
# person.update([("city", "Texas"), ("company", "Google",)])
# # print the updated dictionary
# print(person)


# person_details = {"name": "Jessa", "country": "USA", "telephone": 1178}

# # set default value if key doesn't exists
# person_details.setdefault('state', 'Texas')

# # key doesn't exists and value not mentioned. default None
# person_details.setdefault("zip")

# # key exists and value mentioned. doesn't  change value
# person_details.setdefault('country', 'Canada')

# # Display dictionary
# for key, value in person_details.items():
#     print(key, ':', value)


# person = {"name": "Jessa", "country": "USA"}

# # updating the country name
# person["country"] = "Canada"
# # print the updated country
# print(person['country'])
# # Output 'Canada'

# # updating the country name using update() method
# person.update({"country": "USA"})
# # print the updated country
# print(person['country'])
# # Output 'USA'


# person = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50, 'height': 6}

# # Remove last inserted item from the dictionary
# deleted_item = person.popitem()
# print(deleted_item)  # output ('height', 6)
# # display updated dictionary
# print(person)  
# # Output {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50}

# # Remove key 'telephone' from the dictionary
# deleted_item = person.pop('telephone')
# print(deleted_item)  # output 1178
# # display updated dictionary
# print(person)  
# # Output {'name': 'Jessa', 'country': 'USA', 'weight': 50}

# # delete key 'weight'
# del person['weight']
# # display updated dictionary
# print(person)
# # Output {'name': 'Jessa', 'country': 'USA'}

# # remove all item (key-values) from dict
# person.clear()
# # display updated dictionary
# print(person)  # {}

# # Delete the entire dictionary
# del person


# person = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178}

# # Get the list of keys and check if 'country' key is present
# key_name = 'country'
# if key_name in person.keys():
#     print("country name is", person[key_name])
# else:
#     print("Key not found")
# # Output country name is USA


# dict1 = {'Jessa': 70, 'Arul': 80, 'Emma': 55}
# dict2 = {'Kelly': 68, 'Harry': 50, 'Olivia': 66}

# # copy second dictionary into first dictionary
# dict1.update(dict2)
# # printing the updated dictionary
# print(dict1)


# student_dict1 = {'Aadya': 1, 'Arul': 2, }
# student_dict2 = {'Harry': 5, 'Olivia': 6}
# student_dict3 = {'Nancy': 7, 'Perry': 9}

# # join three dictionaries 
# student_dict = {**student_dict1, **student_dict2, **student_dict3}
# # printing the final Merged dictionary
# print(student_dict)


# dict1 = {'Jessa': 70, 'Arul': 80, 'Emma': 55}
# dict2 = {'Kelly': 68, 'Harry': 50, 'Emma': 66}

# # join two dictionaries with some common items
# dict1.update(dict2)
# # printing the updated dictionary
# print(dict1['Emma'])
# # Output 66

# student3 = {
#     "class": {
#         "student": {
#             "name": "Omikunle",
#         }
#     }

# }

# print(student3['class']['student']['name'])


# myfamily = {
#     "child" : {
#         "name": "Ibraheem",
#         "year": 2004
#     }

# }

# print(myfamily['child']['year'])


# student2 = {"name": "Ade"}
# print(student2["name"])


# student1  = {"name" :{"level": "ND1"}}
# print(student1["name"]["level"])


# # Nested dictionary having same keys
# Dict = { 'Dict1': {'name': 'Ali', 'age': '19'},
#          'Dict2': {'name': 'Bob', 'age': '25'}}
# # Prints value corresponding to key 'name' in Dict1
# print(Dict['Dict1']['name'])
# # Prints value corresponding to key 'age' in Dict2
# print(Dict['Dict2']['age'])

# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
#
# x = car.keys()
#
# print(x)  # before the change
#
# car["color"] = "white"
#
# print(x)
#
# applicants = {"Department": {"Faculty": {"student": "Ade", "Level": 200, "age": 30}}}
# print(applicants["Department"]["Faculty"]["student"])

# my_dict = {
#     'name': 'Tim',
#     'name2': 'Ibraheem',
#     'nationality': 'African',
#     'age': 20,
#     'is_tall': 'True',
#     'Qualification': 'college',
#     'friends': ['Peter', 'Paul', 'Precious']
# }
#
# x = my_dict['name']
# print(my_dict['name'])
# print(len(my_dict))
# print(my_dict['is_tall'])
# print(my_dict['friends'])
# print(my_dict)
# print(my_dict)
# print(type(my_dict))
# print(x)




