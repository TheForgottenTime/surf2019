Always perform gpioInitialise()
when starting program and gpioTerminate()
before exiting.

Prepare the pins to be used as output for signal.
gpioSetMode(thepin, PI_OUTPUT)
//the pin = pin connected to signal on ESC
//PI_OUTPUT = constant variable for indicating the pin will be output

gpioServo(thepin, 1000)
//This sends a power off signal to the ESC, this must be done before
//the motors can be spinned up. This is due in part to how servos work
Spin them up!
gpioServo(thepin, 1500)
//This sends a PWM signal of 1500 to the ESC, from what I have read
//this is halfway point. Pigpio will not allow anything > 2500
gpioServo(thepin, 1000)
//Spin them down before exiting program

Remember to gpioTerminate()
