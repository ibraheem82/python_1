from tkinter import*
from shape import*

root = Tk()
root.configure(background = "red")
root.title("Perimeter Of a Trapezium")

Title = Label(root, text = "Perimeter of a trapezium",font = 40, width = 30, bg = "red")
Title.grid(row = 0, column = 3, columnspan = 5)

L1 = Label(root, text = "Side1", font = 30, bg = "red")
L1.grid(row = 1, column = 1)

# L_space = Label(root, text = " ", font = 30, bg = "red")
# L_space.grid(row = 1, column = 4)

input1 = Entry(root, width = 10, font = 30,)
input1.grid(row = 1, column =4)

L2 = Label(root, text = "Side2", font = 30, bg = "red")
L2.grid(row = 2, column = 1)

# L2_space = Label(root, text = " ", font = 30, bg = "red")
# L2_space.grid(row = 2, column = 4)

input2 = Entry(root, width = 10, font = 30,)
input2.grid(row = 2, column =4)

L3 = Label(root, text = "Side3", font = 30, bg = "red")
L3.grid(row = 3, column = 1)

# L3_space = Label(root, text = " ", font = 30, bg = "red")
# L3_space.grid(row = 3, column = 4)

input3 = Entry(root, width = 10, font = 30,)
input3.grid(row = 3, column =4)

L4 = Label(root, text = "Side4", font = 30, bg = "red")
L4.grid(row = 4, column = 1)

# L3_space = Label(root, text = " ", font = 30, bg = "red")
# L3_space.grid(row = 3, column = 4)

input4 = Entry(root, width = 10, font = 30,)
input4.grid(row = 4, column =4)


def calculatePer():
    side1 = float(input1.get())
    side2 = float(input2.get())
    side3 = float(input3.get())
    side4 = float(input4.get())
    result2 = peri_Trapezoid( side1 ,side2 , side3 ,side4 )
    tri_area =  result2.peri_par()
    Ans = Label(root, text = tri_area, font = 30, bg = "red")
    Ans.grid(row = 5, column = 4)

btnClick = Button(root, text = "Calculate", width = 10, bg = "yellow", command = calculatePer)
btnClick.grid(row = 6, column = 1)

root.mainloop()
