#include <Arduino.h>

/*
 * This ESP32 code is created by esp32io.com
 *
 * This ESP32 code is released in the public domain
 *
 * For more detail (instruction and wiring diagram), visit https://esp32io.com/tutorials/esp32-ultrasonic-sensor
 */

#define TRIG_PIN D2 // ESP32 pin GPIO23 connected to Ultrasonic Sensor's TRIG pin
#define ECHO_PIN D3 // ESP32 pin GPIO22 connected to Ultrasonic Sensor's ECHO pin

float duration_us, distance_cm;

unsigned long startpoint = 0;
boolean millis_check;

void afstand() {
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  duration_us = pulseIn(ECHO_PIN, HIGH);
  distance_cm = 0.017 * duration_us;
  Serial.print("distance: ");
  Serial.print(distance_cm);
  Serial.println(" cm");
}

void afstandnakijken() {
  if (distance_cm <= 10) {
    Serial.println("Object is dichtbij");
  }
  else {
    Serial.println("Object is ver weg");
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  if (startpoint + 1000 < millis()) {
    startpoint = millis();
    millis_check = true;
    afstand();
    afstandnakijken();
  }
  if (millis_check) {
    Serial.println("10 second passed");
    millis_check = false;
  }
}