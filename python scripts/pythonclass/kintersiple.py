from tkinter import*
from simpleinterest import*

root = Tk()
root.configure(background = "cyan")
root.title("Simple Interest")

Title = Label(root, text = "Simple Interest",font = 40, width = 30, bg = "cyan")
Title.grid(row = 0, column = 3, columnspan = 5)

pL = Label(root, text = "Principal", font = 30, bg = "cyan")
pL.grid(row = 1, column = 1)
input1 = Entry(root, width = 10, font = 30,)
input1.grid(row = 1, column =4)

rL = Label(root, text = "Rate", font = 30, bg = "cyan")
rL.grid(row = 2, column = 1)
input2 = Entry(root, width = 10, font = 30,)
input2.grid(row = 2, column =4)

tL = Label(root, text = "Time", font = 30, bg = "cyan")
tL.grid(row = 3, column = 1)
input3 = Entry(root, width = 10, font = 30,)
input3.grid(row = 3, column =4)


def calculateSI():
    p = float(input1.get())
    t = float(input2.get())
    r = float(input3.get())
    interest = Simple_interest(p, r,t)
    Ans = Label(root, text = interest, font = 30, bg = "red")
    Ans.grid(row = 5, column = 4)

btnClick = Button(root, text = "Calculate", width = 10, bg = "yellow", command = calculateSI)
btnClick.grid(row = 6, column = 1)

root.mainloop()