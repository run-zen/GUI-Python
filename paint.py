from tkinter import*


class main:
	def __init__(self,master):
		
		self.master=master
		self.oldy=None
		self.oldx=None
		self.drawWidgets()
		self.c.bind('<B1-Motion>', self.paint)
		self.c.bind('<ButtonRelease-1>', self.reset)

	def paint(self,e):
		if self.oldx and self.oldy:
			self.c.create_line(self.oldx,self.oldy,e.x,e.y,width=5,fill="black",capstyle=ROUND,smooth=True)

		self.oldx = e.x
		self.oldy= e.y

	def reset(self,e):
		self.oldx=None
		self.oldy=None

	def clear(self):
		self.c.delete(ALL)

	def drawWidgets(self):
		self.exit_button = Button(self.master, text='Clear All', command=self.clear).pack(side=BOTTOM)
		self.c = Canvas(self.master, width=500, height=400, bg ='white')
		self.c.pack(fill=NONE, expand=True)


if __name__== '__main__':
	root= Tk()
	main(root)
	root.iconbitmap("icon.ico")
	root.title("Paint")
	root.mainloop()

		

