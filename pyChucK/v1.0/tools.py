import os, sys

class Instrument:
	def __init__(self, n, source=""):
		self.n = n
		self.source = source
		self.arr = [0]
		self.opt = "true"
		self.opts = []
		self.cues = {}

	def setArray(self, arr):
		self.arr = arr

	def addOpt(self, o):
		self.opts.append(o)

	def addCue(self, t, c):
		self.cues[t] = str(c)

	def __str__(self):
		s = 'SndBuf2 {} => dac;\nme.dir() + "{}" => string {}File;\n'.format(self.n, self.source, self.n)
		for o in self.opts:
			s += o
		return s

class Beat:
	def __init__(self, l,t):
		self.l = l
		self.t = t
		self.instruments = {}

	def add(self,i):
		self.instruments[i.n] = i

	def clear(self):
		self.instruments = {}

	def __str__(self):
		nT = 0
		s = "{} => float bpm;\n".format(self.t)
		s +="60/bpm => float tempo;\n"+\
		"(tempo/4)::second => dur tick;\n"
		for i in self.instruments:
			s += self.instruments[i].__str__()

		for i in self.instruments:
			s += str(self.instruments[i].arr) + " @=> int {}A[];\n".format(self.instruments[i].n)
		
		s += "for (0 => int i; i < {}; i++) {{\n".format(self.l)
		nT += 1
		for i in self.instruments:
			s += "\tif ({} && {}A[i%{}A.cap()] == 1) {{\n".format(self.instruments[i].opt, self.instruments[i].n, self.instruments[i].n)
			s += "\t\t{}File => {}.read;\n\t}}\n".format(self.instruments[i].n, self.instruments[i].n)
		
			for c in self.instruments[i].cues:
				s += "\tif(i == {}) {{\n".format(c)
				s += "\t\t{} @=> {}A;\n\t}}\n".format(str(self.instruments[i].cues[c]), self.instruments[i].n)
		s += "\t tick => now;\n"
		s += "}"


		return s

	def write(self, fname):
		with open(fname, "w") as w:
			w.write(self.__str__())

if __name__ == '__main__':
	b = Beat(256, 80)

	i = Instrument("tok", "tok.wav")
	#print i

	b.add(i)
	print b

	b.write("test.ck")