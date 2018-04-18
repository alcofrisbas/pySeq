from Tkinter import *
import ttk

from slideTest import ENV

"""

TODO:::::

- arrow keys to select next slot...
- restructure canvas for 1 2 3 0 DONE

BUGS:

- when editing an instrument, a new line
  appears to the current selected beat, regardless
  of whether or not it is the parent BADDDDD

"""

class TimeCanvas(Canvas):
	def __init__(self, master, arr, arrG, arrP, **kwargs):
		#print kwargs
		self.arr = arr[:]
		#print "init"
		#print len(arr)
		self.arrG = arrG[:]
		self.arrP = arrP[:]

		Canvas.__init__(self, master, **kwargs)
		self.focus_set()
		self.bind("<Button-1>", self.keyOrB1)
		#self.bind("<MouseWheel>", self.setPitch)
		#self.bind("<Button-2>", self.setGain)
		self.bind("<KeyPress>", self.keyOrB1)

		self.bind("<ButtonRelease-1>", self.resetPressedState)
		self.bind("<KeyRelease>", self.resetPressedState)

		self.WIDTH = kwargs["width"]
		self.HEIGHT = kwargs["height"]
		self.pitch = 0
		self.curSlot = 0

		self.keyPressed = False
		self.b1Pressed = False
		self.pitch = 0

		self.setupSubs()

	#def test(self, event):
	#	print "Right"

	def keyOrB1(self, event):
		if event.char.isalpha():
			#print "C Pressed"
			self.keyPressed = True
			self.curKey = event.char
		if event.num == 1:
			#print "B1 Pressed"
			self.b1Pressed = True

		if self.b1Pressed and self.keyPressed:
			print "BOTH DOWN"
			if self.curKey == "g":
				self.setGain(event)
			if self.curKey == "p":
				self.setPitch(event)
			elif self.curKey in "asdf":
				self.toggle(event)
		#elif self.b1Pressed:
		#	self.createBeat(event)

	def resetPressedState(self, event):
		self.keyPressed = False
		self.curKey = "!"
		self.b1Pressed = False
	
	def setPitch(self,event):
		lArr = len(self.arr)
		slot =  event.x/(self.WIDTH/lArr)
		self.curSlot = slot
		self.delete("{}pitchLabel".format(str(slot)))
		#shift = event.keycode
		self.pitch = (self.HEIGHT/2-event.y)/ 3
		print self.pitch
		self.create_text(slot*self.WIDTH/lArr+self.WIDTH/lArr/2, 5, text = str(self.pitch), anchor = N, font="Symbol 8", tags=("{}pitchLabel".format(str(slot))))
		self.create_rectangle(slot*self.WIDTH/lArr+self.WIDTH/lArr/2, event.y+3, slot*self.WIDTH/lArr+self.WIDTH/lArr, event.y-3, tags=("{}pitchLabel".format(str(slot))), fill = "dodgerblue3")
		self.arrP[slot] = self.pitch
	
	def toggle(self, event):
		lArr = len(self.arr)
		slot =  event.x/(self.WIDTH/lArr)
		self.delete("{}toggle".format(str(slot)))

		if self.curKey == "a":
			self.create_rectangle(slot*self.WIDTH/lArr+self.WIDTH/lArr/2, 0, slot*self.WIDTH/lArr+self.WIDTH/lArr, self.HEIGHT/10, tags=("{}toggle".format(str(slot))), fill = "green", width=0)
			self.arr[slot] = 1
		elif self.curKey == "s":
			self.create_rectangle(slot*self.WIDTH/lArr, 0, slot*self.WIDTH/lArr+self.WIDTH/lArr/2, self.HEIGHT/10, tags=("{}toggle".format(str(slot))), fill = "red", width=0)
			self.arr[slot] = 2
		if self.curKey == "d":
			self.create_rectangle(slot*self.WIDTH/lArr, 0, slot*self.WIDTH/lArr+self.WIDTH/lArr/2, self.HEIGHT/10, tags=("{}toggle".format(str(slot))), fill = "red", width=0)
			self.create_rectangle(slot*self.WIDTH/lArr+self.WIDTH/lArr/2, 0, slot*self.WIDTH/lArr+self.WIDTH/lArr, self.HEIGHT/10, tags=("{}toggle".format(str(slot))), fill = "green", width=0)
			self.arr[slot] = 3
		if self.curKey == "f":
			self.arr[slot] = 0

		#print self.arr[slot], self.arrG[slot]
		#print event.char

		# if self.arr[slot] == 0:
		# 	self.arr[slot] = 1
		# 	self.create_rectangle(slot*self.WIDTH/lArr+1, self.HEIGHT*(1-self.arrG[slot]), slot*self.WIDTH/lArr+self.WIDTH/lArr, self.HEIGHT, fill = "dodgerblue", width=0)

		# elif self.arr[slot] == 1:
		# 	self.arr[slot] = 0
		# 	self.create_rectangle(slot*self.WIDTH/lArr+1, self.HEIGHT*(1-self.arrG[slot]), slot*self.WIDTH/lArr+self.WIDTH/lArr, self.HEIGHT, fill = "white", width=0)
		# #print self.arr
		self.create_text(slot*self.WIDTH/lArr+self.WIDTH/lArr/2, self.HEIGHT-3, text = str(slot), anchor = S, font="Symbol 8")

	def setGain(self, event):
		lArr = len(self.arr)
		g = 1-float(event.y)/self.HEIGHT
		slot =  event.x/(self.WIDTH/lArr)
		self.create_rectangle(slot*self.WIDTH/lArr+1, 0, slot*self.WIDTH/lArr+self.WIDTH/lArr/2, self.HEIGHT, fill = "white", width=0)
		self.create_rectangle(slot*self.WIDTH/lArr+1, event.y, slot*self.WIDTH/lArr+self.WIDTH/lArr/2, self.HEIGHT, fill = "dodgerblue", width=0)
		self.create_text(slot*self.WIDTH/lArr+self.WIDTH/lArr/2, self.HEIGHT-3, text = str(slot), anchor = S, font="Symbol 8")
		if g < 0.01:
			g = 0.0
		self.arrG[slot] = g
		#self.arr[slot] = 1
	
	def setupSubs(self):
		self.delete("all")
		#self.arr = []
		lArr = len(self.arr)
		#print "setup"
		#print lArr
		for i in range(len(self.arr)):
			#print "slot",i
			#self.arr.append(0)
			self.create_line(i*self.WIDTH/lArr, 0, i*self.WIDTH/lArr, self.HEIGHT)
			if self.arr[i] == 1 or self.arr[i] == 3:
				self.create_rectangle(i*self.WIDTH/lArr+self.WIDTH/lArr/2, 0, i*self.WIDTH/lArr+self.WIDTH/lArr, self.HEIGHT/10, tags=("{}toggle".format(str(i))), fill = "green", width=0)
			if self.arr[i] == 2 or self.arr[i] or self.arr[i] == 3:
				self.create_rectangle(i*self.WIDTH/lArr, 0, i*self.WIDTH/lArr+self.WIDTH/lArr/2, self.HEIGHT/10, tags=("{}toggle".format(str(i))), fill = "red", width=0)
			self.create_text(i*self.WIDTH/lArr+self.WIDTH/lArr/2, self.HEIGHT-3, text = str(i), anchor = S, font="Symbol 8")
		#print self.arr


	def addSub(self):
		#print "adding"
		self.arr.append(0)
		self.arrG.append(1.0)
		#print self.arr
		#self.labelSubs.set(str(new))
		self.setupSubs()

	def subSub(self):
		#print "subbing"
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
		self.sizeX = 40
		self.connected = True

