"""Deze Python-code beheert het toevoegen en bekijken van volledige geschiedenisgegevens van parkeerplaatsen in een database. Hier is een beknopte beschrijving van de functionaliteit:

Module Imports: Gebruikt modules zoals random, datetime, uuid, en een aangepaste module wachtwoord voor databaseconnectiviteit.
Functie insert_volledigegeschiedenis:
Selecteert willekeurig een ParkeerplaatsID en LocatieID uit de database.
Voegt een nieuwe record toe aan de tabel volledigegeschiedenis met een unieke ID, geselecteerde parkeerplaats en locatie, een willekeurige status (Beschikbaar of Bezet), en de huidige timestamp.
Functie view_volledigegeschiedenis:
Haalt gegevens op uit de tabel volledigegeschiedenis en gerelateerde tabellen (Locatie en Parkeerplaats).
Print de opgehaalde gegevens naar de console.
Hoofdfunctie (main):
Maakt continu verbinding met de database en voert de functies voor het toevoegen en bekijken van volledige geschiedenisgegevens uit in een oneindige lus.
Deze setup is ideaal voor systemen die continu de geschiedenis van parkeerplaatsgebruik moeten bijhouden en weergeven, zoals parkeermanagementsystemen in steden of op grote parkeerterreinen.

Bron: https://www.w3schools.com/python/module_random.asp
tekst verbeteren door: chatgpt
"""

import random
from datetime import datetime
import uuid
from wachtwoord import *
 

def insert_volledigegeschiedenis(connection):
    cursor = connection.cursor()
    
    select_parkeerplaats_sql = """SELECT ParkeerplaatsID FROM Parkeerplaats"""
    cursor.execute(select_parkeerplaats_sql)
    parkeerplaatsen = cursor.fetchall()
    ParkeerplaatsID = random.choice(parkeerplaatsen)[0]
    
    select_locatie_sql = """SELECT LocatieID FROM Locatie"""
    cursor.execute(select_locatie_sql)
    locaties = cursor.fetchall()
    LocatieID = random.choice(locaties)[0]
    
    insert_sql = """INSERT INTO volledigegeschiedenis (GeschiedenisID, ParkeerplaatsID, LocatieID, Status, Timestamp)
                    VALUES (%s, %s, %s, %s, %s)"""
    GeschiedenisID = str(uuid.uuid1())
    Status = random.choice(['Beschikbaar', 'Bezet'])
    Timestamp = datetime.now()
    cursor.execute(insert_sql, (GeschiedenisID, ParkeerplaatsID, LocatieID, Status, Timestamp))
    connection.commit()
    print(f"Volledige geschiedenis toegevoegd: {GeschiedenisID}, {ParkeerplaatsID}, {LocatieID}, {Status}, {Timestamp}")
    cursor.close()

def view_volledigegeschiedenis(connection):
    cursor = connection.cursor()
    sql = """
    SELECT l.Straatnaam, l.huisnummer, l.parkeertarieven, p.ParkeerplaatsID, p.TypeParking, v.Status, v.Timestamp FROM Locatie l JOIN Parkeerplaats p ON l.LocatieID = p.Locatie JOIN volledigegeschiedenis v ON p.ParkeerplaatsID = v.ParkeerplaatsID
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        for row in result:
            print(row)
    else:
        print("Geen gegevens gevonden.")
    cursor.close()

# def main():
#     connection = connect()
#     for i in range(100):
#         print(f"Inserting volledige geschiedenis {i+1}")
#         insert_volledigegeschiedenis(connection)
#     for i in range(100):
#         print(f"Viewing volledige geschiedenis {i+1}")
#         view_volledigegeschiedenis(connection)
#     connection.close()

def main():
    connection = connect()
    while True:
        print("Inserting volledige geschiedenis")
        insert_volledigegeschiedenis(connection)
        print("Viewing volledige geschiedenis")
        view_volledigegeschiedenis(connection)

if __name__ == "__main__":
    main()
