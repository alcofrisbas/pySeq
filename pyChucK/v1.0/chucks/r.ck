80 => float bpm;
60/bpm => float tempo;
(tempo/4)::second => dur tick;
SndBuf2 kick => dac;
me.dir() + "samples/boom.wav" => string kickFile;
0.9 => kick.gain;
[1, 0, 0, 0, 1, 0, 0, 0] @=> int kickA[];
for (0 => int i; i < 256; i++) {
	if (true && kickA[i%kickA.cap()] == 1) {
		kickFile => kick.read;
	}
	if(i == 31) {
		[1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1] @=> kickA;
	}
	if(i == 63) {
		[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0] @=> kickA;
	}
	 tick => now;
}