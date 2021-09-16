statement1 = "python is a dynamic and interpreted language, it's very easy to learn, python is a multi purpose language."
print(statement1.replace("dynamic", "Interpreted"))
last_index_of_python = statement1.rindex("python")
print(f'the last index of python is : {last_index_of_python}')
check_if_python_is_present_in_statement1 = "python" in statement1
print(f'Is python present in statement1 True or False ??? : {check_if_python_is_present_in_statement1}')
check_if_Golang_is_present_in_statement1 = "Golang" in statement1
print(f'Is Golang present in statement1 True or False ??? : {check_if_Golang_is_present_in_statement1}')





statement2 = "It can be used for various programming jobs like web development, data science, machine learning & python can be used for artificial intelligence"
print(statement2[0:43])
change_artificial_intelligence_to_AI = statement2
print(change_artificial_intelligence_to_AI.replace("artificial intelligence", "AI"))




concatenate_st1_and_str2 = statement1 + statement2
print(concatenate_st1_and_str2)




boldlink_strings = "Boldlink Academy"
string_insert = boldlink_strings.split()
string_insert.insert(1, 'Coding')
string_insert_and_join = ' '.join(string_insert)
print(string_insert_and_join)