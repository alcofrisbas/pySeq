SndBuf2 snare => dac;
me.dir() + "samples/snare1.wav" => string snareFile;
function void snareMain() {
	80 => float bpm;
	60/bpm => float tempo;
	(tempo/4)::second => dur tick;
	[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] @=> int snareA[];
	[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] @=> float snareAG[];
	for (0 => int i; i < 256; i++) {
		if (snareA[i%snareA.cap()] == 1) {
			snareAG[i%snareAG.cap()] => snare.gain;
			snareFile => snare.read;
        }
		 tick => now;
     }
}
function void MAIN() {
	80 => float bpm;
	60/bpm => float tempo;
	(tempo/4)::second => dur tick;
	[1] @=> int snareHandA[];
	[1.0] @=> float snareHandAG[];
	for (0 => int i; i < 1; i++) {
		if (snareHandA[i%snareHandA.cap()] == 1) {
			snareHandAG[i%snareHandAG.cap()] => snare.gain;
			spork ~ snareMain();
        }
	
		 tick => now;
     }
};
MAIN();
1::minute => now;