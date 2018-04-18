80 => float bpm;
60/bpm => float tempo;
(tempo/4)::second => dur tick;
SndBuf2 clap => dac;
me.dir() + "samples/clap.wav" => string clapFile;
[1, 1, 0] @=> int clapA[];
[0.6799999999999999, 0.2533333333333333, 0] @=> float clapAG[];
for (0 => int i; i < 256; i++) {
	if (true && clapA[i%clapA.cap()] == 1) {
		clapAG[i%clapAG.cap()] => clap.gain;
		clapFile => clap.read;
	}
	 tick => now;
}