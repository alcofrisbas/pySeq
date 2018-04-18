80 => float bpm;
60/bpm => float tempo;
(tempo/4)::second => dur tick;
SndBuf2 kick => dac;
me.dir() + "samples/boom.wav" => string kickFile;
SndBuf2 clap => dac;
me.dir() + "samples/clap.wav" => string clapFile;
SndBuf2 tss => dac;
me.dir() + "samples/tss.wav" => string tssFile;
[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1] @=> int kickA[];
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] @=> int clapA[];
[0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0] @=> int tssA[];
for (0 => int i; i < 256; i++) {
	if (true && kickA[i%kickA.cap()] == 1) {
		kickFile => kick.read;
	}
	if (true && clapA[i%clapA.cap()] == 1) {
		clapFile => clap.read;
	}
	if (true && tssA[i%tssA.cap()] == 1) {
		tssFile => tss.read;
	}
	 tick => now;
}