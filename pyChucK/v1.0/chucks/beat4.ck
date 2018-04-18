120 => float bpm;
60/bpm => float tempo;
(tempo/4)::second => dur tick;
SndBuf2 kick => dac;
me.dir() + "samples/boom.wav" => string kickFile;
1 => kick.gain;
SndBuf2 clap => dac;
me.dir() + "samples/clap.wav" => string clapFile;
0.5 => clap.gain;
SndBuf2 tik => dac;
me.dir() + "samples/tik.wav" => string tikFile;
[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1] @=> int kickA[];
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] @=> int clapA[];
[0, 0, 0, 0, 0, 1] @=> int tikA[];
for (0 => int i; i < 256; i++) {
	if (true && kickA[i%kickA.cap()] == 1) {
		kickFile => kick.read;
	}
	if (true && clapA[i%clapA.cap()] == 1) {
		clapFile => clap.read;
	}
	if (true && tikA[i%tikA.cap()] == 1) {
		tikFile => tik.read;
	}
	 tick => now;
}