from Tkinter import *

class gui:
	def __init__(self, master):
		self.master = master
		self.frame=Frame(root,width=300,height=300)
		self.frame.grid(row=0,column=0)
		self.canvas=Canvas(self.frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))
		self.hbar=Scrollbar(self.frame,orient=HORIZONTAL)
		self.hbar.pack(side=BOTTOM,fill=X)
		self.hbar.config(command=self.canvas.xview)
		self.vbar=Scrollbar(self.frame,orient=VERTICAL)
		self.vbar.pack(side=RIGHT,fill=Y)
		self.vbar.config(command=self.canvas.yview)
		self.canvas.config(width=300,height=300)
		self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
		self.canvas.pack(side=LEFT,expand=True,fill=BOTH)

		self.canvas.create_rectangle(10,10,30,30)

		self.canvas.bind("<Button-1>", self.b1)

	def b1(self, event):
		print "clicked: {}, {}".format(str(event.x), str(event.y))
		print self.hbar.get()
root=Tk()

gui = gui(root)


root.mainloop()