from tools import *

b = Beat(256, 80)
i = Instrument("tik", source="tik.wav")
i.setArray([1,0,0,0])
b.add(i)
b.write("pyBeat.ck")