Math.pow(2, 1.0/12) => float a;
440=> float f0;
fun float note(int n) {
	return f0 * Math.pow(a, n)
;}
SinOsc s1 => ADSR es1=> dac;
es1.set(10::ms, 100::ms, 0.5, 150::ms);
function void MAIN() {
	80 => float bpm;
	60/bpm => float tempo;
	(tempo/4)::second => dur tick;
	[1, 3, 3, 3, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 2] @=> int s1A[];
	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float s1AG[];
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] @=> int s1AP[];
	for (0 => int i; i < 256; i++) {
		if (s1A[i%s1A.cap()] == 1) {es1.keyOn();}
		else if (s1A[i%s1A.cap()] == 2) {es1.keyOff();}
		else if (s1A[i%s1A.cap()] == 3) {es1.keyOff(); es1.keyOn();}
		tick => now;
	}
}
MAIN();