/*
 * Arduino PWM with Potentiometer
 * Reads an analog input pin, maps the result to a range from 0 to 255, 
 * and uses the result to set the pulse width modulation (PWM) of an output pin.
 */

// These constants won't change:
const int analogInPin = A0;   // Analog input pin that the potentiometer is attached to
const int analogOutPin = 9;  // Analog output pin that the LED is attached to (must be PWM pin, e.g., 3, 5, 6, 9, 10, or 11 on Uno)

int sensorValue = 0;        // value read from the pot
int outputValue = 0;        // value output to the PWM (analog out)

void setup() {
  // Initialize serial communications at 9600 bps for debugging:
  Serial.begin(9600); 
}

void loop() {
  // Read the analog in value:
  sensorValue = analogRead(analogInPin);            

  // Map it to the range of the analog out (0-1023 -> 0-255):
  outputValue = map(sensorValue, 0, 1023, 0, 255);    

  // Change the analog out value:
  analogWrite(analogOutPin, outputValue);           

  // Print the results to the Serial Monitor:
  Serial.print("Sensor Value = ");
  Serial.print(sensorValue);
  Serial.print("\t Output Value = ");
  Serial.println(outputValue);

  // Wait a little bit so the serial monitor is not flooded
  delay(10); 
}
