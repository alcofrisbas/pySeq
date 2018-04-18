Math.pow(2, 1.0/12) => float a;
440=> float f0;
fun float note(int n) {
	return f0 * Math.pow(a, n)
;}
SndBuf2 hihatC => dac;
me.dir() + "samples/tss.wav" => string hihatCFile;
function void timeTest() {
	120 => float bpm;
	60/bpm => float tempo;
	(tempo/3)::second => dur tick;
	[1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1] @=> int hihatCA[];
	[1.0, 1.0, 1.0, 0.49, 1.0, 0.48, 1.0, 1.0, 1.0, 0.5, 1.0, 0.48] @=> float hihatCAG[];
	for (0 => int i; i < 12; i++) {
		if (hihatCA[i%hihatCA.cap()] == 1) {
			hihatCAG[i%hihatCAG.cap()] => hihatC.gain;
			hihatCFile => hihatC.read;
	}
		 tick => now;
	}
}
function void MAIN() {
	120 => float bpm;
	60/bpm => float tempo;
	(tempo/4)::second => dur tick;
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] @=> int hSwangA[];
	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float hSwangAG[];
	for (0 => int i; i < 256; i++) {
		if (hSwangA[i%hSwangA.cap()] == 1) {
			spork ~ timeTest();
	}
		 tick => now;
	}
}
MAIN();