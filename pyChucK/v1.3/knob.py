from Tkinter import *
import ttk


class Knob(Canvas):
	def __init__(self, master):
		self.master = master
		Canvas.__init__(self,self.master)

		#self.l = ttk.Label(self, text = "Placeholder")
		#self.l.grid()
		self.bind("<MouseWheel>", self.test)
		self.pos = 0

	def test(self,event):
		if event.keycode > 0:
			self.pos += 1
		else:
			self.pos -= 1
		if self.pos < 0:
			self.pos = 0
		if self.pos > 99:
			self.pos = 99
		#print self.pos
		self.delete("all")
		f = "knob/simple/s{}.gif".format(self.pos)
		#print f
		self.gif1 = PhotoImage(file=f)
		self.x = self.create_image(0, 0, image=self.gif1, anchor=NW)
		#self.create_text(100, 100, text = "test", fill = "white")

class TESTER:
	def __init__(self, master):
		self.master = master
		self.mainFrame = ttk.Frame(self.master)
		self.mainFrame.grid()

		self.knob = Knob(self.mainFrame)
		self.knob.grid()


if __name__ == '__main__':
	root = Tk()
	t = TESTER(root)
	root.mainloop()