Hid hi;
HidMsg msg;

SinOsc s => ADSR e => LPF f => dac;
e.set(10::ms, 100::ms,0.3,100::ms);
f.set(150.0, 1.0);


// which keyboard
0 => int device;
// get from command line
if( me.args() ) me.arg(0) => Std.atoi => device;

// open keyboard (get device number from command line)
if( !hi.openKeyboard( device ) ) me.exit();
<<< "keyboard '" + hi.name() + "' ready", "" >>>;

// infinite event loop
while( true )
{
    // wait on event
    hi => now;
    
    // get one or more messages
    while( hi.recv( msg ) )
    {
        // check for action type
        if( msg.isButtonDown() )
        {
            e.keyOn();
            //<<< "down:", msg.which, "(code)", msg.key, "(usb key)", msg.ascii, "(ascii)" >>>;
        }
        
        else if ( msg.isButtonUp() )
        {
             e.keyOff();
            //<<< "up:", msg.which, "(code)", msg.key, "(usb key)", msg.ascii, "(ascii)" >>>;
        }
    }
}