from tkinter import *
import datetime
root=Tk()
root.title("Age Calculator")
root.geometry("400x400")
#print(root)

def apple():
    birthdate = datetime.datetime(int(YearVariable.get()),int(MonthVariable.get()),int(DayVariable.get()))
    age = datetime.datetime.now() - birthdate
    convertdays = int(age.days)
    convertyears = round(convertdays/365, 2)
    Label(text = f"{NameVariable.get()} your age is {convertyears}").grid(row =6 , column = 1)

Lb1 = Label(root,text= "Your Name?").grid(row=1,column=1)
lb2 = Label(root,text= "Your Birth Year?").grid(row=2,column=1)
lb3 = Label(root,text= "Your Birth Month?").grid(row=3,column=1)
lb4 = Label(root,text= "Your Birth Day?").grid(row=4,column=1)

NameVariable=StringVar()
YearVariable=StringVar()
MonthVariable=StringVar()
DayVariable=StringVar()

EntryName = Entry(root, textvariable = NameVariable).grid(row= 1, column=2)
EntryYear = Entry(root, textvariable = YearVariable).grid(row=2,column=2)
EntryMonth = Entry(root, textvariable = MonthVariable).grid(row=3,column=2)
EntryDay = Entry(root, textvariable = DayVariable).grid(row=4,column=2)

button1 = Button(root, text = "Calculate Age", command=apple). grid(row=5,column=1)



root.mainloop()
