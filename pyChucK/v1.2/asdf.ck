Math.pow(2, 1.0/12) => float a;
440=> float f0;
fun float note(int n) {
	return f0 * Math.pow(a, n)
;}
function void MAIN() {
	80 => float bpm;
	60/bpm => float tempo;
	(tempo/4)::second => dur tick;
	for (0 => int i; i < 256; i++) {
		 tick => now;
	}
}
MAIN();