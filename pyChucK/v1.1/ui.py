from Tkinter import *
import ttk
from math import ceil

from tools import *

"""
TODO LATER::::

- BUGS:
	- changing the sample sequence erases the cue visually

"""

class TimeCanvas(Canvas):
	def __init__(self, master, arr, arrG, **kwargs):
		#print kwargs
		self.arr = arr[:]
		print "init"
		print len(arr)
		self.arrG = arrG[:]
		Canvas.__init__(self, master, **kwargs)
		self.bind("<Button-1>", self.toggle)
		self.bind("<Button-2>", self.setGain)
		self.WIDTH = kwargs["width"]
		self.HEIGHT = kwargs["height"]
		self.setupSubs()

	def toggle(self, event):
		lArr = len(self.arr)
		slot =  event.x/(self.WIDTH/lArr)
		print self.arr[slot], self.arrG[slot]

		if self.arr[slot] == 0:
			self.arr[slot] = 1
			self.create_rectangle(slot*self.WIDTH/lArr+1, self.HEIGHT*(1-self.arrG[slot]), slot*self.WIDTH/lArr+self.WIDTH/lArr, self.HEIGHT, fill = "dodgerblue", width=0)

		elif self.arr[slot] == 1:
			self.arr[slot] = 0
			self.create_rectangle(slot*self.WIDTH/lArr+1, self.HEIGHT*(1-self.arrG[slot]), slot*self.WIDTH/lArr+self.WIDTH/lArr, self.HEIGHT, fill = "white", width=0)
		#print self.arr
		self.create_text(slot*self.WIDTH/lArr+self.WIDTH/lArr/2, self.HEIGHT-3, text = str(slot), anchor = S, font="Symbol 8")

	def setGain(self, event):
		lArr = len(self.arr)
		g = 1-float(event.y)/self.HEIGHT
		slot =  event.x/(self.WIDTH/lArr)
		self.create_rectangle(slot*self.WIDTH/lArr+1, 0, slot*self.WIDTH/lArr+self.WIDTH/lArr, self.HEIGHT, fill = "white", width=0)
		self.create_rectangle(slot*self.WIDTH/lArr+1, event.y, slot*self.WIDTH/lArr+self.WIDTH/lArr, self.HEIGHT, fill = "dodgerblue", width=0)
		self.create_text(slot*self.WIDTH/lArr+self.WIDTH/lArr/2, self.HEIGHT-3, text = str(slot), anchor = S, font="Symbol 8")
		self.arrG[slot] = g
		self.arr[slot] = 1
	
	def setupSubs(self):
		self.delete("all")
		#self.arr = []
		lArr = len(self.arr)
		print "setup"
		print lArr
		for i in range(len(self.arr)):
			#print "slot",i
			#self.arr.append(0)
			self.create_line(i*self.WIDTH/lArr, 0, i*self.WIDTH/lArr, self.HEIGHT)
			if self.arr[i] == 1:
				self.create_rectangle(i*self.WIDTH/lArr+1, self.HEIGHT*(1-self.arrG[i]), i*self.WIDTH/lArr+self.WIDTH/lArr, self.HEIGHT, fill = "dodgerblue", width=0)
			self.create_text(i*self.WIDTH/lArr+self.WIDTH/lArr/2, self.HEIGHT-3, text = str(i), anchor = S, font="Symbol 8")
		#print self.arr


	def addSub(self):
		print "adding"
		self.arr.append(0)
		self.arrG.append(1.0)
		print self.arr
		#self.labelSubs.set(str(new))
		self.setupSubs()

	def subSub(self):
		print "subbing"
		self.arr.pop()
		self.arrG.pop()
		#self.labelSubs.set(str(new))
		self.setupSubs()

# Information for drawing the box in the main Canvas
class Box:
	def __init__(self, instrument, x,y):
		self.instrument = instrument
		self.oX = x
		self.oY = y
		self.sizeY = 40
		self.sizeX = 40*ceil(len(self.instrument.arr)/40.0)

