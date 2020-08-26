from tkinter import*

# creating the most basic window on which we will display
root = Tk()

def myclick():
	mylabel = Label(root, text="Look I clicked a button")
	mylabel.pack()

mybutton = Button(root, text="Click me!", command=myclick, fg= "#F50F0F", bg="blue")
mybutton.pack()

# mainloop() is to keep the gui running 
root.mainloop()

