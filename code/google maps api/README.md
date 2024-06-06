# Google maps 
Deze HTML-pagina toont een Google Map en bevat knoppen voor verschillende acties. Hier is een korte beschrijving van wat de code doet:

HTML Structuur:
Een koptekst <h1> met de tekst "My First Google Map".
Een <div> element met de id "googleMap" waar de kaart wordt weergegeven.
Vier knoppen die linken naar verschillende pagina's: "Reservatie Annuleren", "Reservatie tijdt status", "Feedback", en "Pagina 4".
JavaScript:
De functie myMap() initialiseert de Google Map met een centrum op een specifieke locatie (coördinaten 51.1749, 4.36664) en een zoomniveau van 15.
Markers worden dynamisch toegevoegd aan de kaart op basis van server-side data (locations).
Elke marker heeft een klik-event listener die de kaart inzoomt, de marker in het midden plaatst, andere markers verbergt, en de parkeerstatus ophaalt.
De functie fetchParkingStatus() haalt parkeerstatusinformatie op van de server en tekent rechthoeken op de kaart met kleuren die de status aangeven (rood voor gereserveerd/bezet, groen voor beschikbaar).
De functie fetchInfo() haalt aanvullende informatie op voor een specifieke parkeerplaats en toont deze in een info-venster. Als de parkeerplaats beschikbaar is, wordt een reserveringslink toegevoegd.
De functie openReservationForm() toont een formulier in het info-venster waarmee gebruikers een parkeerplaats kunnen reserveren.
De functie submitReservation() verstuurt het reserveringsformulier naar de server.
De functies hideMarkers() en showMarkers() verbergen en tonen markers op de kaart, respectievelijk.
Een event listener op de kaart zorgt ervoor dat markers weer zichtbaar worden en het info-venster sluit als er wordt uitgezoomd tot een niveau van 16 of lager.
Google Maps API:
De Google Maps API wordt geladen met een API-sleutel en roept de myMap() functie aan zodra de API is geladen.
Deze code zorgt ervoor dat gebruikers interactief kunnen navigeren op de kaart, parkeerstatussen kunnen bekijken, en reserveringen kunnen maken.

bronnen:
https://www.w3schools.com/graphics/google_maps_basic.asp
https://developers.google.com/maps/documentation/javascript/markers
https://developers.google.com/earth-engine/apidocs/map-setzoom
https://www.w3schools.com/js/js_arrays.asp
https://www.w3schools.com/jsref/jsref_push.asp
https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
https://developer.mozilla.org/en-US/docs/Web/API/Response/json
https://developers.google.com/maps/documentation/javascript/shapes#rectangles
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator
https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_form_submit
https://developers.google.com/maps/documentation/javascript/infowindows
https://developer.mozilla.org/en-US/docs/Web/API/Window/alert
https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch#supplying_request_options
https://www.w3schools.com/js/js_if_else.asp
https://developers.google.com/maps/documentation/javascript/examples/rectangle-simple
https://developers.google.com/maps/documentation/javascript/examples/infowindow-simple
https://developers.google.com/maps/documentation/javascript/examples/marker-remove
https://developers.google.com/maps/documentation/javascript/examples/event-zoom
https://developers.google.com/maps/documentation/javascript/examples/rectangle-event
https://developers.google.com/maps/documentation/javascript/examples/marker-simple
https://developers.google.com/maps/documentation/javascript/examples/infowindow-event