class CueWindow(Toplevel):
	def __init__(self, master, instrument, can):
		self.i = instrument
		print self.i.instrument.arr
		self.can = can
		self.master = master
		Toplevel.__init__(self)

		self.mainFrame = ttk.Frame(self)
		self.mainFrame.grid()

		self.timeCan = TimeCanvas(self.mainFrame, self.i.instrument.arr, self.i.instrument.arrG, width = 400, height = 70)
		self.timeCan.grid()

		self.PMFrame = ttk.Frame(self.mainFrame)
		self.PMFrame.grid(row = 0, column = 1, sticky = N)

		#self.sLabel = ttk.Label(self.PMFrame, textvariable = self.labelSubs)
		#self.sLabel.grid(row = 0, column = 0)

		self.pButton = ttk.Button(self.PMFrame, text = "+", command = self.timeCan.addSub)
		self.pButton.grid(row  = 1, column = 0)
		self.mButton = ttk.Button(self.PMFrame, text = "-", command = self.timeCan.subSub)
		self.mButton.grid(row = 2, column = 0)

		self.buttonFrame = ttk.Frame(self.mainFrame)
		self.buttonFrame.grid(row = 1, column = 0, sticky = EW)

		self.tEntry = ttk.Entry(self.buttonFrame)
		self.tEntry.grid(row = 0, column = 0)
		self.tEntry.insert(0, "0")

		self.goButton = ttk.Button(self.buttonFrame, text = "Set Cue", command = self.setCue)
		self.goButton.grid(row = 0, column = 1)

	def setCue(self):
		self.i.instrument.addCue(self.tEntry.get(), self.timeCan.arr)
		print self.i.instrument.arr
		# draw Rect
		#print len(self.i.instrument.cues)
		self.can.create_rectangle(self.i.oX+self.i.sizeX+self.i.sizeY, self.i.oY+self.i.sizeY/4*(len(self.i.instrument.cues)-1), self.i.oX+self.i.sizeX+2*self.i.sizeY, self.i.oY+self.i.sizeY/4*(len(self.i.instrument.cues)-1)+self.i.sizeY/5, fill = "white",tags = (self.i.instrument.n, "cue", self.tEntry.get()))
		self.can.create_text(self.i.oX+self.i.sizeX+self.i.sizeY+2, self.i.oY+self.i.sizeY/4*(len(self.i.instrument.cues)-1), text = "c: "+self.tEntry.get(),font = "Symbol 8", anchor = NW,tags = (self.i.instrument.n, "cue",self.tEntry.get()))
		self.can.create_line(self.i.oX+self.i.sizeX, self.i.oY+self.i.sizeY/12*(len(self.i.instrument.cues)-1),self.i.oX+self.i.sizeX+self.i.sizeY, self.i.oY+self.i.sizeY/4*(len(self.i.instrument.cues)-1),tags = (self.i.instrument.n, "cue",self.tEntry.get()))
		self.destroy()

class OptionWindow(Toplevel):
	def __init__(self, master, instrument, can):
		self.i = instrument
		self.can = can
		self.master = master
		Toplevel.__init__(self)

		self.mainFrame = ttk.Frame(self)
		self.mainFrame.grid()
		self.boxVal = StringVar()
		self.lBox = ttk.Combobox(self.mainFrame, textvariable=self.boxVal, width = 10)
		self.lBox['values'] = ("cue","rate", "gain")
		self.lBox.current(0)
		self.lBox.grid()

		self.lEntry = ttk.Entry(self.mainFrame, width = 5)
		self.lEntry.grid(row = 0, column = 1)

		self.lSet = ttk.Button(self.mainFrame, text = "Apply", command = self.apply)
		self.lSet.grid(row = 0, column = 2)
	
	def apply(self):
		s = "{} => {}.{};\n".format(self.lEntry.get(), self.i.instrument.n, self.boxVal.get())
		#print s
		if self.boxVal.get() == "cue":

			CueWindow(self, self.i, self.can)
			
		else:
			self.i.instrument.addOpt(s)
			modY = 0
			text = "g"
			fill = "white"
			if self.boxVal.get() == "rate":
				modY = self.i.sizeY/2
				text = "r"
			self.can.create_rectangle(self.i.oX+self.i.sizeX+5, self.i.oY+modY, self.i.oX+self.i.sizeX+5+self.i.sizeY/2.5,self.i.oY+modY+ self.i.sizeY/2.5, fill = fill, tags = (self.i.instrument.n, "option"))
			self.can.create_line(self.i.oX+self.i.sizeX, self.i.oY+modY, self.i.oX+self.i.sizeX+5, self.i.oY+modY,tags = (self.i.instrument.n, "option"))
			self.can.create_text(self.i.oX+self.i.sizeX+5+1, self.i.oY+modY+1, text = text, font = "Symbol 7", anchor = NW, tags = (self.i.instrument.n, "option"))

		self.destroy()

