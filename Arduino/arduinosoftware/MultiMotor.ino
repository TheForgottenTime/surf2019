// Dont forget to ground the arduino with the battery

#include <Servo.h>

Servo escs[6];

int escPins[6] = {9,10,-1,-1,-1,-1};   //Set the pin numbers for motors. Set -1 if not connected
int minPulseRate = 500;
int maxPulseRate = 1500;
int throttleChangeDelay = 100;
int currentThrottle[6] = {90,90,90,90,90,90};

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(500);

  //Attach the motors to the correct pins
  for(int i=0; i<6; i++)
  {
    if(escPins[i] != -1) {
      escs[i].attach(escPins[i], minPulseRate, maxPulseRate);
      escs[i].write(90);
      printStuff("Attached Motor ", i, " to pin ", escPins[i]);
    }
  }
  Serial.println("Usage: {Motor Number 0-5},{Throttle Position 0-180}");
}

void loop() {
  if(Serial.available()) {
    //Read the throttle value and store into variables
    String input = Serial.readString();
    int commaIndex = input.indexOf(',');
    int motor = (input.substring(0,commaIndex)).toInt();
    int throttle = normalize((input.substring(commaIndex+1)).toInt()); 

    //First check if motor is connected
    if(escPins[motor] != -1) {
      //If the throttle has changed then proceed in changing it
      if(throttle != currentThrottle[motor]) {
        changeThrottle(motor,throttle);
      }
      else {
        printStuff("Motor ",motor," already at throttle ",throttle);
      }
    }
    else {
      Serial.println("Motor not connected");
    }
  }

}

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

//Arduino was being difficult printing strings and ints together
void printStuff(const String one,const int two, const String three, const int four)
{
  String two_s = String(two);
  String four_s = String(four);
  Serial.println(one + two_s + three + four_s);
}
