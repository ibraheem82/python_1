class University_ib:
  def __init__(self, students, academic_staffs, non_academic):
    self.students = students
    self.academic_staffs = academic_staffs 
    self.non_academic = non_academic

  def stakeholders(self):
    print("Number of students", self.students,",", "Number of Lecturers", self.academic_staffs, ",", "Number of Non-Teaching staffs", self.non_academic)

info= University_ib(200, 50,  100)
info.stakeholders()

class StudentsInfo(University_ib):
  def __init__(self,students, academic_staffs, non_academic, fname, lname, level, department, faculty, mat_No):
    super().__init__(students, academic_staffs, non_academic,)
    self.fname = fname
    self.lname = lname
    self.level = level
    self.department = department
    self.faculty = faculty
    self.mat_No = mat_No

  def studentsInfomation(self):
    print("Number of students", self.students,",", "Number of Lecturers", self.academic_staffs, ",", "Number of Non-Teaching staffs", self.non_academic, "Name", self.fname, self.lname, "class",self.level, "Department", self.department, "faculty",self.faculty, "Matric-No",self.mat_No)

std= StudentsInfo( 400, 50, 300, "Ade", "Olanrewaju", "200L", "computer", "Science", 236611,)
std.studentsInfomation()
