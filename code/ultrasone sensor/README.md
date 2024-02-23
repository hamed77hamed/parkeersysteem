# ultrasonic-sensor

Hier is een voorbeeldcode voor de ultrasone sensor. Deze code is afkomstig van: https://esp32io.com/tutorials/esp32-ultrasonic-sensor

Deze code is ontworpen om met een ESP32 microcontroller en een ultrasone sensor (zoals de HC-SR04) de afstand tot een object te meten. De ESP32 stuurt een ultrasonische puls uit via de TRIG-pin en ontvangt het echo-signaal via de ECHO-pin. De duur van de ontvangen echo wordt gebruikt om de afstand tot het object te berekenen, waarbij de afstand in centimeters wordt uitgedrukt en vervolgens naar de seriële monitor wordt gestuurd. Daarnaast controleert de code met behulp van de `millis()` functie of er 10 seconden zijn verstreken sinds de laatste meting, en voert indien ja, een nieuwe meting uit. Dit proces herhaalt zich continu in de `loop()` functie.
