Math.pow(2, 1.0/12) => float a;
440=> float f0;
fun float note(int n) {
	return f0 * Math.pow(a, n)
;}
SinOsc s1 => dac;
0 => s1.gain;
function void MAIN() {
	80 => float bpm;
	60/bpm => float tempo;
	(tempo/4)::second => dur tick;
	[8, 0, 10, 0, 8, 0, 0, 0, 2, -4, 0, 0, 0, 0, -17, 0] @=> int s1A[];
	[1.0, 1.0, 0.010000000000000009, 0.010000000000000009, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float s1AG[];
	for (0 => int i; i < 256; i++) {
		if (true) {
			s1AG[i%s1AG.cap()] => s1.gain;
			s1note(AG[i%s1A.cap()]) => s1.freq;
		 tick => now;
	}
}
MAIN();