from tkinter import*

# creating the most basic window on which we will display
root = Tk()

#creating a label widget
mylabel = Label(root, text="Hello World!")

# putting it up on the root window
mylabel.pack()

# mainloop() is to keep the gui running
root.mainloop()

