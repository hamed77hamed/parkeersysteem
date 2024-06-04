#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include "wifi_secrets.h"
#include <ArduinoJson.h>

#define LED1  18
#define LED2  19
#define LED3  23
#define LED4  21
#define LED5  22

String payload;

#define TRIG_PIN1 D3   
#define ECHO_PIN1 D2

#define TRIG_PIN2 D5   
#define ECHO_PIN2 D4

#define TRIG_PIN3 D7   
#define ECHO_PIN3 D6

#define TRIG_PIN4 D8  
#define ECHO_PIN4 D9

#define TRIG_PIN5 A0  
#define ECHO_PIN5 A1

String status_Sensor1 = "Beschikbaar";
String status_Sensor2 = "Beschikbaar";
String status_Sensor3 = "Beschikbaar";
String status_Sensor4 = "Beschikbaar";
String status_Sensor5 = "Beschikbaar";

const float afstand = 10;

float duration_us_Sensor1, distance_cm_Sensor1;
float duration_us_Sensor2, distance_cm_Sensor2;
float duration_us_Sensor3, distance_cm_Sensor3;
float duration_us_Sensor4, distance_cm_Sensor4;
float duration_us_Sensor5, distance_cm_Sensor5;

unsigned long startpoint = 0;
boolean millis_check;

boolean statusuitofaan1 = false;
boolean statusuitofaan2 = false;
boolean statusuitofaan3 = false;
boolean statusuitofaan4 = false;
boolean statusuitofaan5 = false;

void postData_Sensor1() {
  if (WiFi.status() == WL_CONNECTED) {
    String urlFinal = serverName_Sensor1 + "/" + status_Sensor1 + "/" + distance_cm_Sensor1; 
    Serial.print("POST data to flask: ");
    Serial.println(urlFinal);
    HTTPClient http;
    http.begin(urlFinal.c_str());
    int httpCode = http.GET();
    Serial.print("HTTP Status Code: ");
    Serial.println(httpCode);
    if (httpCode > 0) {
      String payload = http.getString();
      //Serial.println("Payload: " + payload);
    }
    http.end();
  }
}

void postData_Sensor2() {
  if (WiFi.status() == WL_CONNECTED) {
    String urlFinal = serverName_Sensor2 + "/" + status_Sensor2 + "/" + distance_cm_Sensor2; 
    Serial.print("POST data to flask: ");
    Serial.println(urlFinal);
    HTTPClient http;
    http.begin(urlFinal.c_str());
    int httpCode = http.GET();
    Serial.print("HTTP Status Code: ");
    Serial.println(httpCode);
    if (httpCode > 0) {
      String payload = http.getString();
      //Serial.println("Payload: " + payload);
    }
    http.end();
  }
}

void postData_Sensor3() {
  if (WiFi.status() == WL_CONNECTED) {
    String urlFinal = serverName_Sensor3 + "/" + status_Sensor3 + "/" + distance_cm_Sensor3; 
    Serial.print("POST data to flask: ");
    Serial.println(urlFinal);
    HTTPClient http;
    http.begin(urlFinal.c_str());
    int httpCode = http.GET();
    Serial.print("HTTP Status Code: ");
    Serial.println(httpCode);
    if (httpCode > 0) {
      String payload = http.getString();
      //Serial.println("Payload: " + payload);
    }
    http.end();
  }
}

void postData_Sensor4() {
  if (WiFi.status() == WL_CONNECTED) {
    String urlFinal = serverName_Sensor4 + "/" + status_Sensor4 + "/" + distance_cm_Sensor4; 
    Serial.print("POST data to flask: ");
    Serial.println(urlFinal);
    HTTPClient http;
    http.begin(urlFinal.c_str());
    int httpCode = http.GET();
    Serial.print("HTTP Status Code: ");
    Serial.println(httpCode);
    if (httpCode > 0) {
      String payload = http.getString();
      //Serial.println("Payload: " + payload);
    }
    http.end();
  }
}

void postData_Sensor5() {
  if (WiFi.status() == WL_CONNECTED) {
    String urlFinal = serverName_Sensor5 + "/" + status_Sensor5 + "/" + distance_cm_Sensor5; 
    Serial.print("POST data to flask: ");
    Serial.println(urlFinal);
    HTTPClient http;
    http.begin(urlFinal.c_str());
    int httpCode = http.GET();
    Serial.print("HTTP Status Code: ");
    Serial.println(httpCode);
    if (httpCode > 0) {
      String payload = http.getString();
      //Serial.println("Payload: " + payload);
    }
    http.end();
  }
}

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

