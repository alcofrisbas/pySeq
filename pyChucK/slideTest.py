from Tkinter import *
import ttk

class ENV(ttk.LabelFrame):
	def __init__(self, master, envelope):
		self.env = envelope
		self.master = master
		ttk.LabelFrame.__init__(self, master, text = "Envelope")
		self.A = ttk.Label(self, text = "A")
		self.A.grid(row = 0, column = 0)

		self.D = ttk.Label(self, text = "D")
		self.D.grid(row = 1, column = 0)

		self.S = ttk.Label(self, text = "S")
		self.S.grid(row = 2, column = 0)

		self.R = ttk.Label(self, text = "R")
		self.R.grid(row = 3, column = 0)

		self.AE = ttk.Entry(self, width = 4)
		self.AE.grid(row = 0, column = 1)
		self.AE.insert(0, self.env[0])

		self.DE = ttk.Entry(self, width = 4)
		self.DE.grid(row = 1, column = 1)
		self.DE.insert(0, self.env[2])

		self.SE = ttk.Entry(self, width = 4)
		self.SE.grid(row = 2, column = 1)
		self.SE.insert(0, self.env[4])

		self.RE = ttk.Entry(self, width = 4)
		self.RE.grid(row = 3, column = 1)
		self.RE.insert(0, self.env[5])

		self.AVal = StringVar()
		self.ABox = ttk.Combobox(self, textvariable=self.AVal, width = 10)
		self.ABox['values'] = ("ms","second")
		self.AVal.set(self.env[1])
		#self.ABox.current(0)
		self.ABox.grid(row = 0, column = 2)

		self.DVal = StringVar()
		self.DBox = ttk.Combobox(self, textvariable=self.DVal, width = 10)
		self.DBox['values'] = ("ms","second")
		self.DVal.set(self.env[3])
		self.DBox.grid(row = 1, column = 2)

		self.RVal = StringVar()
		self.RBox = ttk.Combobox(self, textvariable=self.RVal, width = 10)
		self.RBox['values'] = ("ms","second")
		#self.RBox.current(0)
		self.RVal.set(self.env[6])
		self.RBox.grid(row = 3, column = 2)

	def get(self):
		return [self.AE.get(), self.AVal.get(), self.DE.get(), self.DVal.get(), self.SE.get(), self.RE.get(), self.RVal.get()]
if __name__ == '__main__':
	root = Tk()
	e = ENV(root)
	e.grid()
	#print e.get()
	root.mainloop()
