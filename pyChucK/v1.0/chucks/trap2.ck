140 => float bpm;
60/bpm => float tempo;
(tempo/4)::second => dur tick;
SndBuf2 hihat => dac;
me.dir() + "samples/tss.wav" => string hihatFile;
0.7 => hihat.gain;
0.5 => hihat.gain;
SndBuf2 bass => dac;
me.dir() + "samples/tboom.wav" => string bassFile;
SndBuf2 bass2 => dac;
me.dir() + "samples/boom.wav" => string bass2File;
0.5 => bass2.gain;
1.5 => bass2.rate;
0.7 => bass2.rate;
0.9 => bass2.rate;
SndBuf2 bass3 => dac;
me.dir() + "samples/tboom2.wav" => string bass3File;
SndBuf2 snare => dac;
me.dir() + "samples/snare1.wav" => string snareFile;
SndBuf2 clap => dac;
me.dir() + "samples/clap.wav" => string clapFile;
0.5 => clap.gain;
0.3 => clap.gain;
0 => clap.gain;
0.2 => clap.gain;
SndBuf2 hihatO => dac;
me.dir() + "samples/tssz.wav" => string hihatOFile;
0.4 => hihatO.gain;
[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0] @=> int hihatA[];
[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] @=> int bassA[];
[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] @=> int bass2A[];
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] @=> int bass3A[];
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] @=> int snareA[];
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] @=> int clapA[];
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] @=> int hihatOA[];
for (0 => int i; i < 256; i++) {
	if (true && hihatA[i%hihatA.cap()] == 1) {
		hihatFile => hihat.read;
	}
	if (true && bassA[i%bassA.cap()] == 1) {
		bassFile => bass.read;
	}
	if (true && bass2A[i%bass2A.cap()] == 1) {
		bass2File => bass2.read;
	}
	if (true && bass3A[i%bass3A.cap()] == 1) {
		bass3File => bass3.read;
	}
	if (true && snareA[i%snareA.cap()] == 1) {
		snareFile => snare.read;
	}
	if (true && clapA[i%clapA.cap()] == 1) {
		clapFile => clap.read;
	}
	if (true && hihatOA[i%hihatOA.cap()] == 1) {
		hihatOFile => hihatO.read;
	}
	 tick => now;
}