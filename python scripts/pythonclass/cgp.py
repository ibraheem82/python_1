class Students:

    def __init__(self, name, matric, sem):
        self.name = name
        self.matric = matric
        self.semester = sem

    def personalDetails(self):
        print("Name:{}, Matric No:{}, Semester: {}".format(self.name, self.matric, self.semester))

class Gpcalculator(Students):
    def __init__(self, name, matric, sem, scores_arr, cunit_arr):
        super().__init__(name, matric, sem,)
        self.scores_arr = scores_arr
        self.cunit_arr = cunit_arr
    
    def getGradePoint(self,score):
        if  score >= 40 and score <= 45:
            return 1.5
        if score >= 46 and score <= 49:
            return 2.0
        if  score >= 50 and score <= 55:
            return 2.5
        if  score >= 56 and score <= 59:
            return 3.0
        if  score >= 60 and score <= 65:
            return 3.5
        if  score >= 66 and score <= 69:
            return 4.0
        if  score >= 70 and score <= 75:
            return 4.5
        if  score >= 76: 
            return 5.0

    def getCgp(self):
        tgp = 0.0
        cgp = 0.0
        for i in range(len(self.scores_arr)):
            tgp += self.getGradePoint(self.scores_arr[i]) * self.cunit_arr[i]
        cgp += tgp / sum(self.cunit_arr)
        print(self.personalDetails(), "\n", "Cumulative GradePoint is:{}".format(cgp))

cgp = Gpcalculator("Ayodele John", "DFP100220", "First", [86, 60, 79, 58], [2,3, 2, 2])
cgp.getCgp()






