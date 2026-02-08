# CentrifugeDemo
OCR Centrifuge Demo Controls using google AI.
Arduino pwm with potentiometer sample code with sketch

# Description
To control an output using a potentiometer's input via PWM,
the Arduino reads the analog value from the potentiometer and maps it to the appropriate output range (0-255). This is a common method for dimming an LED or controlling motor speed.

# AI Overview
To control an output using a potentiometer's input via PWM,
the Arduino reads the analog value from the potentiometer and maps it to the appropriate output range (0-255). This is a common method for dimming an LED or controlling motor speed. 
Required Components

* Arduino Board: Arduino MEGA 2560
* Potentiometer 10K Ohm Potentometer
* LED and a matching resistor (around 220 Ohm) if controlling LED brightness
* Breadboard and jumper wires 

# Circuit Diagram
* Connect one outer pin of the potentiometer to the Arduino's 5V pin.
* Connect the other outer pin of the potentiometer to the Arduino's GND pin.
* Connect the middle (wiper) pin of the potentiometer to an analog input pin (e.g., A0).
* Connect the positive (longer) leg of the LED to a PWM-enabled digital pin (e.g., pin 9). PWM pins are marked with a tilde (~) on the board.
* Connect the negative (shorter) leg of the LED to GND, in series with the resistor.

# Circuit Pinout
Component 	Arduino Pin
Potentiometer (VCC)	5V
Potentiometer (GND)	GND
Potentiometer (Signal)	A0
LED Anode (+ Resistor)	Pin 9 (PWM ~)
LED Cathode	GND