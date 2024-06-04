# ultrasonic-sensor GET

Hier is een voorbeeldcode voor de ultrasone sensor. Deze code is afkomstig van: 
Bronnen:
https://randomnerdtutorials.com/esp32-http-get-open-weather-map-thingspeak-arduino/
https://arduinojson.org/v6/example/
https://arduinojson.org/?utm_source=meta&utm_medium=library.properties

Deze code voor een ESP32 microcontroller doet het volgende:

WiFi Verbinding: Verbindt de ESP32 met een WiFi-netwerk met behulp van de SSID en wachtwoord die zijn opgeslagen in wifi_secrets.h.
Data Ophalen: Maakt een HTTP GET verzoek naar een server om JSON data op te halen. De ontvangen data wordt opgeslagen in een string genaamd payload.
JSON Parsing: Gebruikt de ArduinoJson bibliotheek om de ontvangen JSON data te parsen. De JSON data bevat reserveringsinformatie die wordt gebruikt om de status van LEDs bij te werken.
LED Status Bijwerken: Controleert de reserveringsstatussen in de JSON data en schakelt de bijbehorende LEDs in of uit op basis van de status ("Gereserveerd" of niet).
Periodieke Metingen: Voert elke 10 seconden een meting uit, haalt de data op van de server en werkt de LED-statussen bij.
