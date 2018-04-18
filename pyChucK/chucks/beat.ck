Math.pow(2, 1.0/12) => float a;
440=> float f0;
fun float note(int n) {
	return f0 * Math.pow(a, n)
;}
SndBuf2 snareR => dac;
me.dir() + "samples/snare1.wav" => string snareRFile;
Math.pow(2, 1.0/12) => float a;
440=> float f0;
fun float note(int n) {
	return f0 * Math.pow(a, n)
;}
SndBuf2 hihatO => dac;
me.dir() + "samples/tssz.wav" => string hihatOFile;
SndBuf2 hihatC => dac;
me.dir() + "samples/tss.wav" => string hihatCFile;
SinOsc s1 => dac;
0 => s1.gain;SinOsc s1Bass => dac;
0 => s1Bass.gain;SndBuf2 snare => dac;
me.dir() + "samples/snare1.wav" => string snareFile;
SndBuf2 kick => dac;
me.dir() + "samples/tboom2.wav" => string kickFile;
function void sRamp() {
	192 => float bpm;
	60/bpm => float tempo;
	(tempo/4)::second => dur tick;
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] @=> int snareRA[];
	[0.11499999999999999, 0.17000000000000004, 0.21999999999999997, 0.29500000000000004, 0.35, 0.41500000000000004, 0.45499999999999996, 0.505, 0.575, 0.625, 0.64, 0.755, 0.8049999999999999, 0.855, 0.92, 1.0] @=> float snareRAG[];
	for (0 => int i; i < 8; i++) {
		if (snareRA[i%snareRA.cap()] == 1) {
			snareRAG[i%snareRAG.cap()] => snareR.gain;
			snareRFile => snareR.read;
	}
		 tick => now;
	}
}
function void MAIN() {
	96 => float bpm;
	60/bpm => float tempo;
	(tempo/4)::second => dur tick;
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0] @=> int hihatOA[];
	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float hihatOAG[];
	[0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0] @=> int hihatCA[];
	[1.0, 0.61, 0.595, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.515, 0.515, 0.515, 1.0, 1.0, 1.0, 1.0] @=> float hihatCAG[];
	[1, 1, 1, 0, -2, 0, 2, 4, 2, 0, 1, 1, 1, 1, 1, 0] @=> int s1A[];
	[0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.015000000000000013, 0.010000000000000009, 0.010000000000000009, 0.010000000000000009, 0.010000000000000009, 1.0] @=> float s1AG[];
	[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] @=> int sRampHA[];
	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float sRampHAG[];
	[-19, -36, -47, -28, -34, -34, -43, -43, -54, -35, -52, -39, -26, -30, -13, -39] @=> int s1BassA[];
	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float s1BassAG[];
	[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] @=> int snareA[];
	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float snareAG[];
	[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1] @=> int kickA[];
	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float kickAG[];
	for (0 => int i; i < 256; i++) {
		if (hihatOA[i%hihatOA.cap()] == 1) {
			hihatOAG[i%hihatOAG.cap()] => hihatO.gain;
			hihatOFile => hihatO.read;
	}
		if (hihatCA[i%hihatCA.cap()] == 1) {
			hihatCAG[i%hihatCAG.cap()] => hihatC.gain;
			hihatCFile => hihatC.read;
	}
		if (true) {
			s1AG[i%s1AG.cap()] => s1.gain;
			note(s1A[i%s1A.cap()]) => s1.freq;
	}
		if (sRampHA[i%sRampHA.cap()] == 1) {
			spork ~ sRamp();
	}
		if (true) {
			s1BassAG[i%s1BassAG.cap()] => s1Bass.gain;
			note(s1BassA[i%s1BassA.cap()]) => s1Bass.freq;
	}
		if(i == 32) {
			[-22, -24, -22, -27, -29, -31, -37, -33, -29, -25, -21, -19, -17, -16, -15, -16] @=> s1BassA;
	}
		if (snareA[i%snareA.cap()] == 1) {
			snareAG[i%snareAG.cap()] => snare.gain;
			snareFile => snare.read;
	}
		if (kickA[i%kickA.cap()] == 1) {
			kickAG[i%kickAG.cap()] => kick.gain;
			kickFile => kick.read;
	}
		 tick => now;
	}
}
MAIN();