/*Run this and open Serial Plotter in the tools menu*/

void setup() {
  Serial.begin(9600); 
}

void loop() {
  Serial.print(0);  // To freeze the lower limit
  Serial.print(" ");
  Serial.print(500);  // To freeze the upper limit
  Serial.print(" ");
  Serial.println(analogRead(0));
  delay(1);
}
