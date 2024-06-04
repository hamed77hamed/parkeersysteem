#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include "wifi_secrets.h"
#include <ArduinoJson.h>

#define LED1  18


String payload;

#define TRIG_PIN1 D3   
#define ECHO_PIN1 D2

String status_Sensor1 = "Beschikbaar";
const float afstand = 10;
float duration_us_Sensor1, distance_cm_Sensor1;
unsigned long startpoint = 0;
boolean millis_check;
boolean statusuitofaan1 = false;
String id = "6f954476-06ee-11ef-acec-c4b301cc06d7";


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

    if (id == id) {
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
  }
}


    
    


 

void checkuitvoorafstandSensor()
{
  if (statusuitofaan1 == true)
  {
   afstandSensor1();
   statusuitofaan1 = false;
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(LED1, OUTPUT);
  pinMode(TRIG_PIN1, OUTPUT);
  pinMode(ECHO_PIN1, INPUT);
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