class BeatWindow(Toplevel):
	def __init__(self, master, beat):
		self.beat = beat
		Toplevel.__init__(self)

		#self.master = master
		self.title("configure beat")

		self.mainFrame = ttk.Frame(self)
		self.mainFrame.grid()

		self.tEntry = ttk.Entry(self.mainFrame)
		self.tEntry.grid(row = 0, column = 0)
		self.tEntry.insert(0, self.beat.t)
		self.lEntry = ttk.Entry(self.mainFrame)
		self.lEntry.grid(row = 0, column = 1)
		self.lEntry.insert(0, self.beat.l)

		self.goButton = ttk.Button(self.mainFrame, text = "set", command = self.setBeat)
		self.goButton.grid(row = 0, column = 2)
	def setBeat(self):
		self.beat.t = int(self.tEntry.get())
		self.beat.l = int(self.lEntry.get())
		print self.beat.t
		self.destroy()
# A toplevel window for configuring an instrument in a beat
class InstWindow(Toplevel):
	def __init__(self, master, can, originX, originY, instrumentDict, lineX, lineY, instrument):
		self.can = can
		self.iDict = instrumentDict
		self.oX = originX
		self.oY = originY
		self.lineX = lineX
		self.lineY = lineY
		self.i = instrument

		self.labelSubs = StringVar()
		self.labelSubs.set(str(16))
		self.arr = []
		
		self.WIDTH = 400
		self.HEIGHT = 75

		Toplevel.__init__(self)
		self.mainFrame = ttk.Frame(self)
		self.mainFrame.grid()
		
		self.upperFrame = ttk.Frame(self.mainFrame)
		self.upperFrame.grid(row = 0, column = 0)
		##### FILLER ARRAYS
		self.timeCan = TimeCanvas(self.upperFrame, self.i.arr, self.i.arrG, width = self.WIDTH, height = self.HEIGHT)
		self.timeCan.grid(row = 0, column = 0)
		

		self.PMFrame = ttk.Frame(self.upperFrame)
		self.PMFrame.grid(row = 0, column = 1, sticky = N)

		self.sLabel = ttk.Label(self.PMFrame, textvariable = self.labelSubs)
		self.sLabel.grid(row = 0, column = 0)

		self.pButton = ttk.Button(self.PMFrame, text = "+", command = self.timeCan.addSub)
		self.pButton.grid(row  = 1, column = 0)
		self.mButton = ttk.Button(self.PMFrame, text = "-", command = self.timeCan.subSub)
		self.mButton.grid(row = 2, column = 0)

		self.lowerFrame = ttk.Frame(self.mainFrame)
		self.lowerFrame.grid(row = 1, column = 0, sticky = W)

		self.tName = ttk.Entry(self.lowerFrame, width = 10)
		self.tName.grid(row = 0, column = 0)
		self.tName.insert(0, self.i.n)

		self.tSource = ttk.Entry(self.lowerFrame)
		self.tSource.grid(row = 0, column = 1)
		source = "track_source.wav"
		if self.iDict.get(self.i.n):
			source = self.iDict[self.i.n].instrument.source

		self.tSource.insert(0, source)

		self.goButton = ttk.Button(self.lowerFrame, text = "Make", command = self.make)
		self.goButton.grid(row = 0, column = 2)

		#self.timeCan.setupSubs()

	def make(self):
		#i = Instrument(self.tName.get(), source=self.tSource.get())
		#################
		self.i.n = self.tName.get()
		self.i.source = self.tSource.get()
		self.i.setArray(self.timeCan.arr, self.timeCan.arrG)
		b = Box(self.i, self.oX, self.oY)
		self.iDict[self.i.n] = b
		#self.can.delete(self.tName.get())
		print b.oX, b.oY, b.oX+b.sizeX, b.oY+b.sizeY
		self.can.create_line(self.lineX, self.lineY, self.oX, self.oY, tags=(self.tName.get(), "instrument"))
		self.can.create_rectangle(b.oX, b.oY, b.oX+b.sizeX, b.oY+b.sizeY, fill = "white", tags=(self.tName.get(), "instrument"))
		self.can.create_text(b.oX+1, b.oY+1, text=b.instrument.n, anchor=NW, font ="Symbol 7", width=b.sizeX, tags=(self.tName.get(), "instrument"))
		#for j, k in enumerate(self.i.arr):
		#	if k == 1:
		#		self.can.create_line(b.oX+1+j*2, b.oY+b.sizeY-3,b.oX+1+j*2, b.oY+b.sizeY,tags=(self.tName.get(), "instrument"))
		self.destroy()



