100 => float bpm;
60/bpm => float tempo;
(tempo/4)::second => dur tick;
SndBuf2 kick => dac;
me.dir() + "samples/boom.wav" => string kickFile;
SndBuf2 clap => dac;
me.dir() + "samples/clap.wav" => string clapFile;
0.5 => clap.gain;
[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1] @=> int kickA[];
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] @=> int clapA[];
for (0 => int i; i < 256; i++) {
	if (true && kickA[i%kickA.cap()] == 1) {
		kickFile => kick.read;
	}
	if (true && clapA[i%clapA.cap()] == 1) {
		clapFile => clap.read;
	}
	if(i == 47) {
		[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0] @=> clapA;
	}
	if(i == 31) {
		[0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] @=> clapA;
	}
	 tick => now;
}