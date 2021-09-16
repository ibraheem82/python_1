# Python program to create a 
# GUI mark sheet using tkinter 
  
  
# Import tkinter as tk 
import tkinter as tk 
  
  
# creating a new tkinter window 
master = tk.Tk()  
  
# assigning a title 
master.title("CGPA CALCULATOR") 
  
# specifying geomtery for window size  
master.geometry("600x300")  
  
  
# declaring objects for entering data 
e1 = tk.Entry(master) 
e2 = tk.Entry(master) 
# e3 = tk.Entry(master)
# scores entry 
e4 = tk.Entry(master) 
e5 = tk.Entry(master) 
e6 = tk.Entry(master) 
e7 = tk.Entry(master)
e8 = tk.Entry(master) 
e9 = tk.Entry(master) 
e10 = tk.Entry(master) 
e11 = tk.Entry(master)

# Subjects Units
u1 = tk.Entry(master) 
u2 = tk.Entry(master) 
u3 = tk.Entry(master) 
u4 = tk.Entry(master)
u5 = tk.Entry(master) 
u6 = tk.Entry(master) 
u7 = tk.Entry(master) 
u8 = tk.Entry(master)
# e12 = tk.Entry(master) 
# e13 = tk.Entry(master) 

  
  
  
# function to display the total subject  
# credits total credits and SGPA according 
# to grades entered 
def display(): 
      
    # Varibale to store total marks 
    # tot=0
      
    # 10*number of subject credits  
    # give total credits for grade A
    if e4.get() >= "0" and e4.get() <= "39":
        return tk.Label(master, text ="F").grid(row=3, column=4) 
    if e4.get() >= "40" and e4.get() <= "44":
        return tk.Label(master, text ="E").grid(row=3, column=4)
    if e4.get() >= "45" and e4.get() <= "49":
        return tk.Label(master, text ="D").grid(row=3, column=4)
    if e4.get() >= "50" and e4.get() <= "54":
        return tk.Label(master, text ="CD").grid(row=3, column=4) 
    if e4.get() >= "55" and e4.get() <= "59":
        return tk.Label(master, text ="C").grid(row=3, column=4)  
    if e4.get() >= "60" and e4.get() <= "64":
        return tk.Label(master, text ="BC").grid(row=3, column=4)  
    if e4.get() >= "65" and e4.get() <= "69":
        return tk.Label(master, text ="B").grid(row=3, column=4)
    if e4.get() >= "70" and e4.get() <= "74":
        return tk.Label(master, text ="AB").grid(row=3, column=4)
    if e4.get() >= "75" and e4.get() <= "99":
        return tk.Label(master, text ="A").grid(row=3, column=4)

    

    if e5.get() >= "0" and e5.get() <= "39":
        return tk.Label(master, text ="F").grid(row=4, column=4)
    if e5.get() >= "40" and e5.get() <= "44":
        return tk.Label(master, text ="E").grid(row=4, column=4)
    if e5.get() >= "45" and e5.get() <= "49":
        return tk.Label(master, text ="D").grid(row=4, column=4)
    if e5.get() >= "50" and e5.get() <= "54":
        return tk.Label(master, text ="CD").grid(row=4, column=4) 
    if e5.get() >= "55" and e5.get() <= "59":
        return tk.Label(master, text ="C").grid(row=4, column=4)  
    if e5.get() >= "60" and e5.get() <= "64":
        return tk.Label(master, text ="BC").grid(row=4, column=4)  
    if e5.get() >= "65" and e5.get() <= "69":
        return tk.Label(master, text ="B").grid(row=4, column=4)
    if e5.get() >= "70" and e5.get() <= "74":
        return tk.Label(master, text ="AB").grid(row=4, column=4)
    if e5.get() >= "75" and e5.get() <= "99":
        return tk.Label(master, text ="A").grid(row=4, column=4)



    if e6.get() >= "0" and e6.get() <= "39":
        return tk.Label(master, text ="F").grid(row=5, column=4)
    if e6.get() >= "40" and e6.get() <= "44":
        return tk.Label(master, text ="E").grid(row=5, column=4)
    if e6.get() >= "45" and e6.get() <= "49":
        return tk.Label(master, text ="D").grid(row=5, column=4)
    if e6.get() >= "50" and e6.get() <= "54":
        return tk.Label(master, text ="CD").grid(row=5, column=4) 
    if e6.get() >= "55" and e6.get() <= "59":
        return tk.Label(master, text ="C").grid(row=5, column=4)  
    if e6.get() >= "60" and e6.get() <= "64":
        return tk.Label(master, text ="BC").grid(row=5, column=4)  
    if e6.get() >= "65" and e6.get() <= "69":
        return tk.Label(master, text ="B").grid(row=5, column=4)
    if e6.get() >= "70" and e6.get() <= "74":
        return tk.Label(master, text ="AB").grid(row=5, column=4)
    if e6.get() >= "75" and e6.get() <= "99":
        return tk.Label(master, text ="A").grid(row=5, column=4)




    # e e4.get() <= "39" or e4.get() >= "0":
    #     tk.Label(master, text ="F").grid(row=3, column=4)       
          
        
        
        
        # grid method is used for placing  
        # the widgets at respective positions  
        # in table like structure . 
        # tk.Label(master, text ="A").grid(row=3, column=4)


        # tot += 40
          
    # 9*number of subject credits give  
    # total credits for grade B 
    # if e4.get() == "B":  
    #     tk.Label(master, text ="36").grid(row=3, column=4) 
        # tot += 36
          
    # # 8*number of subject credits give 
    # # total credits for grade C 
    # if e4.get() == "C":  
    #     tk.Label(master, text ="32").grid(row=3, column=4) 
    #     tot += 32
          
    # # 7*number of subject credits  
    # # give total credits for grade D     
    # if e4.get() == "D":  
    #     tk.Label(master, text ="28").grid(row=3, column=4) 
    #     tot += 28
          
    # # 6*number of subject credits give  
    # # total credits for grade P     
    # if e4.get() == "P":  
    #     tk.Label(master, text ="24").grid(row=3, column=4) 
    #     tot += 24
          
    # # 0*number of subject credits give  
    # # total credits for grade F     
    # if e4.get() == "F":  
    #     tk.Label(master, text ="0").grid(row=3, column=4) 
    #     tot += 0
   
   
    # # Similarly doing with other objects 
    # if e5.get() == "A": 
    #     tk.Label(master, text ="40").grid(row=4, column=4) 
    #     tot += 40
    # if e5.get() == "B": 
    #     tk.Label(master, text ="36").grid(row=4, column=4) 
    #     tot += 36
    # if e5.get() == "C": 
    #     tk.Label(master, text ="32").grid(row=4, column=4) 
    #     tot += 32
    # if e5.get() == "D": 
    #     tk.Label(master, text ="28").grid(row=4, column=4) 
    #     tot += 28
    # if e5.get() == "P": 
    #     tk.Label(master, text ="28").grid(row=4, column=4) 
    #     tot += 24
    # if e5.get() == "F": 
    #     tk.Label(master, text ="0").grid(row=4, column=4) 
    #     tot += 0
       
       
   
    # if e6.get() == "A": 
    #     tk.Label(master, text ="30").grid(row=5, column=4) 
    #     tot += 30
    # if e6.get() == "B": 
    #     tk.Label(master, text ="27").grid(row=5, column=4) 
    #     tot += 27
    # if e6.get() == "C": 
    #     tk.Label(master, text ="24").grid(row=5, column=4) 
    #     tot += 24
    # if e6.get() == "D": 
    #     tk.Label(master, text ="21").grid(row=5, column=4) 
    #     tot += 21
    # if e6.get() == "P": 
    #     tk.Label(master, text ="28").grid(row=5, column=4) 
    #     tot += 24
    # if e6.get() == "F": 
    #     tk.Label(master, text ="0").grid(row=5, column=4) 
    #     tot += 0
   
   
   
   
    # if e7.get() == "A": 
    #     tk.Label(master, text ="40").grid(row=6, column=4) 
    #     tot += 40
    # if e7.get() == "B": 
    #     tk.Label(master, text ="36").grid(row=6, column=4) 
    #     tot += 36
    # if e7.get() == "C": 
    #     tk.Label(master, text ="32").grid(row=6, column=4) 
    #     tot += 32
    # if e7.get() == "D": 
    #     tk.Label(master, text ="28").grid(row=6, column=4) 
    #     tot += 28
    # if e7.get() == "P": 
    #     tk.Label(master, text ="28").grid(row=6, column=4) 
    #     tot += 24
    # if e7.get() == "F": 
    #     tk.Label(master, text ="0").grid(row=6, column=4) 
    #     tot += 0
   
   
    # # to display total credits 
    # tk.Label(master, text=str(tot)).grid(row=7, column=4)  
      
    # # to display SGPA 
    # tk.Label(master, text=str(tot/15)).grid(row=8, column=4)  
  
      
