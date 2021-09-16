from tkinter import*

root = Tk()
root.title("GP CALCULATOR")
root.configure(background = "orangered")
root.geometry("500x500")

myfirstLabel = Label(root, text = "My first Desktop app")
mysecondLabel = Label(root, text = "My second Desktop app")

myfirstLabel.pack()
mysecondLabel.pack()

root.mainloop()
