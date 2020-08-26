from tkinter import*
from PIL import ImageTk,Image 

root=Tk()
root.title('IMAGE')
root.iconbitmap('icon.ico')

img = Image.open("1.png")
img = img.resize((640,359), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(img)
mylabel = Label(image=my_img)
mylabel.grid(row=0,column=0)

button_quit = Button(root, text="EXIT", command=root.quit)
button_quit.grid(row=1,column=0)

root.mainloop()