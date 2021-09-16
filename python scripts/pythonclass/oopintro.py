# defining my class file person
class person:
  
## defining constructor method
    def __init__(self, name,eyeColor,legtype):
        self.name = name
        self.eyeColor = eyeColor
        self.legtype = legtype
# defining user_defined method "getname"
    def getname(self):
        return self.name

    def dancing(self):
        print(self.name, "with", self.eyeColor, "colored eye is dancng with", self.legtype, "leg")

# person_A = person("Olanrewaju","red", "short") #class intantiation to object person_A
# print(person_A.getname()) #person_A object is calling getname()
# person_A.dancing()


class Employee:
  
## defining constructor method
    def __init__(self, fullname,salary,role):
        self.fullname = fullname
        self.salary = salary
        self.role = role
# defining user_defined method "getname"
    def getfullname(self):
        return self.fullname

    def salaryEmp(self):
        print(self.fullname, "earns", self.salary, "for a ", self.role, "in a First Bank")

Employee_A = Employee("Mr Yakub",200000, "Manager") #class intantiation to object person_A
Employee_A.salaryEmp()

Employee_B = Employee("Mr Adekunle",220000, "Programer") #class intantiation to object person_A
Employee_B.salaryEmp()

Employee_C = Employee("Mr Tope",150000, "Code Editor") #class intantiation to object person_A
Employee_C.salaryEmp()



