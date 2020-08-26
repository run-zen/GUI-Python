from tkinter import*

# creating the most basic window on which we will display
root = Tk()

e = Entry(root, width = 50, height= 20)
e.
e.insert(0, "Enter your name")

def myclick():
	hello = "Hi " + e.get()
	mylabel = Label(root, text=hello)
	mylabel.pack()

mybutton = Button(root, text="Enter your name", command=myclick)
mybutton.pack()

# mainloop() is to keep the gui running 
root.mainloop()

