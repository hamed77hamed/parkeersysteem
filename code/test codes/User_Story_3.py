"""Deze Python-code beheert het toevoegen, bijwerken en bekijken van parkeerplaatsen in een database. Hier is een beknopte beschrijving van de functionaliteit:

Module Imports: Gebruikt modules zoals random, datetime, uuid, en een aangepaste module wachtwoord voor databaseconnectiviteit.
Functie insert_parkeerplaatsen: Voegt een nieuwe parkeerplaats toe aan de database met een unieke ID, een willekeurig type (elektrische of gewone parking), en een willekeurige status (Beschikbaar of Bezet).
Functie update_parkeerplaatsen: Werkt de status van alle parkeerplaatsen in de database bij naar een willekeurige nieuwe status (Beschikbaar of Bezet).
Functie view_parkeerplaatsen: Haalt alle parkeerplaatsen op uit de database en print deze naar de console.
Hoofdfunctie (main): Maakt continu verbinding met de database en voert de functies voor het toevoegen, bijwerken en bekijken van parkeerplaatsen uit in een oneindige lus.
Deze setup is ideaal voor systemen die continu de status van parkeerplaatsen moeten beheren en bijwerken, zoals parkeermanagementsystemen in steden of op grote parkeerterreinen.

Bron: https://www.w3schools.com/python/module_random.asp
tekst verbeteren door: chatgpt
"""

import random
from datetime import datetime
import uuid
from wachtwoord import *
 

def insert_parkeerplaatsen(connection):
    cursor = connection.cursor()
    sql = """INSERT INTO Parkeerplaats (ParkeerplaatsID, TypeParking, Parkeerplaats_Status)
             VALUES (%s, %s, %s)"""
    ParkeerplaatsID = str(uuid.uuid4())
    TypeParking = random.choice(['elektrische parking', 'gewoon parking'])
    Parkeerplaats_Status = random.choice(['Beschikbaar', 'Bezet'])
    val = (ParkeerplaatsID, TypeParking, Parkeerplaats_Status)
    cursor.execute(sql, val)
    print(f"Parkeerplaats toegevoegd: {val}")
    connection.commit()
    cursor.close()

def update_parkeerplaatsen(connection):
    cursor = connection.cursor()
    sql = "UPDATE Parkeerplaats SET Parkeerplaats_Status = %s WHERE ParkeerplaatsID = %s"
    select_query = "SELECT ParkeerplaatsID FROM Parkeerplaats"
    cursor.execute(select_query)
    parkeerplaatsen = cursor.fetchall()

    for parkeerplaats_id in parkeerplaatsen:
        nieuwe_status = random.choice(['Beschikbaar', 'Bezet'])
        print(nieuwe_status)
        cursor.execute(sql, (nieuwe_status, parkeerplaats_id[0]))

    connection.commit()
    print(f"Alle parkeerplaatsen zijn bijgewerkt met een nieuwe status.")
    cursor.close()

def view_parkeerplaatsen(connection):
    cursor = connection.cursor()
    sql = "SELECT * FROM Parkeerplaats"
    cursor.execute(sql)
    parkeerplaatsen = cursor.fetchall()
    print(parkeerplaatsen)
    cursor.close()

# def main():
#     connection = connect()
#     for i in range(100):
#         print(f"Inserting parkeerplaats {i+1}")
#         insert_parkeerplaatsen(connection)
#     for i in range(100):
#         print(f"Updating parkeerplaatsen {i+1}")
#         update_parkeerplaatsen(connection)
#     for i in range(100):  
#         print(f"Viewing parkeerplaatsen")
#         view_parkeerplaatsen(connection)
#         break  
#     connection.close()

def main():
    connection = connect()
    while True:
        print(f"Inserting parkeerplaats")
        insert_parkeerplaatsen(connection)
        print(f"Updating parkeerplaatsen")
        update_parkeerplaatsen(connection)
        print(f"Viewing parkeerplaatsen")
        view_parkeerplaatsen(connection)
        

if __name__ == "__main__":
    main()
