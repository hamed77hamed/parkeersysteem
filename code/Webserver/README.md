# Flask

Deze Flask-applicatie biedt verschillende routes voor het beheren van parkeerplaatsen, reserveringen en gebruikersfeedback. Hier is een korte beschrijving van wat de code doet:

Beschrijving van de Code
Imports:
Importeert benodigde modules zoals Flask, request, render_template, json, redirect, uuid, datetime, timedelta, smtplib en wachtwoord.
Flask Applicatie:
Initialiseert een Flask-applicatie.
Routes:
/parking: Haalt locaties van parkeerplaatsen op uit de database en rendert een HTML-template met een Google Map.
/ReserveringStatus: Haalt de status van reserveringen op en retourneert deze als JSON.
/parkingstatus: Haalt de status van parkeerplaatsen op en retourneert deze als JSON.
/Sensor/<sensor_id>/<status>/<afstand>: Update de status van een parkeerplaats op basis van sensorgegevens.
/info: Haalt informatie over parkeerplaatsen op en retourneert deze als JSON.
/gebruiker: Voegt een nieuwe gebruiker toe aan de database en stuurt een bevestigingsmail.
/Reservatie-annuleren: Rendert een HTML-template voor het annuleren van een reservering.
/geannuleerd: Verwerkt het annuleren van een reservering en stuurt een bevestigingsmail.
/tijd: Rendert een HTML-template voor het bekijken van de reserveringstijd.
/statustijd: Haalt de begin- en eindtijd van een reservering op en rendert deze in een HTML-template.
/feedback: Rendert een HTML-template voor het geven van feedback.
/feedbackstatus: Voegt feedback toe aan de database.
/page4: Rendert een HTML-template voor een vierde pagina.
Helper Functies:
volledigegeschiedenis(sensor_id, status): Voegt een volledige geschiedenis van een parkeerplaats toe aan de database.
update_reservering(GebruikerID, plaatsID): Update de reserveringsstatus van een parkeerplaats.
Bronnen
Hier zijn de volledige URL's van de bronnen die relevant zijn voor de gebruikte technologieën en methoden in de code:

https://flask.palletsprojects.com/en/2.0.x/
https://flask.palletsprojects.com/en/2.0.x/quickstart/#rendering-templates
https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request
https://flask.palletsprojects.com/en/2.0.x/api/#flask.json.jsonify
https://flask.palletsprojects.com/en/2.0.x/api/#flask.redirect
https://developer.mozilla.org/en-US/docs/Web/API/Response/json
https://developer.mozilla.org/en-US/docs/Web/API/Window/alert

tekst verbeteren door: chatgpt