from tkinter import*

root = Tk()
root.configure(background = "aquamarine")
root.title("Testing")

myinput = Entry(root, text = "Enter a word", width = 50, bg = "hotpink",)
myinput.grid(row = 0, column = 4, columnspan = 7)

def clickBtn():
    myLabel = Label(root, text = "My name is:"+ " "+ myinput.get())
    myLabel.grid(row = 3, column = 4)

myButton = Button(root, text="Click me!", bg="orangered",fg = "white", width = 20, command = clickBtn)
myButton.grid(row = 1, column = 4)

quiBtn = Button(root, text = "Quit", bg = "green", width = 20, command = root.destroy)
quiBtn.grid(row = 1, column = 6)
root.mainloop()