# end of display function 
  
# label to enter name 
tk.Label(master, text="Name").grid(row=0, column=0) 
  
# label for registration number 
tk.Label(master, text="Matric.No").grid(row=0, column=3) 
  
# label for roll Number 
# tk.Label(master, text="Roll.No").grid(row=1, column=0)  
  
# labels for serial numbers 
tk.Label(master, text="Srl.No").grid(row=2, column=0)  
tk.Label(master, text="1").grid(row=3, column=0) 
tk.Label(master, text="2").grid(row=4, column=0) 
tk.Label(master, text="3").grid(row=5, column=0) 
tk.Label(master, text="4").grid(row=6, column=0)

tk.Label(master, text="5").grid(row=7, column=0) 
tk.Label(master, text="6").grid(row=8, column=0) 
tk.Label(master, text="7").grid(row=9, column=0) 
tk.Label(master, text="8").grid(row=10, column=0) 
  
  
# labels for subject codes 
tk.Label(master, text="Subject").grid(row=2, column=1)  
tk.Label(master, text="CSC 201").grid(row=3, column=1) 
tk.Label(master, text="CSC 202").grid(row=4, column=1) 
tk.Label(master, text="MAT 201").grid(row=5, column=1) 
tk.Label(master, text="ECS 201").grid(row=6, column=1)

