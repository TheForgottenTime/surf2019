// Dont forget to ground the arduino with the battery
/*
 * 2400-544=1856
 * 1856/180=10.311
 * 10.311*44=453.66
 * 453.68+544=997.68us
 * Shows the motor will turn on at 1ms
 */

#include <Servo.h>  servo.write sets the frequency of pulse being sent to the esc. The Pheonix edge requires
// a constant pulse rate, changing duty cycle instead to alter the speed of the motor. Without the ability to
// alter the Duty Cylce instead of the pulse rate, we cant control the esc, so we cannot use SERVO.h, but
// instead use PWM functions (8kz pulse rate).

Servo escs[6];
Servo directions[2];

//===============================================================================================
int escPins[6] = {9,10,2,3,4,5};    //Set the pin numbers for motors. Must be PWM. First two have directions. Set to -1 if not connected
int directionPins[2] = {4,5};           //Set the pin numbers that control the direction of the big motors. Must be PWM
//===============================================================================================

int minPulseWidth = 1000;
int maxPulseWidth = 1100;
int currentThrottle[6] = {0,0,90,90,90,90};   //The initial throttle of each motor
int currentDirections[2] = {0,0};
//================================ SETUP =========================================================
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(500);

  //Attach the motors to the correct pins
  for(int i=0; i<6; i++)
  {
    if(escPins[i] != -1) {
      escs[i].attach(escPins[i], minPulseWidth, maxPulseWidth);
      escs[i].write(currentThrottle[i]);
      printStuff("[SETUP] Attached Motor ", i, " to pin ", escPins[i]);
    }
  }
  //Attach direction to the correct pins
  for(int i=0; i<2; i++) {
    if(directionPins[i] != -1) {
      directions[i].attach(directionPins[i]);
      printStuff("[SETUP] Attached direction ",i, " to pin ",directionPins[i]);
    }
  }
  Serial.println("Usage: {Motor Number 0-5},{Throttle Position 0-180},{[Optional] Direction 0-1}");
}

//================================ MAIN LOOP =======================================================
void loop() {
  if(Serial.available()) {
    //Read the throttle value and store into variables
    String input = Serial.readString();
    int commaIndex1 = input.indexOf(',');
    int commaIndex2 = input.indexOf(',',commaIndex1+1);
    int motor = (input.substring(0,commaIndex1)).toInt();
    int throttle = (input.substring(commaIndex1+1,commaIndex2)).toInt();
    int dir = (input.substring(commaIndex2+1)).toInt();

    //update the arrays
    if(motor < 2){
      currentDirections[motor] = dir;
    }
    currentThrottle[motor] = throttle;
  }

  changeThrottle(0);
  changeThrottle(1);
  changeThrottle(2);
  changeThrottle(3);
  changeThrottle(4);
  changeThrottle(5);

}
//================================ CHANGE THROTTLE =================================================
void changeThrottle(int motor)
{
  if(m < 2){
    directions[motor].write(currentDirections[motor]*180);
  }
  escs[m].write(currentThrottle[motor]);
}
//================================ NORMALIZE ========================================================