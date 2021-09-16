from tkinter import*

root = Tk()
root.configure(background = "Orangered")
root.geometry("500x500")

Title = Label(root, text = "Name List",font =30, bg = "orangered", width = "30")
Title.pack()

Input = Entry()
Input.pack()

names = []
def getNames():
    Inputs = Input.get()
    names.append(Inputs)
    errors = ""

    # if(names == ""):
    #     errors = "pls input a name"
    #     names.pop()

    if  names.count(names[-1]) == " ":
        errors = "pls Enter Name"
        names.pop

    if  names.count(names[-1]) > 1:
        errors = "exist"
        names.pop


    if(len(names[-1]) > 0 and (names[-1].count('z') or  names[-1].count('Z')) > 0 ):
        errors = "names must not contain both small and capital 'Z'"
        names.pop

    
    if (len(names) != 0 and len(names[-1]) < 5):
        errors = "names must be more than 5 characters"
        names.pop

    if (len(names) > 10): 
        errors= "Numbers of names must not exceedd!"
        names.pop

    if (errors == "" and len(names) != 0 and len(names) <=10):
        List =  Label(root, text =names[-1],bg = "orangered", font =30, fg = "#fff")
        List.pack()
    else:
        List =  Label(root, text =errors,bg = "green", font =30, fg = "#fff")
        List.pack()

btn = Button(root, text = "Add Name", width = 10, bg = "green", fg = "#fff",command=getNames)
btn.pack()




root.mainloop()