tk.Label(master, text="CSC 201").grid(row=7, column=1) 
tk.Label(master, text="CSC 202").grid(row=8, column=1) 
tk.Label(master, text="MAT 201").grid(row=9, column=1) 
tk.Label(master, text="GNS 201").grid(row=10, column=1)  
   
      
# label for grades 
tk.Label(master, text="Enter Scores").grid(row=2, column=2)  
e4.grid(row=3, column=2) 
e5.grid(row=4, column=2) 
e6.grid(row=5, column=2) 
e7.grid(row=6, column=2)

e8.grid(row=7, column=2) 
e9.grid(row=8, column=2) 
e10.grid(row=9, column=2) 
e11.grid(row=10, column=2)
 
   
  
# labels for subject credits 
tk.Label(master, text="Sub units").grid(row=2, column=3)
u1.grid(row=3, column=3) 
u2.grid(row=4, column=3) 
u3.grid(row=5, column=3) 
u4.grid(row=6, column=3)

u5.grid(row=7, column=3) 
u6.grid(row=8, column=3) 
u7.grid(row=9, column=3) 
u8.grid(row=10, column=3)



# tk.Label(master, text="4").grid(row=3, column=3) 
# tk.Label(master, text="4").grid(row=4, column=3) 
# tk.Label(master, text="3").grid(row=5, column=3) 
# tk.Label(master, text="4").grid(row=6, column=3) 
   
tk.Label(master, text="Remarks").grid(row=11, column=3)  
   
# taking entries of name, reg, roll number respectively 
e1=tk.Entry(master)  
e2=tk.Entry(master) 
# e3=tk.Entry(master) 
   
# organizing them in th e grid 
e1.grid(row=0, column=1) 
e2.grid(row=0, column=4) 
# e3.grid(row=1, column=1) 
   
# button to display all the calculated credit scores and sgpa 
button1=tk.Button(master, text="submit", bg="green", command=display) 
button1.grid(row=11, column=1) 
   
   
   
tk.Label(master, text="Grade Point").grid(row=11, column=2) 
# tk.Label(master, text="SGPA").grid(row=12, column=3) 
   
  
      
master.mainloop() 