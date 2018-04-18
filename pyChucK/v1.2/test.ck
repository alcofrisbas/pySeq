Math.pow(2, 1.0/12) => float a;
440=> float f0;
fun float note(int n) {
	return f0 * Math.pow(a, n)
;}
function void MAIN() {
	80 => float bpm;
	60/bpm => float tempo;
	(tempo/4)::second => dur tick;
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] @=> int track_nameA[];
	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float track_nameAG[];
	for (0 => int i; i < 256; i++) {
		if (track_nameA[i%track_nameA.cap()] == 1) {
			spork ~ track_source();
	}
		 tick => now;
	}
}
MAIN();