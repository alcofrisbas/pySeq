from Tkinter import *
import ttk

from slider import Slide

class Envelope(ttk.LabelFrame):
	def __init__(self, master):
		self.master = master

		ttk.LabelFrame.__init__(self, self.master, text = "Envelope")

		self.a = Slide(self,1000, "A")
		self.a.grid(row = 0, column = 0)

		self.d = Slide(self,1000, "D")
		self.d.grid(row = 0, column = 1)

		self.s = Slide(self,1, "S")
		self.s.grid(row = 0, column = 2)

		self.r = Slide(self,1000, "R")
		self.r.grid(row = 0, column = 3)

	def get(self):
		return [self.a.get(), self.d.get(), self.s.get(), self.r.get()]

class Filter(ttk.LabelFrame):
	def __init__(self, master):
		self.master = master

		ttk.LabelFrame.__init__(self, self.master, text="Filter")

		self.f = Slide(self, 1000, "Freq")
		self.f.grid(row = 0, column = 0)

		self.q = Slide(self, 1, "Res")
		self.q.grid(row = 0, column = 1)

		self.e = ttk.Entry(self, width = 5)
		self.e.grid(row = 1, column = 0, columnspan = 2)


# class  Trigger(ttk.LabelFrame):
# 	def __init__(self, master, t):
# 		self.master = master

# 		ttk.LabelFrame.__init__(self, self.master, text=t)

# 		self.g = 
		

class TriggerSeq(ttk.LabelFrame):
	def __init__(self, master):
		self.master = master

		ttk.LabelFrame.__init__(self, self.master, text = "TriggerSeq")
		self.triggers = []
		self.vals = []
		for i in range(16):
			self.vals.append(IntVar())
			self.triggers.append(ttk.Checkbutton(self, var=self.vals[i]))

		for i in range(len(self.triggers)):
			self.triggers[i].grid(row = i/4, column = i%4)

		self.b = ttk.Button(self, text = "getTest", command = self.get)
		self.b.grid(row = 4, column = 0, columnspan = 4)
		
		

	def get(self):
		l = [y.get() for y in self.vals]
		print l
		return l


class GUI:
	def __init__(self, master):
		self.master = master

		self.e = Envelope(self.master)
		self.e.grid()	

		self.f = Filter(self.master)
		self.f.grid(row = 0, column = 1)

		self.t = TriggerSeq(self.master)
		self.t.grid(row = 0, column = 2)


if __name__ == '__main__':
	root = Tk()
	g = GUI(root)
	root.mainloop()