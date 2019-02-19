// Dont forget to ground the arduino with the battery

#include <Servo.h>

Servo escs[6];
Servo directions[2];

//===============================================================================================
int escPins[6] = {9,10,-1,-1,-1,-1};    //Set the pin numbers for motors. Must be PWM. First two have directions. Set to -1 if not connected
int directionPins[2] = {4,5};           //Set the pin numbers that control the direction of the big motors. Must be PWM
//===============================================================================================

int minPulseRate = 500;
int maxPulseRate = 1500;
int throttleChangeDelay = 100;
int currentThrottle[6] = {0,0,90,90,90,90};   //The initial throttle of each motor

//================================ SETUP =========================================================
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(500);

  //Attach the motors to the correct pins
  for(int i=0; i<6; i++)
  {
    if(escPins[i] != -1) {
      escs[i].attach(escPins[i], minPulseRate, maxPulseRate);
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
    int throttle = normalize((input.substring(commaIndex1+1,commaIndex2)).toInt());
    int dir = (input.substring(commaIndex2+1)).toInt();

    //First check if motor is connected
    if(escPins[motor] != -1 or motor < 0 or motor > 5) {
      
      //Change the direction if necessary
      if(motor == 0 or motor == 1) {
        if(dir == 0 or dir == 1) {
          directions[motor].write(dir);
          printStuff("Setting Motor ",motor," to direction ",dir);
        }
        else {
          Serial.println("Direction out of range. Ignoring.");
        }
      }

      //If the throttle has changed then proceed to change it
      if(throttle != currentThrottle[motor]) {
        changeThrottle(motor,throttle);
      }
      else {
        printStuff("Motor ",motor," already at throttle ",throttle);
      }
    }
    else {
      Serial.println("[ERROR] Motor not connected");
    }
  }

}
//================================ CHANGE THROTTLE =================================================
void changeThrottle(int m, int t)
{
  printStuff("Setting Motor ",m," to throttle ",t);
  int delta = 1;    //the step size
  if(t < currentThrottle[m]) {
    delta = -1;
  }

  //Step by one until the correct value is reached
  while(true) {
    if(currentThrottle[m] == t) { break; }
      currentThrottle[m] += delta;
      printStuff("Motor: ",m," Throttle: ",currentThrottle[m]);
      escs[m].write(currentThrottle[m]);
      delay(throttleChangeDelay);
  }
}
//================================ NORMALIZE ========================================================
//Make the throttle values between 0 and 180
int normalize(int t)
{
  if(t < 0) {
    return 0;
  }
  else if(t > 180) {
    return 180;
  }
  return t;
}

//==================================== PRINT =========================================================
//Arduino was being difficult printing strings and ints together
void printStuff(const String one,const int two, const String three, const int four)
{
  String two_s = String(two);
  String four_s = String(four);
  Serial.println(one + two_s + three + four_s);
}
