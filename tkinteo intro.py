from tkinter import *

root = Tk()
#text for first entry
l1 = Label(root,text="Please enter first number")
l1.pack()
#getting first entry
e1 = Entry(root, bd=5)
e1.pack()
#text for second entry
l2 = Label(root,text="Please enter second number")
l2.pack()
#getting second entry
e2 = Entry(root, bd=5)
e2.pack()

#func to add entrys
def Add() :
 x1 = e1.get()
 x2 = e2.get()

 A1 = Label(root,text= float(x1)+float(x2))
 A1.pack()
#func to exit
def Exit() :
    exit()
#func to clear boxs
def Clear() :
    e1.delete(0,END)
    e2.delete(0,END)
   # Add.A1.pack_forget()

#btn on press calls add func
Addbtn = Button(text="Add", command=Add)
Addbtn.pack()
#btn on press clears entrys
Clearbtn = Button(text="Clear", command=Clear)
Clearbtn.pack()
#btn on press closes
Closebtn = Button(text="close", command=Exit)
Closebtn.pack()
#size of window
root.geometry("300x300") #size of window
#displays here
root.mainloop()