"""Deze Python-code beheert het verzamelen en opslaan van gebruikersfeedback in een database. Hier is een beknopte beschrijving van de functionaliteit:

Module Imports: Gebruikt modules zoals random, datetime, uuid, en een aangepaste module wachtwoord voor databaseconnectiviteit.
Feedback Opties: Definieert een lijst met mogelijke feedbackopties zoals "Goede service", "Slechte service", etc.
Feedback Invoerfunctie: Genereert een unieke ID voor elke feedback, selecteert willekeurig een feedback uit de lijst, registreert de datum en tijd, en slaat deze gegevens op in een database.
Hoofdfunctie (main): Maakt continu verbinding met de database en voert de feedbackinvoerfunctie uit in een oneindige lus.
Deze setup is ideaal voor systemen die continu gebruikersfeedback moeten verzamelen en opslaan, zoals klantenserviceportalen of interactieve kiosken.
Bron: https://www.w3schools.com/python/module_random.asp
tekst verbeteren door: chatgpt
"""





import random
from datetime import datetime
import uuid
from wachtwoord import *



feedback_options = [
    "Goede service",
    "Slechte service",
    "Zeer tevreden",
    "Niet tevreden",
    "Uitstekende ervaring",
    "Kan beter",
    "Zeer behulpzaam",
    "Niet behulpzaam",
    "Snelle service",
    "Langzame service"
]



def insert_feedback(connection):
    cursor = connection.cursor()
    sql = "INSERT INTO Feedback (FeedbackID, Naam, Opmerking, DatumTijd) VALUES (%s, %s, %s, %s)"
    feedback_id = str(uuid.uuid4())
    naam = "Random User"
    opmerking = random.choice(feedback_options)
    datum_tijd = datetime.now()
    val = (feedback_id, naam, opmerking, datum_tijd)
    cursor.execute(sql, val)
    print(f"Feedback inserted: {feedback_id}, {naam}, {opmerking}, {datum_tijd}")  
    connection.commit()
    cursor.close()
    return val



# def main():
#     connection = connect()    
#     for i in range(100):
#         print(f"Inserting feedback {i+1}")
#         insert_feedback(connection)
        
#     connection.close()

def main():
    connection = connect()    
    while True:
        print(f"Inserting feedback")
        insert_feedback(connection)
        
        

if __name__ == "__main__":
    main()
    