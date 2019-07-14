// Dont forget to ground the arduino with the battery
// Set signal value, which should be between 1100 and 1900

#include <Servo.h>  

Servo escs[6];
#define INPUT_SIZE 41 //1:1111&2:2222&3:3333&4:4444&5:5555&6:6666

//===============================================================================================
int escPins[6] = {7,9,5,4,3,2};    //Set the pin numbers for motors. Must be PWM. First two have directions. Set to -1 if not connected
//===============================================================================================
int throttleArray[6] = {1500,1500,1500,1500,1500,1500};   
/* 0 => Motor 1   Right Forward ESC
 * 1 => Motor 2   Left Foward ESC
 * 2 => Motor 3   FR ESC
 * 3 => Motor 4   BR ESC
 * 4 => Motor 5   FL ESC
 * 5 => Motor 6   BL ESC

 */
//================================ SETUP =========================================================
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(500);

  //Attach the motors to the correct pins
  for(int i=0; i<6; i++)
  {
    if(escPins[i] != -1) {
      escs[i].attach(escPins[i]);
      escs[i].writeMicroseconds(throttleArray[i]);  
      delay(7000); //Delay to let the ESC setup
    }
  }  
}

//================================ MAIN LOOP =======================================================
void loop() {
  char input[INPUT_SIZE+1]; //Add 1 for trailing 0
  byte size = Serial.readBytes(input,INPUT_SIZE);
  input[size] = 0;  //Add trailing 0
  bool processFlag = false;

  //Read each command pair
  char* command = strtok(input,"&");
  while(command != 0) {
    processFlag = true;
    //Split the command into two values
    char* separator = strchr(command,':');
    if(separator != 0) {
      *separator = 0;   //Replace ':' with 0
      int motorID = atoi(command);
      ++separator;
      int value = atoi(separator);
      throttleArray[motorID] = value;
      changeThrottle(motorID);
    }
    //Find the next command in input string
    command = strtok(0,"&");
    
  }
  
  //All commands have been processed. Tell sender its OK to send more
  if(processFlag) {
    Serial.println("OK"); 
    processFlag = false;
  }
}
//================================ CHANGE THROTTLE =================================================
void changeThrottle(int motor)
{
  escs[motor].writeMicroseconds(throttleArray[motor]);

  //DEBUGGING 
  Serial.print(motor);
  Serial.print(" is at ");
  Serial.println(throttleArray[motor]);
}
