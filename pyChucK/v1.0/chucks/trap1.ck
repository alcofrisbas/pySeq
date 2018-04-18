135 => float bpm;
60/bpm => float tempo;
(tempo/4)::second => dur tick;
SndBuf2 hihat => dac;
me.dir() + "samples/tss.wav" => string hihatFile;
SndBuf2 hihat-O => dac;
me.dir() + "samples/tssz.wav" => string hihat-OFile;
SndBuf2 bass => dac;
me.dir() + "samples/tboom.wav" => string bassFile;
SndBuf2 clap => dac;
me.dir() + "samples/clap.wav" => string clapFile;
SndBuf2 hihat_O => dac;
me.dir() + "samples/tssz.wav" => string hihat_OFile;
[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0] @=> int hihatA[];
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] @=> int hihat-OA[];
[1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0] @=> int bassA[];
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] @=> int clapA[];
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] @=> int hihat_OA[];
for (0 => int i; i < 256; i++) {
	if (true && hihatA[i%hihatA.cap()] == 1) {
		hihatFile => hihat.read;
	}
	if (true && hihat-OA[i%hihat-OA.cap()] == 1) {
		hihat-OFile => hihat-O.read;
	}
	if (true && bassA[i%bassA.cap()] == 1) {
		bassFile => bass.read;
	}
	if (true && clapA[i%clapA.cap()] == 1) {
		clapFile => clap.read;
	}
	if (true && hihat_OA[i%hihat_OA.cap()] == 1) {
		hihat_OFile => hihat_O.read;
	}
	 tick => now;
}