void checkafstand_Sensor1() {
  if (distance_cm_Sensor1 <= afstand) {
    Serial.println("Bezet");
    status_Sensor1 = "Bezet";
    digitalWrite(LED1, HIGH);
  } else {
    Serial.println("Beschikbaar");
    status_Sensor1 = "Beschikbaar";
    digitalWrite(LED1, LOW);
  }
  postData_Sensor1();
}

void checkafstand_Sensor2() {
  if (distance_cm_Sensor2 <= afstand) {
    Serial.println("Bezet");
    status_Sensor2 = "Bezet";
    digitalWrite(LED2, HIGH);
  } else {
    Serial.println("Beschikbaar");
    status_Sensor2 = "Beschikbaar";
    digitalWrite(LED2, LOW);
  }
  postData_Sensor2();
}

void checkafstand_Sensor3() {
  if (distance_cm_Sensor3 <= afstand) {
    Serial.println("Bezet");
    status_Sensor3 = "Bezet";
    digitalWrite(LED3, HIGH);
  } else {
    Serial.println("Beschikbaar");
    status_Sensor3 = "Beschikbaar";
    digitalWrite(LED3, LOW);
  }
  postData_Sensor3();
}

void checkafstand_Sensor4() {
  if (distance_cm_Sensor4 <= afstand) {
    Serial.println("Bezet");
    status_Sensor4 = "Bezet";
    digitalWrite(LED4, HIGH);
  } else {
    Serial.println("Beschikbaar");
    status_Sensor4 = "Beschikbaar";
    digitalWrite(LED4, LOW);
  }
  postData_Sensor4();
}

void checkafstand_Sensor5() {
  if (distance_cm_Sensor5 <= afstand) {
    Serial.println("Bezet");
    status_Sensor5 = "Bezet";
    digitalWrite(LED5, HIGH);
  } else {
    Serial.println("Beschikbaar");
    status_Sensor5 = "Beschikbaar";
    digitalWrite(LED5, LOW);
  }
  postData_Sensor5();
}

void afstandSensor1() {
  digitalWrite(TRIG_PIN1, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN1, LOW);
  duration_us_Sensor1 = pulseIn(ECHO_PIN1, HIGH);
  distance_cm_Sensor1 = 0.017 * duration_us_Sensor1;
  Serial.print("Distance: Sensor 1: ");
  Serial.print(distance_cm_Sensor1);
  Serial.println(" cm");
  checkafstand_Sensor1();
}

void afstandSensor2() {
  digitalWrite(TRIG_PIN2, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN2, LOW);
  duration_us_Sensor2 = pulseIn(ECHO_PIN2, HIGH);
  distance_cm_Sensor2 = 0.017 * duration_us_Sensor2;
  Serial.print("Distance: Sensor 2: ");
  Serial.print(distance_cm_Sensor2);
  Serial.println(" cm");
  checkafstand_Sensor2();
}

void afstandSensor3() {
  digitalWrite(TRIG_PIN3, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN3, LOW);
  duration_us_Sensor3 = pulseIn(ECHO_PIN3, HIGH);
  distance_cm_Sensor3 = 0.017 * duration_us_Sensor3;
  Serial.print("Distance: Sensor 3: ");
  Serial.print(distance_cm_Sensor3);
  Serial.println(" cm");
  checkafstand_Sensor3();
}

void afstandSensor4() {
  digitalWrite(TRIG_PIN4, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN4, LOW);
  duration_us_Sensor4 = pulseIn(ECHO_PIN4, HIGH);
  distance_cm_Sensor4 = 0.017 * duration_us_Sensor4;
  Serial.print("Distance: Sensor 4: ");
  Serial.print(distance_cm_Sensor4);
  Serial.println(" cm");
  checkafstand_Sensor4();
}

void afstandSensor5() {
  digitalWrite(TRIG_PIN5, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN5, LOW);
  duration_us_Sensor5 = pulseIn(ECHO_PIN5, HIGH);
  distance_cm_Sensor5 = 0.017 * duration_us_Sensor5;
  Serial.print("Distance: Sensor 5: ");
  Serial.print(distance_cm_Sensor5);
  Serial.println(" cm");
  checkafstand_Sensor5();
}

