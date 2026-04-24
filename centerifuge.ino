/****************************************************
 * Centrifuge PWM Controller (Serial Commands)
 *
 * Commands received over Serial (newline terminated):
 *  1000  -> Motor ON
 *  1001  -> Motor OFF
 *  1     -> Increment speed by 1
 * -1     -> Decrement speed by 1
 ****************************************************/

// ===== Includes =====
// (Arduino core provides everything needed)

// ===== Pin Configuration =====
const int PWM_PIN = 9;

// ===== Safety Limits =====
const int MAX_PWM = 160;
const int MIN_PWM = 145;

// ===== State Variables =====
int currentPWM = 0;
bool motorEnabled = false;

void setup() {
  Serial.begin(115200);
  pinMode(PWM_PIN, OUTPUT);
  analogWrite(PWM_PIN, 0);   // motor off at boot
}

void loop() {
  if (Serial.available() > 0) {
    int cmd = Serial.parseInt();

    // Flush remaining characters (newline, etc.)
    while (Serial.available()) {
      Serial.read();
    }

    // -------- Command Handling --------
    if (cmd == 1000) {
      motorEnabled = true;           // ON
    }
    else if (cmd == 1001) {
      motorEnabled = false;          // OFF
    }
    else if (cmd == 1) {
      currentPWM += 1;               // increment
    }
    else if (cmd == -1) {
      currentPWM -= 1;               // decrement
    }

    // -------- Clamp PWM --------
    if (currentPWM > MAX_PWM) currentPWM = MAX_PWM;
    if (currentPWM < MIN_PWM) currentPWM = MIN_PWM;

    // -------- Output --------
    if (motorEnabled) {
      analogWrite(PWM_PIN, currentPWM);
    } else {
      analogWrite(PWM_PIN, 0);
    }

    // -------- Debug --------
    Serial.print("Enabled: ");
    Serial.print(motorEnabled);
    Serial.print(" | PWM: ");
    Serial.println(currentPWM);
  }
}
