//this code write potentiometer data(A0) to the servo motors (pin 9)

#include <Servo.h>
int incomingByte = 0; 
int potpin = 0;  // analog pin used to connect the potentiometer
int val;
Servo esc;
 
void setup()
{
  Serial.begin(9600);
  esc.attach(9);
  arm();
}

void arm(){
 // arm the speed controller, modify as necessary for your ESC  
 setSpeed(0); 
 delay(1000); //delay 1 second,  some speed controllers may need longer
}

void setSpeed(int speed){
 // speed is from 0 to 100 where 0 is off and 100 is maximum speed
 //the following maps speed values of 0-100 to angles from 0-180,
 // some speed controllers may need different values, see the ESC instructions
 int angle = map(speed, 0, 100, 0, 180);
 esc.write(angle);    
}

void loop()
{
 val = analogRead(potpin);            // reads the value of the potentiometer (value between 0 and 1023)
  val = map(val, 0, 660, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
  Serial.println(val);                  // sets the servo position according to the scaled value
  setSpeed(val);      

  /*
  if (Serial.available() > 0) {
                // read the incoming byte:
                incomingByte = Serial.parseInt();
                Serial.println("I received: ");
                Serial.println(incomingByte);
                Serial.println(incomingByte, DEC);
                esc.write(incomingByte);
        }

*/
}
