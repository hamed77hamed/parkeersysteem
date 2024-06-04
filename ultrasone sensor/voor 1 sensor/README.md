# ultrasonic-sensor voor 1 sensor en led

Hier is een voorbeeldcode voor de ultrasone sensor. Deze code is afkomstig van: 
bronnen: https://esp32io.com/tutorials/esp32-ultrasonic-sensor 
https://randomnerdtutorials.com/esp32-http-get-open-weather-map-thingspeak-arduino/ 
https://arduinojson.org/

Deze code voor een ESP32 microcontroller doet het volgende:

WiFi Verbinding: Verbindt de ESP32 met een WiFi-netwerk met behulp van de SSID en wachtwoord die zijn opgeslagen in wifi_secrets.h.
Sensor en LED Initialiseren: Definieert en initialiseert pinnen voor een ultrasone sensor en een LED.
Afstand Meten: Meet de afstand met behulp van een ultrasone sensor door een trigger signaal te sturen en de echo tijd te meten. De gemeten tijd wordt omgezet in afstand in centimeters.
Status Bepalen: Controleert of de gemeten afstand kleiner is dan een drempelwaarde (10 cm). Als de afstand kleiner is, wordt de status van de sensor ingesteld op "Bezet" en de bijbehorende LED wordt ingeschakeld; anders wordt de status ingesteld op "Beschikbaar" en de LED wordt uitgeschakeld.
Data Verzenden: Verzendt de status en gemeten afstand van de sensor naar een Flask-server via een HTTP GET verzoek.
Data Ontvangen: Ontvangt JSON data van een server met reserveringsstatussen en past de LED-status aan op basis van de ontvangen data. Dit wordt gedaan met behulp van de ArduinoJson bibliotheek.
Periodieke Metingen: Voert elke 10 seconden een meting uit, haalt de data op van de server en werkt de LED-status bij.
JSON Parsing: Gebruikt de ArduinoJson bibliotheek om de ontvangen JSON data te parsen en de LED-status bij te werken op basis van de reserveringsstatus.