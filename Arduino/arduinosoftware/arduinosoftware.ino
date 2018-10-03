#include <Servo.h>
 
Servo esc;
 
void setup()
{
esc.attach(9);
}
 
void loop()
{
esc.write(10);
}
