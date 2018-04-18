Math.pow(2, 1.0/12) => float a;
440=> float f0;
fun float note(int n) {
	return f0 * Math.pow(a, n)
;}
SndBuf2 hihatO => dac;
me.dir() + "samples/tssz.wav" => string hihatOFile;
SndBuf2 hihatC => dac;
me.dir() + "samples/tss.wav" => string hihatCFile;
SndBuf2 clap => dac;
me.dir() + "samples/clap.wav" => string clapFile;
SndBuf2 snare => dac;
me.dir() + "samples/snare1.wav" => string snareFile;
SndBuf2 kick => dac;
me.dir() + "samples/boom.wav" => string kickFile;
SinOsc b1 => ADSR eb1=> dac;
eb1.set(30::ms, 50::ms, 0.5, 150::ms);

function void MAIN() {
	135 => float bpm;
	60/bpm => float tempo;
	(tempo/4)::second => dur tick;
	[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] @=> int hihatOA[];
	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.55, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float hihatOAG[];
	[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0] @=> int hihatCA[];
	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float hihatCAG[];
	[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] @=> int clapA[];
	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.39, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float clapAG[];
	[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] @=> int snareA[];
	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float snareAG[];
	[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] @=> int kickA[];
	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float kickAG[];
	[1, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] @=> int b1A[];
	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float b1AG[];
	[-28, -28, -28, -28, -28, -28, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] @=> int b1AP[];
	for (0 => int i; i < 256; i++) {
		if (hihatOA[i%hihatOA.cap()] == 1) {
			hihatOAG[i%hihatOAG.cap()] => hihatO.gain;
			hihatOFile => hihatO.read;
	}
		if (hihatCA[i%hihatCA.cap()] == 1) {
			hihatCAG[i%hihatCAG.cap()] => hihatC.gain;
			hihatCFile => hihatC.read;
	}
		if (clapA[i%clapA.cap()] == 1) {
			clapAG[i%clapAG.cap()] => clap.gain;
			clapFile => clap.read;
	}
		if (snareA[i%snareA.cap()] == 1) {
			snareAG[i%snareAG.cap()] => snare.gain;
			snareFile => snare.read;
	}
		if (kickA[i%kickA.cap()] == 1) {
			kickAG[i%kickAG.cap()] => kick.gain;
			kickFile => kick.read;
	}
		if (b1A[i%b1A.cap()] == 1) {eb1.keyOn();}
		else if (b1A[i%b1A.cap()] == 2) {eb1.keyOff();}
		else if (b1A[i%b1A.cap()] == 3) {eb1.keyOff(); eb1.keyOn();}
		note(b1AP[i%b1AP.cap()]) => b1.freq;
		tick => now;
	}
}
MAIN();