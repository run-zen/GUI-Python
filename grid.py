from tkinter import*

# creating the most basic window on which we will display
root = Tk()

#creating a label widget
mylabel1 = Label(root, text="Hello World!")
mylabel2 = Label(root, text="My name is Ranjan")
# putting it up on the root window
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=1)

# mainloop() is to keep the gui running 
root.mainloop()

