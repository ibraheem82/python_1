# Using oop Concept find the mean, mode, median and the range of the following
# numbers[8, 5, 7, 9, 5, 1, 5]

class Statistics:
    def __init__(self, rec):
        self.sample = [float(x) for x in rec]

    def my_mean(self):
        return sum(self.sample) / len(self.sample)

    def my_range(self):
        return max(self.sample) - min(self.sample)

    def my_median(self):
         lensample = len(sorted(self.sample))
         items_sample = sorted(self.sample)
         if (lensample % 2 == 0):
             indexOne = lensample/2
             indexTwo = indexOne - 1

             firstVal = items_sample[int(indexOne)]
             secondVal = items_sample[int(indexTwo)]

             ans = firstVal + secondVal
             return ans/2

         else:
            middleIndex = lensample//2
            middle_no = items_sample[middleIndex]
            return middle_no

    def my_mode(self):
        dict_vals = {}
        for i in self.sample:
            if (i not in dict_vals):
                dict_vals.update({i:self.sample.count(i)})
        max_value = max(dict_vals.values())

        for key,value in dict_vals.items():
            if(value == max_value):
                return key

             

   
statObj = Statistics([8, 5, 7, 9, 5, 1, 5, 11, 20, 20, 20, 20, 20, 30, 46])
print("Mean", statObj.my_mean(),"\n")
print("Median", statObj.my_median(),"\n")
print("Mode", statObj.my_mode(),"\n")
print("Range", statObj.my_range(),"\n")

          

from tkinter import*
from statistics import*

root = Tk()
root.configure(background = "hotpink")
root.title("STATISTICS ")

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