SinOsc s => ADSR e => dac;
SndBuf2 s2 => dac;
120 => float bpm;
bpm/60 => float tempo;
4 => int subs;

tempo/subs => dur tick;

