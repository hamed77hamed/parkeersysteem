# ultrasonic-sensor post

Hier is een voorbeeldcode voor de ultrasone sensor. Deze code is afkomstig van: 
Bronnen:
https://esp32io.com/tutorials/esp32-ultrasonic-sensor en bron https://randomnerdtutorials.com/esp32-http-get-open-weather-map-thingspeak-arduino/


Deze code komt van de website Random Nerd Tutorials en is bedoeld voor een ESP32 microcontroller. De code doet het volgende:

WiFi Verbinding: Verbindt de ESP32 met een WiFi-netwerk.
Sensoren en LEDs Initialiseren: Definieert en initialiseert pinnen voor vijf ultrasone sensoren en vijf LEDs.
Afstand Meten: Meet de afstand met behulp van ultrasone sensoren en berekent de afstand in centimeters.
Status Bepalen: Controleert of de gemeten afstand kleiner is dan een drempelwaarde (10 cm). Als dat zo is, wordt de status van de sensor ingesteld op "Bezet" en de bijbehorende LED wordt ingeschakeld; anders wordt de status ingesteld op "Beschikbaar" en de LED wordt uitgeschakeld.
Data Verzenden: Verzendt de status en gemeten afstand van elke sensor naar een Flask-server via een HTTP GET verzoek.
Periodieke Metingen: Voert elke 10 seconden metingen uit en verzendt de data naar de server.