class BeatBox:
	def __init__(self, beat, x, y):
		self.beat = beat
		self.oX = x
		self. oY = y
		self.sizeX = 50
		self.sizeY = 50

class CueWindow(Toplevel):
	def __init__(self, master, instrument, can):
		self.i = instrument
		#print self.i.instrument.arr
		self.can = can
		self.master = master
		Toplevel.__init__(self)

		self.mainFrame = ttk.Frame(self)
		self.mainFrame.grid()

		self.timeCan = TimeCanvas(self.mainFrame, self.i.instrument.arr, self.i.instrument.arrG, self.i.instrument.arrP,width = 400, height = 70)
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
		#print self.i.instrument.arr
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
	def __init__(self, master, beat, oX, oY, can, beatDict):
		self.can = can
		self.beat = beat
		self.oX = oX
		self.oY = oY
		self.beats = beatDict
		Toplevel.__init__(self)

		#self.master = master
		self.title("configure beat")

		self.mainFrame = ttk.Frame(self)
		self.mainFrame.grid()

		self.nEntry = ttk.Entry(self.mainFrame)
		self.nEntry.grid(row = 0, column = 0, columnspan = 2)
		self.nEntry.insert(0, self.beat.n)

		self.tLabel = ttk.Label(self.mainFrame, text = "tempo")
		self.tLabel.grid(row = 1, column = 0)

		self.tEntry = ttk.Entry(self.mainFrame, width = 6)
		self.tEntry.grid(row = 1, column = 1)
		self.tEntry.insert(0, self.beat.t)
		
		self.lLabel = ttk.Label(self.mainFrame, text = "number of\n ticks")
		self.lLabel.grid(row = 2, column = 0)

		self.lEntry = ttk.Entry(self.mainFrame, width = 6)
		self.lEntry.grid(row = 2, column = 1)
		self.lEntry.insert(0, self.beat.l)

		self.sLabel = ttk.Label(self.mainFrame, text = "ticks per beat")
		self.sLabel.grid(row = 3, column = 0)

		self.sEntry = ttk.Entry(self.mainFrame, width = 6)
		self.sEntry.grid(row = 3, column = 1)
		self.sEntry.insert(0, self.beat.s)

		self.goButton = ttk.Button(self.mainFrame, text = "set", command = self.setBeat)
		self.goButton.grid(row = 4, column = 0, columnspan = 2, sticky=EW)
	def setBeat(self):
		self.beat.t = int(self.tEntry.get())
		self.beat.l = int(self.lEntry.get())
		self.beat.n = self.nEntry.get()
		self.beat.s = int(self.sEntry.get())

		b = BeatBox(self.beat, self.oX, self.oY)
		#print "BEATWINDOW:\n"+str(self.oX), str(self.oY)
		self.can.create_rectangle(b.oX, b.oY, b.oX+b.sizeX, b.oY+b.sizeY, fill = "white", tags=(self.nEntry.get(), "beat"))
		self.can.create_text(b.oX+1, b.oY+1, text=b.beat.n, anchor=NW, font ="Symbol 7", width=b.sizeX, tags=(self.nEntry.get(), "beat"))
		self.beats[self.nEntry.get()] = b
		#print self.beat.t
		#print self.beats
		self.destroy()
