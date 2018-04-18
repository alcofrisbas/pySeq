Math.pow(2, 1.0/12) => float a;
440=> float f0;
fun float note(int n) {
	return f0 * Math.pow(a, n)
;}
SndBuf2 s2 => dac;
me.dir() + "SinOsc" => string s2File;
function void MAIN() {
	80 => float bpm;
	60/bpm => float tempo;
	(tempo/4)::second => dur tick;
	[1, 1, 1, 1, 1, 19, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] @=> int s2A[];
	[0.495, 0.45999999999999996, 0.485, 0.49, 0.495, 0.495, 0.475, 0.515, 0.525, 0.5, 0.525, 0.525, 0.525, 0.54, 0.54, 0.5449999999999999] @=> float s2AG[];
	for (0 => int i; i < 256; i++) {
		if (s2A[i%s2A.cap()] == 1) {
			s2AG[i%s2AG.cap()] => s2.gain;
			s2File => s2.read;
	}
		 tick => now;
	}
}
MAIN();