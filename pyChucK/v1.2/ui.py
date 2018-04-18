from Tkinter import *
import ttk
from math import ceil

from tools import *
from windows import *

"""
TODO LATER::::

- Delete instruments.
- edit tick duration in beats
- 0123 for arrays: envelope commands...

- BUGS:
	- it's all fucking buggy
	- prevent people from same name tracks and beats 
		- hard because Editing is identical to creating...

	- extra line drawn from instrument to selected beat
	  on edit(not creation)
"""





class GUI:
	def __init__(self, master):
		self.keyPressed = False
		self.b1Pressed = False

		self.master = master
		self.master.title("pyChucK BeatMaster")

		self.selectedBeat = "MAIN"

		self.mainFrame = ttk.Frame(self.master)
		self.mainFrame.grid()

		self.can = Canvas(self.mainFrame, bg = "gray80", width = 600, height = 600)
		self.can.grid(padx=5, pady = 5)

		#self.can.bind("<Button-1>", self.createBeat)
		self.can.bind("<Button-1>", self.keyOrB1)

		self.can.bind("<Button-2>", self.mouse2)
		self.can.tag_bind("instrument", "<Button-1>", self.inst1)
		self.can.tag_bind("beat", "<Button-1>", self.beat1)
		self.can.tag_bind("beat", "<Button-2>", self.beat2)

		self.can.tag_bind("instrument", "<Button-2>", self.inst2)
		self.can.tag_bind("cue", "<Button-1>", self.cue)
		self.can.tag_bind("option", "<Button-1>", self.option)
		self.master.bind("<Key>", self.keyOrB1)


		self.can.bind("<ButtonRelease-1>", self.resetPressedState)
		self.master.bind("<KeyRelease>", self.resetPressedState)


		self.buttonFrame = ttk.Frame(self.mainFrame)
		self.buttonFrame.grid(row = 1, column = 0, sticky = EW)

		self.nEntry = ttk.Entry(self.buttonFrame)
		self.nEntry.grid(row = 0, column = 0, sticky = W)

		self.goButton = ttk.Button(self.buttonFrame, text = "Write to ChucK", command = self.makeBeat)
		self.goButton.grid(row = 1, column = 0, sticky = EW)

		# ----------------------------------------

		self.instruments = {}
		self.beats = {}
		self.theBeat = Beat("MAIN",256, 80, 4)
		self.beats[self.theBeat.n] = BeatBox(self.theBeat, 10, 10)

		self.setupBeat()


	def keyOrB1(self, event):
		if event.char.isalpha():
			#print "C Pressed"
			self.keyPressed = True
		if event.num == 1:
			#print "B1 Pressed"
			self.b1Pressed = True

		if self.b1Pressed and self.keyPressed:
			print "BOTH DOWN"
		elif self.b1Pressed:
			self.createBeat(event)
	

	def resetPressedState(self, event):
		self.keyPressed = False
		self.b1Pressed = False

	def aPressed(self,event):
		print 'mustafa'

	def createBeat(self, event):
		tags = list(self.can.gettags(event.widget.find_closest(event.x, event.y)))
		if "current" in tags:
			return
		b = Beat("NEW_BEAT",self.theBeat.l, self.theBeat.t, self.theBeat.s)
		BeatWindow(self, b, event.x, event.y, self.can, self.beats)


	def beat1(self, event):
		tags = list(self.can.gettags(event.widget.find_closest(event.x, event.y)))
		if "current" in tags:
			tags.remove("current")
			tags.remove("beat")
			b = self.beats[tags[0]]
			BeatWindow(self, b.beat,b.oX, b.oY, self.can, self.beats )

	def beat2(self, event):
		tags = list(self.can.gettags(event.widget.find_closest(event.x, event.y)))
		if "current" in tags:
			tags.remove("current")
			tags.remove("beat")
			self.selectedBeat = tags[0]
			print self.selectedBeat

	def inst1(self, event):
		tags = list(self.can.gettags(event.widget.find_closest(event.x, event.y)))
		tags.remove("current")
		tags.remove("instrument")
		inst = self.instruments[tags[0]]
		InstWindow(self, self.can, inst.oX, inst.oY, self.instruments, self.beats, 60, 60, inst.instrument)
	
	def inst2(self, event):
		print "via Inst2"
		tags = list(self.can.gettags(event.widget.find_closest(event.x, event.y)))
		tags.remove("current")
		tags.remove("instrument")
		inst = self.instruments[tags[0]]
		OptionWindow(self, inst, self.can)

	def cue(self, event):
		#print "cue"
		tags = list(self.can.gettags(event.widget.find_closest(event.x, event.y)))
		#print tags
		items = list(self.can.find_withtag("&&".join(tags)))
		#print items
		tags.remove("current")
		tags.remove("cue")
		tags.sort()
		inst = self.instruments[tags[1]]
		cueT = tags[0]
		if "//" in inst.instrument.cues[cueT]:
			inst.instrument.cues[cueT] = inst.instrument.cues[cueT].replace("//","")
			theFill = "white"

		else:
			inst.instrument.cues[cueT] = "//"+inst.instrument.cues[cueT]
			theFill = "gray80"
		for i in items:
			self.can.itemconfig(i, fill=theFill)

	def option(self, event):
		print "option"

	def setupBeat(self):
		self.oX = 10
		self.oY = 10
		self.size = 50
		self.can.create_rectangle(self.oX, self.oY, self.oX+self.size, self.oY+self.size, fill = "white", tags = ("beat", self.theBeat.n))
		self.can.create_text(self.oX+1, self.oY+1, text="Main", anchor=NW, font ="Symbol 8", width=self.size-2, tags = ("beat", self.theBeat.n))

	def mouse2(self, event):
		item = self.can.find_closest(event.x, event.y)
		tags =  list(self.can.gettags(item))

		if "current" not in tags:
			i = Instrument("track_name", "track_source", self.beats[self.selectedBeat].beat)
			print "via mouse2"
			print len(i.arr)
			pX = self.beats[self.selectedBeat].oX+self.beats[self.selectedBeat].sizeX
			pY = self.beats[self.selectedBeat].oY+self.beats[self.selectedBeat].sizeY
			InstWindow(self, self.can, event.x, event.y, self.instruments, self.beats, pX, pY, i)

	def makeBeat(self):
		for beatB in self.beats:
			self.beats[beatB].beat.clear()
		for i in self.instruments:
			self.beats[self.instruments[i].instrument.p.n].beat.add(self.instruments[i].instrument)
			#print i
		s = ""
		s += "Math.pow(2, 1.0/12) => float a;\n"
		s += "440=> float f0;\n"
		s += "fun float note(int n) {\n"
		s += "\treturn f0 * Math.pow(a, n)\n;"
		s += "}\n"
		for b in self.beats:
			s += self.beats[b].beat.prelude()

		for b in self.beats:
			s += self.beats[b].beat.__str__()
		s += self.theBeat.n+"();"
		with open(self.nEntry.get(),"w") as w:
			w.write(s)
		#self.theBeat.write(self.nEntry.get())
if __name__ == '__main__':
	root = Tk()
	g = GUI(root)
	root.mainloop()