class GUI:
	def __init__(self, master):
		self.master = master
		self.master.title("pyChucK BeatMaster")

		self.mainFrame = ttk.Frame(self.master)
		self.mainFrame.grid()

		self.can = Canvas(self.mainFrame, bg = "gray80", width = 600, height = 600)
		self.can.grid(padx=5, pady = 5)

		#self.can.bind("<Button-1>", self.mouse1)
		self.can.bind("<Button-2>", self.mouse2)
		self.can.tag_bind("instrument", "<Button-1>", self.inst1)
		self.can.tag_bind("beat", "<Button-1>", self.beat1)
		self.can.tag_bind("instrument", "<Button-2>", self.inst2)
		self.can.tag_bind("cue", "<Button-1>", self.cue)
		self.can.tag_bind("option", "<Button-1>", self.option)

		self.buttonFrame = ttk.Frame(self.mainFrame)
		self.buttonFrame.grid(row = 1, column = 0, sticky = EW)

		self.nEntry = ttk.Entry(self.buttonFrame)
		self.nEntry.grid(row = 0, column = 0, sticky = W)

		self.goButton = ttk.Button(self.buttonFrame, text = "Write to ChucK", command = self.makeBeat)
		self.goButton.grid(row = 1, column = 0, sticky = EW)

		# ----------------------------------------

		self.instruments = {}
		self.beats = {}
		self.theBeat = Beat(256, 80)

		self.setupBeat()

	def beat1(self, event):
		BeatWindow(self, self.theBeat)

	def inst1(self, event):
		tags = list(self.can.gettags(event.widget.find_closest(event.x, event.y)))
		tags.remove("current")
		tags.remove("instrument")
		inst = self.instruments[tags[0]]
		InstWindow(self, self.can, inst.oX, inst.oY, self.instruments, 60, 60, inst.instrument)
	
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
		self.can.create_rectangle(self.oX, self.oY, self.oX+self.size, self.oY+self.size, fill = "white", tags = ("beat"))
		self.can.create_text(self.oX+1, self.oY+1, text="Main", anchor=NW, font ="Symbol 8", width=self.size-2, tags = ("beat"))

	def mouse2(self, event):
		item = self.can.find_closest(event.x, event.y)
		tags =  list(self.can.gettags(item))

		if "current" not in tags:
			i = Instrument("track_name", "track_source")
			print "via mouse2"
			print len(i.arr)
			InstWindow(self, self.can, event.x, event.y, self.instruments, 60, 60, i)

	def makeBeat(self):
		self.theBeat.clear()
		for i in self.instruments:
			self.theBeat.add(self.instruments[i].instrument)
			#print i
		self.theBeat.write(self.nEntry.get())
if __name__ == '__main__':
	root = Tk()
	g = GUI(root)
	root.mainloop()