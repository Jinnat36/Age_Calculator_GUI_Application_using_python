# create text entry box filling the information.# Import tkinter module here
from tkinter import*

# Import datetime module here
from datetime import date

# Create a GUI window
root=Tk()
root.title("Age Calculator")

# Set background colour of GUI window
root.configure(background="lightgreen")

# Set  the geometry
root.geometry("450x350")

#  Set font for heading 
font_for_names=("Times",20,"bold")

# Function to calculate age  
def CalculateAge():
    today=date.today()
    brithday=date(int(year1.get()),int(month1.get()),int(day1.get()))
    age=today.year-brithday.year -((today.month,today.day)<(brithday.month,brithday.day))
    Label(text=f"Result : {name.get().capitalize()} is {age} years old",font=5).place(x=50,y=300)    
    
# It is heading part
heading=Label(root,text="AGE CALCULATOR",fg="red",font=font_for_names,background="lightgreen")
heading.place(x=100,y=25)

# create  given name,year,age,day : label 

Label(root,text="ENTER YOUR NAME : ",background="lightgreen").place(x=30,y=90)
Label(root,text="ENTER YOUR BRITH YEAR : ",background="lightgreen").place(x=30,y=130)
Label(root,text="ENTER YOUR BRITH MONTH : ",background="lightgreen").place(x=30,y=170)
Label(root,text="ENTER YOUR BRITH DAY : ",background="lightgreen").place(x=30,y=210)

# Set datatypes
n=StringVar()
y=StringVar()
m=StringVar()
d=StringVar()

# place() method is used for explicilty set the position and size of 
# a window,either in absolute terms, or relative to another window.

# create text entry box filling the information.
name=Entry(root,textvariable=n,width=30,bd=3)
name.place(x=200,y=90)
year1=Entry(root,textvariable=y,width=30,bd=3)
year1.place(x=200,y=130)
month1=Entry(root,textvariable=m,width=30,bd=3)
month1.place(x=200,y=170)
day1=Entry(root,textvariable=d,width=30,bd=3)
day1.place(x=200,y=210)

# Create  result button and attached to CalculateAge  function
b=Button(root,text="Calculate Age",command=CalculateAge,background="red",bd=3)
b.place(x=175,y=250)

# Start the GUI
root.mainloop()