void get_data() {
  if ((WiFi.status() == WL_CONNECTED)) {
    HTTPClient http;
    http.begin(serverNamestatus);
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
      } else if (status == "Voltooid" || status == "Geannuleerd") {
        digitalWrite(LED1, LOW);
        Serial.println("Reservering 1 is niet Gereserveerd");
        statusuitofaan1 = true;
      }

    }

    if (id == "6f95405c-06ee-11ef-acec-c4b301cc06d7") {
      if (status == "Gereserveerd") {
        digitalWrite(LED2, HIGH);
        Serial.print("led 2 is aan met id ");
        Serial.println(id);
        Serial.println("Reservering 2 is Gereserveerd");
      } else if (status == "Voltooid" || status == "Geannuleerd") {
        digitalWrite(LED2, LOW);
        Serial.println("Reservering 2 is niet Gereserveerd");
        statusuitofaan2 = true; 
      }
    }

    if (id == "6f954412-06ee-11ef-acec-c4b301cc06d7") {
      if (status == "Gereserveerd") {
        digitalWrite(LED3, HIGH);
        Serial.print("led 3 is aan met id ");
        Serial.println(id);
        Serial.println("Reservering 3 is Gereserveerd");
      } else if (status == "Voltooid" || status == "Geannuleerd") {
        digitalWrite(LED3, LOW);
        Serial.println("Reservering 3 is niet Gereserveerd");
        statusuitofaan3 = true;
      }
    }

    if (id == "6f9544b2-06ee-11ef-acec-c4b301cc06d7") {
      if (status == "Gereserveerd") {
        digitalWrite(LED4, HIGH);
        Serial.print("led 4 is aan met id ");
        Serial.println(id);
        Serial.println("Reservering 4 is Gereserveerd");
      } else if (status == "Voltooid" || status == "Geannuleerd") {
        digitalWrite(LED4, LOW);
        Serial.println("Reservering 4 is niet Gereserveerd");
        statusuitofaan4 = true;
      }
    }

    if (id == "6f95452a-06ee-11ef-acec-c4b301cc06d7") {
      if (status == "Gereserveerd") {
        digitalWrite(LED5, HIGH);
        Serial.print("led 5 is aan met id ");
        Serial.println(id);
        Serial.println("Reservering 5 is Gereserveerd");
      } else if (status == "Voltooid" || status == "Geannuleerd") {
        digitalWrite(LED5, LOW);
        Serial.println("Reservering 5 is niet Gereserveerd");
        statusuitofaan5 = true;
      }
    }
  }
}

void checkuitvoorafstandSensor()
{
  if (statusuitofaan1 == true)
  {
   afstandSensor1();
   statusuitofaan1 = false;
  }
  if (statusuitofaan2 == true)
  {
    afstandSensor2();
    statusuitofaan2 = false;

  }
  if (statusuitofaan3 == true)
  {
    afstandSensor3();
    statusuitofaan3 = false;
  }
  if (statusuitofaan4 == true)
  {
    afstandSensor4();
    statusuitofaan4 = false;
  }
  if (statusuitofaan5 == true)
  {
    afstandSensor5();
    statusuitofaan5 = false;
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(LED4, OUTPUT);
  pinMode(LED5, OUTPUT);
  pinMode(TRIG_PIN1, OUTPUT);
  pinMode(ECHO_PIN1, INPUT);
  pinMode(TRIG_PIN2, OUTPUT);
  pinMode(ECHO_PIN2, INPUT);
  pinMode(TRIG_PIN3, OUTPUT);
  pinMode(ECHO_PIN3, INPUT);
  pinMode(TRIG_PIN4, OUTPUT);
  pinMode(ECHO_PIN4, INPUT);
  pinMode(TRIG_PIN5, OUTPUT);
  pinMode(ECHO_PIN5, INPUT);
  initWifi();
}


void loop() {
  // Update data every 10 seconds
  if (millis() - startpoint >= 10000) {
    startpoint = millis();
    get_data();
    updateLedStatus();
  }
  if (millis_check) {
    Serial.println("10 seconds passed");
  }
  checkuitvoorafstandSensor();
}


