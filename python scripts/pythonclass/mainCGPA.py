from tkinter import *
import tkinter.font as tkFont

root = Tk()
root.title('SEMESTER GPA CALCULATOR')
# root.configure(background = "hotpink")
root.geometry('570x350')

# -------------------------------------------------------------------------------------------
# Heading Size Setting
HeadingSize = tkFont.Font(size=10)

# Name endind
NameHeading = Label(text='Enter your Name', font=HeadingSize).grid(row=0, column=0, )
Name = Entry(root, justify='center')
Name.grid(row=0, column=1)
blankLabel = Label(text='      ').grid(row=1, )
# -------------------------------------------------------------------------------------------
# COURSE NAMES HEADING and blank label for spacing out the rows
CourseHeading = Label(text='Courses', font=HeadingSize).grid(row=2, column=1)
blankLabel = Label(text='      ').grid(row=2, column=2)

 # -------------------------------------------------------------------------------------------
 # SCORES HEADING
ScoresHeading = Label(text='Scores (0-100)', font=HeadingSize).grid(row=2, column=3, )
blankLabel2 = Label(text='      ').grid(row=2, column=4)

# -------------------------------------------------------------------------------------------
# Unit HEADING
UnitHeading = Label(text='Course Units', font=HeadingSize).grid(row=2, column=5, )

# -------------------------------------------------------------------------------------------
# COURSE NAME INPUTS
Course1 = Entry(root, justify='center')
Course1.grid(row=3, column=1)
Course1.insert(0, "Course 1")

Course2 = Entry(root, justify='center')
Course2.grid(row=4, column=1)
Course2.insert(0, "Course 2")

Course3 = Entry(root, justify='center')
Course3.grid(row=5, column=1)
Course3.insert(0, "Course 3")

Course4 = Entry(root, justify='center')
Course4.grid(row=6, column=1)
Course4.insert(0, "Course 4")

Course5 = Entry(root, justify='center')
Course5.grid(row=7, column=1)
Course5.insert(0, "Course 5")

Course5 = Entry(root, justify='center')
Course5.grid(row=8, column=1)
Course5.insert(0, "Course 6")

Course5 = Entry(root, justify='center')
Course5.grid(row=9, column=1)
Course5.insert(0, "Course 7")

Course5 = Entry(root, justify='center')
Course5.grid(row=10, column=1)
Course5.insert(0, "Course 8")

Course5 = Entry(root, justify='center')
Course5.grid(row=11, column=1)
Course5.insert(0, "Course 9")

Course5 = Entry(root, justify='center')
Course5.grid(row=12, column=1)
Course5.insert(0, "Course 10")

# -------------------------------------------------------------------------------------------
# Grade inputs
Score1 = Entry(root, justify='center', width=10)
Score1.grid(row=3, column=3)

Score2 = Entry(root, justify='center', width=10)
Score2.grid(row=4, column=3)

Score3 = Entry(root, justify='center', width=10)
Score3.grid(row=5, column=3)

Score4 = Entry(root, justify='center', width=10)
Score4.grid(row=6, column=3)

Score5 = Entry(root, justify='center', width=10)
Score5.grid(row=7, column=3)

Score6 = Entry(root, justify='center', width=10)
Score6.grid(row=8, column=3)

Score7 = Entry(root, justify='center', width=10)
Score7.grid(row=9, column=3)

Score8 = Entry(root, justify='center', width=10)
Score8.grid(row=10, column=3)

Score9 = Entry(root, justify='center', width=10)
Score9.grid(row=11, column=3)

Score10 = Entry(root, justify='center', width=10)
Score10.grid(row=12, column=3)

# -------------------------------------------------------------------------------------------
# Credit inputs
Unit1 = Entry(root, justify='center', width=7)
Unit1.grid(row=3, column=5)
Unit1.insert(0, str(3))

Unit2 = Entry(root, justify='center', width=7)
Unit2.grid(row=4, column=5)
Unit2.insert(0, str(3))

Unit3 = Entry(root, justify='center', width=7)
Unit3.grid(row=5, column=5)
Unit3.insert(0, str(3))

