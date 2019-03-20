//this code write potentiometer data(A0) to the servo motors (pin 9)

#include <Servo.h>
String incomingString = ""; 
int potpin = 0;  // analog pin used to connect the potentiometer
int val;


Servo jetLeft;
Servo jetRight;
Servo frontLeft;
Servo frontRight;
Servo backLeft;
Servo backRight;
 
void setup()
{
  Serial.begin(9600);
  
  jetLeft.attach(2);
  jetRight.attach(3);
  frontLeft.attach(4);
  frontRight.attach(5);
  backLeft.attach(6);
  backRight.attach(7);
  arm();

}

void arm(){
 //arm the motors with 90 which is neutral.
 setSpeed(0, jetLeft);
 setSpeed(0, jetRight);
 setSpeed(90, frontLeft);
 setSpeed(90, frontRight);
 setSpeed(90, backLeft);
 setSpeed(90, backRight);
 delay(1000); //delay 1 second,  some speed controllers may need longer
}

void setSpeed(int speed, Servo _servo){
 // speed is from 0 to 100 where 0 is off and 100 is maximum speed
 //the following maps speed values of 0-100 to angles from 0-180,
 // some speed controllers may need different values, see the ESC instructions
 int angle = map(speed, 0, 100, 0, 180);
 jetLeft.write(angle);    
}

void goForward(int speed, float rateOfChange){
  jetLeft.write(speed);
  jetRight.write(speed);
}

void loop()
{
  setSpeed(val, jetLeft);      
  if (Serial.available() > 0) {
                // read the incoming byte:
                incomingString = Serial.readString();
                Serial.println("I received: ");
                String motorString = getValue(incomingString, ':', 0);
                String speedString = getValue(incomingString, ':', 1);
                String gradientString = getValue(incomingString, ':', 2);

                int motor = motorString.toInt();
                int speed = speedString.toInt();
                //double gradient = gradientString.toDouble();
                
                Serial.println("Motor:");
                Serial.print(motor, DEC);
                Serial.println("Speed:");
                Serial.print(speed, DEC);
                goForward(speed, 1);
                //Serial.println("Gradient:" + gradient);
                //Serial.println(incomingByte, DEC);
        }
}
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

String getValue(String data, char separator, int index)
{
    int found = 0;
    int strIndex[] = { 0, -1 };
    int maxIndex = data.length() - 1;

    for (int i = 0; i <= maxIndex && found <= index; i++) {
        if (data.charAt(i) == separator || i == maxIndex) {
            found++;
            strIndex[0] = strIndex[1] + 1;
            strIndex[1] = (i == maxIndex) ? i+1 : i;
        }
    }
    return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}
