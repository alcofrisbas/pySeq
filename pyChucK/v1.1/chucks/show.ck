120 => float bpm;
60/bpm => float tempo;
(tempo/4)::second => dur tick;
SndBuf2 snare => dac;
me.dir() + "samples/snare1.wav" => string snareFile;
SndBuf2 tss => dac;
me.dir() + "samples/tss.wav" => string tssFile;
0.8 => tss.rate;
SndBuf2 kick => dac;
me.dir() + "samples/boom.wav" => string kickFile;
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0] @=> int snareA[];
[1.0, 1.0, 1.0, 1.0, 0.6533333333333333, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.56, 1.0, 0.52, 1.0] @=> float snareAG[];
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] @=> int tssA[];
[0.5066666666666666, 0.4666666666666667, 0.4933333333333333, 0.4933333333333333, 0.41333333333333333, 0.4666666666666667, 0.45333333333333337, 0.45333333333333337, 0.45333333333333337, 0.45333333333333337, 0.45333333333333337, 0.45333333333333337, 0.41333333333333333, 0.45333333333333337, 0.3866666666666667, 0.42666666666666664] @=> float tssAG[];
[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1] @=> int kickA[];
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float kickAG[];
for (0 => int i; i < 256; i++) {
	if (true && snareA[i%snareA.cap()] == 1) {
		snareAG[i%snareAG.cap()] => snare.gain;
		snareFile => snare.read;
	}
	if (true && tssA[i%tssA.cap()] == 1) {
		tssAG[i%tssAG.cap()] => tss.gain;
		tssFile => tss.read;
	}
	if(i == 16) {
		[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1] @=> tssA;
	}
	if (true && kickA[i%kickA.cap()] == 1) {
		kickAG[i%kickAG.cap()] => kick.gain;
		kickFile => kick.read;
	}
	 tick => now;
}