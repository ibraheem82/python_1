from tkinter import*
from statistics import*

root = Tk()
root.configure(background = "hotpink")
root.title("STATISTICS")

root.rowconfigure(4, minsize = "50")
root.columnconfigure([0,1,2,3,4,5,6], minsize = "50")


Title = Label(root, text = "STATISTICS CALCULATOR",font =40, bg = "hotpink", )
Title.grid(row = 0, column = 3)

input = Entry(root, width = 40,)
input.grid(row = 1, column =3)

mean =Label(root, text = "Mean", font = 30, bg = "hotpink",)
mean.grid(row = 3, column =1)

space = Label(root, text = " ", font = 30, bg = "hotpink")
space.grid(row = 3, column = 2)

mode =Label(root, text = "Mode", font = 30, bg = "hotpink",)
mode.grid(row = 3, column =3)

median =Label(root, text = "Median", font = 30, bg = "hotpink",)
median.grid(row = 3, column =4)

space1 = Label(root, text = " ", font = 30, bg = "hotpink")
space1.grid(row = 3, column = 5)

range1 =Label(root, text = "Range", font = 30, bg = "hotpink",)
range1.grid(row = 3, column =6)

def getStat():
    inputs = input.get().split(',')
    Ans = Statistics(inputs)
    mean = Ans.my_mean()
    mode = Ans.my_mode()
    median = Ans.my_median()
    ranges = Ans.my_range()
    MeanAns = Label(root, text = mean, font = 30, bg = "hotpink",)
    MeanAns.grid(row = 4, column = 1)
    ModeAns = Label(root, text = mode, font = 30, bg = "hotpink",)
    ModeAns.grid(row = 4, column = 3)
    MedianAns = Label(root, text = median, font = 30, bg = "hotpink",)
    MedianAns.grid(row = 4, column = 4)
    RangeAns = Label(root, text = ranges, font = 30, bg = "hotpink",)
    RangeAns.grid(row = 4, column = 6)

btnClick = Button(root, text = "Calculate", width = 10, bg = "green", fg = "#fff",command=getStat)
btnClick.grid(row = 2, column = 3, padx = 10, pady = 10)
root.mainloop()