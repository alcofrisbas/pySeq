from Tkinter import *
import ttk


class Slide(ttk.LabelFrame):
	def __init__(self, master, r, name):
		self.master = master
		ttk.LabelFrame.__init__(self, self.master, text = name, labelanchor=N)
		self.scaleVal = DoubleVar()
		self.scaleText = StringVar()
		self.r = StringVar()
		self.rVal = IntVar()
		self.rVal.set(r)
		self.r.set(str(self.rVal.get()))
		self.scaleText.set("0")
		
		self.slide = ttk.Scale(self, from_=self.rVal.get(), to=0,orient=VERTICAL,
			variable=self.scaleVal, command = self.set)
		self.slide.grid(row = 0, column = 0)

		self.e = ttk.Entry(self, textvariable = self.scaleText,width=4)
		self.e.grid(row = 1, column = 0)

		self.e.bind("<Return>", self.setScale)
		self.setScale("a")
		
		self.c = ttk.Entry(self, textvariable = self.r, width = 4)
		self.c.grid(row = 2)

		self.c.bind("<Return>", self.setRange)

	def set(self, a):
		self.scaleText.set(str(self.scaleVal.get()))
		#print a

	def setScale(self, e):
		self.scaleVal.set(float(self.e.get()))
	
	def setRange(self, event):
		self.slide["from_"] = self.r.get()


	def get(self):
		return self.scaleVal.get()


class GUI:
	def __init__(self, master):
		self.master = master

		self.mainFrame = ttk.LabelFrame(self.master, text = "Envelope", relief="groove")
		self.mainFrame.grid()

		self.a = Slide(self.mainFrame,1000, "A")
		self.a.grid(row = 0, column = 0)

		self.d = Slide(self.mainFrame,1000, "D")
		self.d.grid(row = 0, column = 1)

		self.s = Slide(self.mainFrame,1, "S")
		self.s.grid(row = 0, column = 2)

		self.r = Slide(self.mainFrame,1000, "R")
		self.r.grid(row = 0, column = 3)

if __name__ == '__main__':
	root = Tk()
	g = GUI(root)
	root.mainloop()