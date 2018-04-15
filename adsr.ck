SinOsc s1 => ADSR e1 => dac;
Noise n1 => e1 => dac;
50 => s1.freq;
0.0015 => n1.gain;
e1.set( 0::ms, 0::ms, 1, 00::ms );

SndBuf2 s2 => ADSR e2 => dac;
me.dir()+"samples/snare1" => string snFile;
Noise n2 => e2 => dac;
0.01 => n2.gain;
e2.set( 10::ms, 60::ms, .001, 80::ms );

ADSR e3 => dac;
Noise n3 => e3 => dac;
//100 => s3.freq;
0.05 => n3.gain;
e3.set( 50::ms, 50::ms, .01, 400::ms );

0.15::second => dur tick;
//12 3 4 5 6 7 8 9 10 11 12 13 14 15 16
//[0] @=> int e1A[];
[3,2,0,0,0,0,1,2,0,0, 0, 0, 0, 0, 0, 1] @=> int e1A[]; 
[0,0,0,1,2,0,0,0,0,0, 0, 1, 2, 0, 0, 0] @=> int e2A[];
[0,1,3,2,0,0,0,0,1,2, 0, 0, 0, 1, 3, 2] @=> int e3A[];
for (0 => int i; i < 64; i++) {
    
    
    if (e1A[i%e1A.cap()] == 1) {
        e1.keyOn();
    } else if (e1A[i%e1A.cap()] == 2) {
        e1.keyOff();
    } else if (e1A[i%e1A.cap()] == 3) {
        e1.keyOff();
        e1.keyOn();
    }
    
    if (e2A[i%e2A.cap()] == 1) {
        e2.keyOn();
        snFile => s2.read;
    } else if (e2A[i%e2A.cap()] == 2) {
        e2.keyOff();
    } else if (e2A[i%e2A.cap()] == 3) {
        e2.keyOff();
        e2.keyOn();
    }
    
    if (e3A[i%e3A.cap()] == 1) {
        e3.keyOn();
    } else if (e3A[i%e3A.cap()] == 2) {
        e3.keyOff();
    } else if (e3A[i%e3A.cap()] == 3) {
        e3.keyOff();
        e3.keyOn();
    }
    tick => now;
}
e1.keyOff();
// 5::second => now;