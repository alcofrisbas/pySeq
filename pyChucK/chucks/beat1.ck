80 => float bpm;
60/bpm => float tempo;
(tempo/4)::second => dur tick;
SndBuf2 hihatO => dac;
me.dir() + "samples/tssz.wav" => string hihatOFile;
SndBuf2 hihatC => dac;
me.dir() + "samples/tss.wav" => string hihatCFile;
SndBuf2 tok => dac;
me.dir() + "samples/tok.wav" => string tokFile;
SndBuf2 kick => dac;
me.dir() + "samples/tboom2.wav" => string kickFile;
SndBuf2 tik => dac;
me.dir() + "samples/tik.wav" => string tikFile;
SndBuf2 snare => dac;
me.dir() + "samples/snare1.wav" => string snareFile;
SndBuf2 clap => dac;
me.dir() + "samples/clap.wav" => string clapFile;
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0] @=> int hihatOA[];
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float hihatOAG[];
[0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0] @=> int hihatCA[];
[1.0, 1.0, 0.56, 0.33333333333333337, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5333333333333333, 0.2533333333333333, 1.0, 1.0, 1.0, 1.0] @=> float hihatCAG[];
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] @=> int tokA[];
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.45333333333333337, 0.4, 0.42666666666666664, 1.0, 1.0] @=> float tokAG[];
[1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1] @=> int kickA[];
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float kickAG[];
[0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0] @=> int tikA[];
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float tikAG[];
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] @=> int snareA[];
[1.0, 1.0, 1.0, 1.0, 0.41333333333333333, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3733333333333333, 1.0, 1.0, 1.0] @=> float snareAG[];
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0] @=> int clapA[];
[1.0, 0.053333333333333344, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.7333333333333334, 1.0, 1.0, 0.3466666666666667, 1.0, 1.0] @=> float clapAG[];
for (0 => int i; i < 256; i++) {
	if (true && hihatOA[i%hihatOA.cap()] == 1) {
		hihatOAG[i%hihatOAG.cap()] => hihatO.gain;
		hihatOFile => hihatO.read;
	}
	if (true && hihatCA[i%hihatCA.cap()] == 1) {
		hihatCAG[i%hihatCAG.cap()] => hihatC.gain;
		hihatCFile => hihatC.read;
	}
	if (true && tokA[i%tokA.cap()] == 1) {
		tokAG[i%tokAG.cap()] => tok.gain;
		tokFile => tok.read;
	}
	if (true && kickA[i%kickA.cap()] == 1) {
		kickAG[i%kickAG.cap()] => kick.gain;
		kickFile => kick.read;
	}
	if (true && tikA[i%tikA.cap()] == 1) {
		tikAG[i%tikAG.cap()] => tik.gain;
		tikFile => tik.read;
	}
	if (true && snareA[i%snareA.cap()] == 1) {
		snareAG[i%snareAG.cap()] => snare.gain;
		snareFile => snare.read;
	}
	if (true && clapA[i%clapA.cap()] == 1) {
		clapAG[i%clapAG.cap()] => clap.gain;
		clapFile => clap.read;
	}
	 tick => now;
}