# ultrasonic-sensor

Hier is een voorbeeldcode voor de ultrasone sensor. Deze code is afkomstig van: https://esp32io.com/tutorials/esp32-ultrasonic-sensor

WiFi Verbinding: Verbindt de ESP32 met een WiFi-netwerk met behulp van de SSID en wachtwoord die zijn opgeslagen in wifi_secrets.h.
Afstand Meten: Meet de afstand met behulp van een ultrasone sensor (HC-SR04) door een trigger signaal te sturen en de echo tijd te meten. De gemeten tijd wordt omgezet in afstand in centimeters.
Object Detectie: Controleert of de gemeten afstand kleiner is dan een drempelwaarde (10 cm). Als dat zo is, wordt gemeld dat een object dichtbij is; anders wordt gemeld dat het object ver weg is.
Periodieke Metingen: Voert elke seconde een meting uit en controleert de afstand.