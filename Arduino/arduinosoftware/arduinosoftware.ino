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
}
 
void loop()
{
 val = analogRead(potpin);            // reads the value of the potentiometer (value between 0 and 1023)
  val = map(val, 0, 660, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
  Serial.println(val);                  // sets the servo position according to the scaled value
  esc.write(val);      

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
