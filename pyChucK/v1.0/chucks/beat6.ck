80 => float bpm;
60/bpm => float tempo;
(tempo/4)::second => dur tick;
SndBuf2 kick => dac;
me.dir() + "samples/boom.wav" => string kickFile;
[1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0] @=> int kickA[];
for (0 => int i; i < 256; i++) {
	if (true && kickA[i%kickA.cap()] == 1) {
		kickFile => kick.read;
	}
	 tick => now;
}