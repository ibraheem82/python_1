# from tkinter import*

# root = None
# def buttonPushed():
#     global root
#     root.destroy()
#     print("Button pushed!")

# def main():
#     global root

# root = Tk()
# root.title("My first Desk App")
# root.configure(background = "hotpink",)
# root.geometry("500x500")
# a = Label(root, text = "Enter Your name")
# b = Label(root, text = "Enter your matNo.")
# c = Button(root, text = "Exit", command = buttonPushed)

# def createTextBox(parent):
#     tBox = Entry(parent)
#     tBox.pack()


# a.pack()
# b.pack()
# c.pack()

# root.mainloop()
# main()

# createTextBox(root)

# from tkinter import *
# # Hold onto a global reference for the root window
# root = None
# def buttonPushed():
#     global root
#     root.destroy() # Kill the root window!
# def main():
#     global root
# root = Tk() # Create the root (base) window where all widgets go
# w = Label(root, text="Hello, world!") # Create a label with words
# w.pack() # Put the label into the window
# myButton = Button(root, text="Exit",command=buttonPushed)
# myButton.pack()
# root.mainloop() # Start the event loop
# main()


# from tkinter import *
# # Hold onto a global reference for the root window
# root = None
# # Hold onto the Text Entry Box also
# entryBox = None
# def buttonPushed():
#     global entryBox
# txt = entryBox.get()
# print ("The text is:",txt)
# def createTextBox(parent):
#     global entryBox
# entryBox = Entry(parent)
# entryBox.pack()
# def main():
#     global root
# root = Tk() # Create the root (base) window where all widgets go
# myButton = Button(root, text="Show Text",command=buttonPushed)
# myButton.pack()
# createTextBox(root)
# root.mainloop() # Start the event loop
# main()
# Using a text entry box
# Call the get() operation on the entry box
# to get the text when button is pushed
# Create the global entry box


#pack_sample.py
from tkinter import *

root = None
count = 0 # Click counter


def buttonPushed():
    global root
    root.destroy()
    print("Button pushed!")


def addButton(root, sideToPack):
    global count
    name = "Button" + str(count) + " " + sideToPack
    button = Button(root, text=name)
    button.pack(side=sideToPack)
count += 1
def main():
    global root
root = Tk() # Create the root (base) window where all widgets go

root.title("My first Desk App")
root.configure(background = "hotpink",)
root.geometry("500x500")
a = Label(root, text = "Enter Your name")
b = Label(root, text = "Enter your matNo.")
c = Button(root, text = "Exit", command = buttonPushed)

for i in range(6):
    addButton(root, TOP)
root.mainloop() # Start the event loop
main()