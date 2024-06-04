/* bron: https://randomnerdtutorials.com/esp32-http-get-open-weather-map-thingspeak-arduino/
https://arduinojson.org/v6/example/
https://arduinojson.org/?utm_source=meta&utm_medium=library.properties*/

#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include "wifi_secrets.h"

unsigned long startpoint = 0;
boolean millis_check;

#define LED1  18
#define LED2  19
#define LED3  23
#define LED4  21
#define LED5  22 

String payload;

void initWifi() {
  Serial.print("Connecting to WiFi: ");
  Serial.println(WIFI_SSID);
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected to WiFi network");
}

void get_data() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverName);
    int httpResponseCode = http.GET();
    if (httpResponseCode > 0) {
      payload = http.getString();
      Serial.println(payload);
    } else {
      Serial.print("Error code: ");
      Serial.println(httpResponseCode);
    }
    http.end();
  }
}

void updateLedStatus() {
  DynamicJsonDocument doc(2048); // Vergroot de buffer indien nodig
  DeserializationError error = deserializeJson(doc, payload);
  if (error) {
    Serial.print("deserializeJson() failed: ");
    Serial.println(error.c_str());
    return;
  }

  JsonArray arr = doc.as<JsonArray>();
  for (JsonVariant v : arr) {
    JsonObject nestedObj = v.as<JsonObject>();
    String id = nestedObj["ReserveringID"].as<String>();
    String status = nestedObj["Reservering_Status"].as<String>();

    if (id == "6f954476-06ee-11ef-acec-c4b301cc06d7") {
      if (status == "Gereserveerd") {
        digitalWrite(LED1, HIGH);
        Serial.print("led 1 is aan met id ");
        Serial.println(id);
        Serial.println("Reservering 1 is Gereserveerd");
      } else {
        digitalWrite(LED1, LOW);
        Serial.println("Reservering 1 is niet Gereserveerd");
      }
    }

    if (id == "6f95405c-06ee-11ef-acec-c4b301cc06d7") {
      if (status == "Gereserveerd") {
        digitalWrite(LED2, HIGH);
        Serial.print("led 2 is aan met id ");
        Serial.println(id);
        Serial.println("Reservering 2 is Gereserveerd");
      } else {
        digitalWrite(LED2, LOW);
        Serial.println("Reservering 2 is niet Gereserveerd");
      }
    }

    if (id == "6f954412-06ee-11ef-acec-c4b301cc06d7") {
      if (status == "Gereserveerd") {
        digitalWrite(LED3, HIGH);
        Serial.print("led 3 is aan met id ");
        Serial.println(id);
        Serial.println("Reservering 3 is Gereserveerd");
      } else {
        digitalWrite(LED3, LOW);
        Serial.println("Reservering 3 is niet Gereserveerd");
      }
    }

    if (id == "6f9544b2-06ee-11ef-acec-c4b301cc06d7") {
      if (status == "Gereserveerd") {
        digitalWrite(LED4, HIGH);
        Serial.print("led 4 is aan met id ");
        Serial.println(id);
        Serial.println("Reservering 4 is Gereserveerd");
      } else {
        digitalWrite(LED4, LOW);
        Serial.println("Reservering 4 is niet Gereserveerd");
      }
    }

    if (id == "6f95452a-06ee-11ef-acec-c4b301cc06d7") {
      if (status == "Gereserveerd") {
        digitalWrite(LED5, HIGH);
        Serial.print("led 5 is aan met id ");
        Serial.println(id);
        Serial.println("Reservering 5 is Gereserveerd");
      } else {
        digitalWrite(LED5, LOW);
        Serial.println("Reservering 5 is niet Gereserveerd");
      }
    }
  }
}
void setup() {
  Serial.begin(115200);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(LED4, OUTPUT);
  pinMode(LED5, OUTPUT);
  initWifi();
}

// void loop() {
//     for (int i = 1; i <= 100; i++) {
//       get_data();
//       updateLedStatus();
//       Serial.print("Huidige iteratie: ");
//       Serial.println(i);
//       if (i == 100) {
//       }
//     }
//     while (1) {
//     }
// }

void loop() {
  if (startpoint + 10000 < millis()) {  
    startpoint = millis();
    millis_check = true;
    get_data();
    updateLedStatus();
  }
  if (millis_check) {
    Serial.println("10 seconds passed");
    millis_check = false;
  }
}