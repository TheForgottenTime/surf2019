// Dont forget to ground the arduino with the battery
/*
 * 2400-544=1856
 * 1856/180=10.311
 * 10.311*44=453.66
 * 453.68+544=997.68us
 * Shows the motor will turn on at 1ms
 */

#include "ServoTimer2.h" servo.write sets the frequency of pulse being sent to the esc.The Pheonix edge requires
// a constant pulse rate, changing duty cycle instead to alter the speed of the motor. Without the ability to
// alter the Duty Cylce instead of the pulse rate, we cant control the esc, so we cannot use SERVO.h, but
// instead use PWM functions (8kz pulse rate).

#include <AltSoftSerial.h>

ServoTimer2 escs[6];
ServoTimer2 directions[2];

//===============================================================================================
int escPins[6] = {9, 10, 2, 3, 4, 5}; //Set the pin numbers for motors. Must be PWM. First two have directions. Set to -1 if not connected
int directionPins[2] = {4, 5};        //Set the pin numbers that control the direction of the big motors. Must be PWM
//===============================================================================================

int minPulseWidth = 1000;
int maxPulseWidth = 1100;
int throttleChangeDelay = 100;
int currentThrottle[6] = {0, 0, 90, 90, 90, 90}; //The initial throttle of each motor

AltSoftSerial altSerial;

//================================ SETUP =========================================================
void setup()
{
  altSerial.begin(9600);
  altSerial.setTimeout(500);

  //Attach the motors to the correct pins
  for (int i = 0; i < 6; i++)
  {
    if (escPins[i] != -1)
    {
      escs[i].attach(escPins[i], minPulseWidth, maxPulseWidth);
      escs[i].write(currentThrottle[i]);
      printStuff("[SETUP] Attached Motor ", i, " to pin ", escPins[i]);
    }
  }
  //Attach direction to the correct pins
  for (int i = 0; i < 2; i++)
  {
    if (directionPins[i] != -1)
    {
      directions[i].attach(directionPins[i]);
      printStuff("[SETUP] Attached direction ", i, " to pin ", directionPins[i]);
    }
  }
  altSerial.println("Usage: {Motor Number 0-5},{Throttle Position 0-180},{[Optional] Direction 0-1}");
}

//================================ MAIN LOOP =======================================================
void loop()
{
  if (altSerial.available())
  {
    //Read the throttle value and store into variables
    String input = altSerial.readString();
    int commaIndex1 = input.indexOf(',');
    int commaIndex2 = input.indexOf(',', commaIndex1 + 1);
    int motor = (input.substring(0, commaIndex1)).toInt();
    int throttle = normalize((input.substring(commaIndex1 + 1, commaIndex2)).toInt());
    int dir = (input.substring(commaIndex2 + 1)).toInt();

    //First check if motor is connected
    if (escPins[motor] != -1 or motor < 0 or motor > 5)
    {

      //Change the direction if necessary
      if (motor == 0 or motor == 1)
      {
        if (dir == 0)
        {
          directions[motor].write(0);
          printStuff("Setting Motor ", motor, " to direction ", dir);
        }
        else
        {
          directions[motor].write(180);
          printStuff("Setting Motor ", motor, " to direction ", dir);
        }
      }

      //If the throttle has changed then proceed to change it
      if (throttle != currentThrottle[motor])
      {
        changeThrottle(motor, throttle);
      }
      else
      {
        printStuff("Motor ", motor, " already at throttle ", throttle);
      }
    }
    else
    {
      altSerial.println("[ERROR] Motor not connected");
    }
  }
}
//================================ CHANGE THROTTLE =================================================
void changeThrottle(int m, int t)
{
  printStuff("Setting Motor ", m, " to throttle ", t);
  //Step by one until the correct value is reached
  int delta = 1; //the step size
  if (t < currentThrottle[m])
  {
    delta = -1;
  }
  currentThrottle[m] = t;
  escs[m].write(currentThrottle[m]);
  while (true)
  {
    if (currentThrottle[m] == t)
    {
      break;
    }
    currentThrottle[m] += delta;
    printStuff("Motor: ", m, " Throttle: ", currentThrottle[m]);
    escs[m].write(currentThrottle[m]);
    delay(throttleChangeDelay);
  }
}
//================================ NORMALIZE ========================================================
//Make the throttle values between 0 and 180
int normalize(int t)
{
  if (t < 0)
  {
    return 0;
  }
  else if (t > 180)
  {
    return 180;
  }
  return t;
}

//==================================== PRINT =========================================================
//Arduino was being difficult printing strings and ints together
void printStuff(const String one, const int two, const String three, const int four)
{
  String two_s = String(two);
  String four_s = String(four);
  altSerial.println(one + two_s + three + four_s);
}
