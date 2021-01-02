from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=2)
e.pack()
e.get()

def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

myButton = Button(root, text="Enter your name", command=myClick)
myButton.pack()

root.mainloop()