Unit4 = Entry(root, justify='center', width=7)
Unit4.grid(row=6, column=5)
Unit4.insert(0, str(3))

Unit5 = Entry(root, justify='center', width=7)
Unit5.grid(row=7, column=5)
Unit5.insert(0, str(3))

Unit6 = Entry(root, justify='center', width=7)
Unit6.grid(row=8, column=5)
Unit6.insert(0, str(3))

Unit7 = Entry(root, justify='center', width=7)
Unit7.grid(row=9, column=5)
Unit7.insert(0, str(3))

Unit8 = Entry(root, justify='center', width=7)
Unit8.grid(row=10, column=5)
Unit8.insert(0, str(3))

Unit9 = Entry(root, justify='center', width=7)
Unit9.grid(row=11, column=5)
Unit9.insert(0, str(3))

Unit10 = Entry(root, justify='center', width=7)
Unit10.grid(row=12, column=5)
Unit10.insert(0, str(3))


# -------------------------------------------------------------------------------------------
# BUTTON CLICK FUNCTION

def CalculateClick():
    numerator = (int(Score1.get()) * int(Unit1.get())) + (int(Score2.get()) * int(Unit2.get())) + (
                int(Score3.get()) * int(Unit3.get())) + (int(Score4.get()) * int(Unit4.get())) + (
                int(Score5.get()) * int(Unit5.get())) + (int(Score6.get()) * int(Unit6.get())) + (
                int(Score7.get()) * int(Unit7.get())) + (int(Score8.get()) * int(Unit8.get())) + (
                int(Score9.get()) * int(Unit9.get())) + (int(Score10.get()) * int(Unit10.get()))

    denominator = (
                int(Unit1.get()) + int(Unit2.get()) + int(Unit3.get()) + int(Unit4.get()) + int(Unit5.get()) +
                int(Unit6.get()) + int(Unit7.get()) + int(Unit8.get()) + int(Unit9.get()) + int(Unit10.get()))

    Output = Label(text='Your weighted average is ' + str(numerator / denominator), wraplength=100).grid(
        row=14, column=3)

    if (numerator / denominator) >=0 and (numerator / denominator) <= 39:
         return Label(root, text ="Grade Point:" + " " + "0.00" + " " + "Remark:" + " " + "Fail", wraplength=100).grid(row = 14, column = 5)
    if (numerator / denominator) >=40 and (numerator / denominator) <= 44:
         return Label(root, text ="Grade Point:" + " " + "1.00" + " " + "Remark:" + " " + "Pass", wraplength=100).grid(row = 14, column = 5)
    if (numerator / denominator) >=45 and (numerator / denominator) <= 49:
         return Label(root, text ="Grade Point:" + " " + "2.00" + " " + "Remark:" + " " + "3rd Class", wraplength=100).grid(row = 14, column = 5)
    if (numerator / denominator) >=50 and (numerator / denominator) <= 59:
         return Label(root, text ="Grade Point:" + " " + "3.00" + " " + "Remark:" + " " + "2nd Lower", wraplength=120).grid(row = 14, column = 5)
    if (numerator / denominator) >=60 and (numerator / denominator) <= 69:
         return Label(root, text ="Grade Point:" + " " + "4.00" + " " + "Remark:" + " " + "2nd Upper", wraplength=120).grid(row = 14, column = 5)
    if (numerator / denominator) >=70 and (numerator / denominator) <= 100:
         return Label(root, text ="Grade Point:" + " " + "5.00" + " " + "Remark:" + " " + "1st Class", wraplength=100).grid(row = 14, column = 5)

# -----------------------------------------------------------------------------------------------
# Calculate Button
blankLabel3 = Label(text='      ').grid(row=13, column=0)
CalculateButton = Button(root, text='Calculate CGPA', command=lambda: CalculateClick()).grid(row=14, column=1)

blankLabel3 = Label(text='      ').grid(row=14, column=4)

# -----------------------------------------------------------------------------------------------
root.mainloop()

