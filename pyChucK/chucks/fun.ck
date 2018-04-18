Math.pow(2, 1.0/12) => float a;
440=> float f0;
fun float note(int n) {
	return f0 * Math.pow(a, n)
;}
SndBuf2 kick => dac;
me.dir() + "samples/tboom2.wav" => string kickFile;
SndBuf2 snare => dac;
me.dir() + "NEW_BEAT" => string snareFile;
function void MAIN() {
	80 => float bpm;
	60/bpm => float tempo;
	(tempo/4)::second => dur tick;
	[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] @=> int snareHA[];
	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float snareHAG[];
	[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1] @=> int kickA[];
	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float kickAG[];
	for (0 => int i; i < 256; i++) {
		if (snareHA[i%snareHA.cap()] == 1) {
			spork ~ NEW_BEAT();
	}
		if (kickA[i%kickA.cap()] == 1) {
			kickAG[i%kickAG.cap()] => kick.gain;
			kickFile => kick.read;
	}
		if(i == 32) {
			[1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1] @=> kickA;
	}
		 tick => now;
	}
}
function void NEW_BEAT() {
	80 => float bpm;
	60/bpm => float tempo;
	(tempo/3)::second => dur tick;
	[1] @=> int snareA[];
	[1.0] @=> float snareAG[];
	for (0 => int i; i < 1; i++) {
		if (snareA[i%snareA.cap()] == 1) {
			snareAG[i%snareAG.cap()] => snare.gain;
			snareFile => snare.read;
	}
		 tick => now;
	}
}
MAIN();