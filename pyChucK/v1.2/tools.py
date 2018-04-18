import os, sys

"""

There's a main beat.

Beats can control instruments

Beats can also be called asynchronously by instruments.
HOW? -- beats are written as functions.
the main beat is played by a function call.

Prelude, or soundGen is at the head of the file.

each beat is a function that is sporked...?
What starts it?
is the main beat a special beat?

instead of the beat calling a sndbuf read command, it calls
a spork function command! done.

"""


class Instrument:
	def __init__(self, n, t,  p,source=""):
		self.n = n # name
		self.p = p # parent( beat object)
		self.source = source #source(either sound file, beat name, or oscilator type)
		self.fillArrs()
		#self.arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		#self.arrG = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
		self.opts = []
		self.cues = {}
		self.t = t # type
		self.connected = False

	def fillArrs(self):
		self.arr = [0 for i in range(self.p.s*4)]
		self.arrG = [1.0 for i in range(self.p.s*4)]

	def setArray(self, arr, arrG):
		self.arr = arr
		self.arrG = arrG

	def addOpt(self, o):
		self.opts.append(o)

	def addCue(self, t, c):
		self.cues[t] = str(c)

	def __str__(self):
		s = ""
		if self.t == "sample":
			s = 'SndBuf2 {} => dac;\nme.dir() + "{}" => string {}File;\n'.format(self.n, self.source, self.n)
		elif self.t == "osc":
			s = "{} {} => dac;\n0 => {}.gain;".format(self.source, self.n, self.n)
		return s

class Beat:
	def __init__(self, n,l,t,s):
		self.n = n # name
		self.l = l # lenght(number of ticks)
		self.t = t # tempo (beats per second)
		self.s = s # subdivision(ticks per beat)
		self.instruments = {}

	def add(self,i):
		self.instruments[i.n] = i

	def clear(self):
		self.instruments = {}
	
	def prelude(self):
		s = ""
		
		for i in self.instruments:
			s += self.instruments[i].__str__()
		return s
	
	def __str__(self):
		nT = 0
		s = "function void {}() {{\n".format(self.n)
		s += "\t{} => float bpm;\n".format(self.t)
		s +="\t60/bpm => float tempo;\n"+\
		"\t(tempo/{})::second => dur tick;\n".format(self.s)

		for i in self.instruments:
			s += "\t"+str(self.instruments[i].arr) + " @=> int {}A[];\n".format(self.instruments[i].n)
			s += "\t"+str(self.instruments[i].arrG) + " @=> float {}AG[];\n".format(self.instruments[i].n)
		
		s += "\tfor (0 => int i; i < {}; i++) {{\n".format(self.l)
		nT += 1
		# too lazy to make tabs look nice...oops
		for i in self.instruments:
			if self.instruments[i].t == "osc":
				cond = "true"
			else:
				cond = "{}A[i%{}A.cap()] == 1".format(self.instruments[i].n, self.instruments[i].n)
			s += "\t\tif ({}) {{\n".format(cond)
			if self.instruments[i].t == "sample":
				s += "\t\t\t{}AG[i%{}AG.cap()] => {}.gain;\n".format(self.instruments[i].n,self.instruments[i].n,self.instruments[i].n)
				s += "\t\t\t{}File => {}.read;\n\t}}\n".format(self.instruments[i].n, self.instruments[i].n)
			elif self.instruments[i].t == "osc":
				s += "\t\t\t{}AG[i%{}AG.cap()] => {}.gain;\n".format(self.instruments[i].n,self.instruments[i].n,self.instruments[i].n)
				s += "\t\t\tnote({}A[i%{}A.cap()]) => {}.freq;\n\t}}\n".format(self.instruments[i].n,self.instruments[i].n,self.instruments[i].n)
			elif self.instruments[i].t == "beat":
				s += "\t\t\tspork ~ {}();\n\t}}\n".format(self.instruments[i].source)
		
			for c in self.instruments[i].cues:
				s += "\t\tif(i == {}) {{\n".format(c)
				s += "\t\t\t{} @=> {}A;\n\t}}\n".format(str(self.instruments[i].cues[c]), self.instruments[i].n)
		s += "\t\t tick => now;\n\t}\n"
		s += "}\n"


		return s

	def write(self, fname):
		with open(fname, "w") as w:
			w.write(self.__str__())

if __name__ == '__main__':
	b = Beat(256, 80)

	i = Instrument("tok", "tok.wav")
	#print i
	i.setArray([1,0,0,0,1,0,0,0], [1,0,0,0,0.5,0,0,0,])
	b.add(i)
	print b

	b.write("test.ck")