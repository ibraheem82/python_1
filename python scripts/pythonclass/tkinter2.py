from tkinter import*
from shape import*

root = Tk()
root.configure(background = "red")
root.title("Area of a triangle")

Title = Label(root, text = "Area of a triangle",font = 40, width = 30, bg = "red")
Title.grid(row = 0, column = 3, columnspan = 5)

b1 = Label(root, text = "Base", font = 30, bg = "red")
b1.grid(row = 1, column = 1)

b_space = Label(root, text = " ", font = 30, bg = "red")
b_space.grid(row = 1, column = 4)

b2 = Entry(root, width = 10, font = 30,)
b2.grid(row = 1, column =4)

h1 = Label(root, text="Hight", font = 30, bg = "red")
h1.grid(row = 2, column = 1)

h_space = Label(root, text = " ", font = 30, bg = "red")
h_space.grid(row = 2, column = 1)

h2 = Entry(root, width = 10, font = 30,)
h2.grid(row = 2, column = 4)


def calculateTr():
    base = float(b2.get())
    height = float(h2.get())
    result3 = Triangle(base,height)
    tri_area = result3.area()
    Ans = Label(root, text = tri_area, font = 30, bg = "red")
    Ans.grid(row = 4, column = 4)

btnClick = Button(root, text = "Calculate", width = 10, bg = "yellow", command = calculateTr)
btnClick.grid(row = 4, column = 1)

root.mainloop()