# A toplevel window for configuring an instrument in a beat
class InstWindow(Toplevel):
	def __init__(self, master, can, originX, originY, instrumentDict, beatDict, lineX, lineY, instrument):
		self.can = can
		self.iDict = instrumentDict
		self.bDict = beatDict
		self.oX = originX
		self.oY = originY
		self.lineX = lineX
		self.lineY = lineY
		self.i = instrument

		self.labelSubs = StringVar()
		self.labelSubs.set(str(16))
		self.arr = []
		
		self.WIDTH = 600
		self.HEIGHT = 200

		Toplevel.__init__(self)
		self.mainFrame = ttk.Frame(self)
		self.mainFrame.grid()
		
		self.upperFrame = ttk.Frame(self.mainFrame)
		self.upperFrame.grid(row = 0, column = 0)
		##### FILLER ARRAYS
		self.timeCan = TimeCanvas(self.upperFrame, self.i.arr, self.i.arrG, self.i.arrP, width = self.WIDTH, height = self.HEIGHT)
		self.timeCan.grid(row = 0, column = 0)
		

		self.PMFrame = ttk.Frame(self.upperFrame)
		self.PMFrame.grid(row = 0, column = 1, sticky = N)


		self.pButton = ttk.Button(self.PMFrame, text = "+", command = self.timeCan.addSub)
		self.pButton.grid(row  = 1, column = 0)
		self.mButton = ttk.Button(self.PMFrame, text = "-", command = self.timeCan.subSub)
		self.mButton.grid(row = 2, column = 0)

		self.delButton = ttk.Button(self.PMFrame, text = "Delete", command = self.delete)
		self.delButton.grid(row = 3, column = 0, sticky = S)

		self.envelope = ENV(self.PMFrame, self.i.env)
		self.envelope.grid(row = 4)

		self.lowerFrame = ttk.Frame(self.mainFrame)
		self.lowerFrame.grid(row = 1, column = 0, sticky = W)

		self.tName = ttk.Entry(self.lowerFrame, width = 10)
		self.tName.grid(row = 0, column = 0)
		self.tName.insert(0, self.i.n)

		self.tSource = ttk.Entry(self.lowerFrame)
		self.tSource.grid(row = 0, column = 1)

		source = "track_source"
		if self.iDict.get(self.i.n):
			source = self.iDict[self.i.n].instrument.source

		self.tSource.insert(0, source)

		self.boxVal = StringVar()
		self.lBox = ttk.Combobox(self.lowerFrame, textvariable=self.boxVal, width = 10)
		self.lBox['values'] = ("sample","beat", "osc")
		#self.lBox.current("osc")
		self.lBox.grid(row = 0, column = 2)

		self.goButton = ttk.Button(self.lowerFrame, text = "Make", command = self.make)
		self.goButton.grid(row = 0, column = 3)

		self.bind("e",self.edit)

		#self.timeCan.setupSubs()

	def delete(self):
		try:
			del self.iDict[self.i.n]
		except KeyError:
			pass
		self.can.delete(self.i.n)
		self.destroy()

	def edit(self, event):
		self.timeCan.focus_set()

	def make(self):
		#i = Instrument(self.tName.get(), source=self.tSource.get())
		#################
		self.i.n = self.tName.get()
		self.i.source = self.tSource.get()
		self.i.t = self.boxVal.get()
		self.i.env = self.envelope.get()
		#print self.i.env

		#print self.i.t
		self.i.setArray(self.timeCan.arr, self.timeCan.arrG, self.timeCan.arrP)
		b = Box(self.i, self.oX, self.oY)
		self.iDict[self.i.n] = b
		#self.can.delete("line&&{}".format(self.tName.get()))

		#print b.oX, b.oY, b.oX+b.sizeX, b.oY+b.sizeY
		self.can.create_line(self.lineX, self.lineY, self.oX, self.oY, tags=(self.tName.get(), "instrument", "line"))
		self.can.create_rectangle(b.oX, b.oY, b.oX+b.sizeX, b.oY+b.sizeY, fill = "white", tags=(self.tName.get(), "instrument"))
		self.can.create_text(b.oX+1, b.oY+1, text=b.instrument.n, anchor=NW, font ="Symbol 7", width=b.sizeX, tags=(self.tName.get(), "instrument"))
		if self.i.t == "beat" and not self.i.connected:
			self.i.connected = True
			if self.bDict.get(self.tSource.get(), False):
				#print self.bDict[self.tSource.get()].oX, self.bDict[self.tSource.get()].oX
				self.can.create_line(b.oX+b.sizeX, b.oY+b.sizeY, self.bDict[self.tSource.get()].oX, self.bDict[self.tSource.get()].oY, dash=(3,), tags=("line"))
		#for j, k in enumerate(self.i.arr):
		#	if k == 1:
		#		self.can.create_line(b.oX+1+j*2, b.oY+b.sizeY-3,b.oX+1+j*2, b.oY+b.sizeY,tags=(self.tName.get(), "instrument"))
		self.can.tag_lower("line")
		self.destroy()

#### LATER!!!!!!!!!!!

class RateWindow(Toplevel):
	def __init__(self, master):
		Toplevel.__init__(self)
		self.master = master
		self.mainFrame = ttk.Frame(self)
		self.mainFrame.grid()



if __name__ == '__main__':
	root = Tk()
	f = Frame(root)
	#f.grid()
	#RateWindow(frame)
	t = RateWindow(f)
	root.mainloop()