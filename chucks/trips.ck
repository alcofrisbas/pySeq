SndBuf2 kick => dac;
me.dir() + "samples/tboom2.wav" => string kickFile;
SndBuf2 snare => dac;
me.dir() + "samples/snare1.wav" => string snareFile;
function void MAIN() {
	80 => float bpm;
	60/bpm => float tempo;
	(tempo/4)::second => dur tick;
	[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] @=> int SnareHA[];
	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float SnareHAG[];
	[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0] @=> int kickA[];
	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float kickAG[];
	for (0 => int i; i < 256; i++) {
		if (SnareHA[i%SnareHA.cap()] == 1) {
			spork ~ tripSnare();
	}
		if (kickA[i%kickA.cap()] == 1) {
			kickAG[i%kickAG.cap()] => kick.gain;
			kickFile => kick.read;
	}
		 tick => now;
	}
}
function void tripSnare() {
	96 => float bpm;
	60/bpm => float tempo;
	(tempo/4)::second => dur tick;
	[1] @=> int snareA[];
	[1.0] @=> float snareAG[];
	for (0 => int i; i < 3; i++) {
		if (snareA[i%snareA.cap()] == 1) {
			snareAG[i%snareAG.cap()] => snare.gain;
			snareFile => snare.read;
	}
		 tick => now;
	}
}
MAIN();