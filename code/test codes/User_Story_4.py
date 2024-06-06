"""Deze Python-code beheert het toevoegen, bijwerken en bekijken van gebruikers en reserveringen in een database. Hier is een beknopte beschrijving van de functionaliteit:

Module Imports: Gebruikt modules zoals uuid, random, datetime, timedelta, Faker voor het genereren van nepgegevens, en een aangepaste module wachtwoord voor databaseconnectiviteit.
Functie gebruiker: Voegt een nieuwe gebruiker toe aan de database met een unieke ID, gegenereerde naam, auto, nummerplaat, e-mail en telefoonnummer.
Functie insert_reserveren: Voegt een nieuwe reservering toe aan de database met een unieke ID, starttijd, eindtijd en een willekeurige status (Gereserveerd, Voltooid, Geannuleerd).
Functie update_reserveren: Werkt de status van alle reserveringen in de database bij naar een willekeurige nieuwe status (Gereserveerd, Voltooid, Geannuleerd).
Functie view_reserveringen: Haalt alle reserveringen op uit de database en print deze naar de console.
Hoofdfunctie (main): Maakt continu verbinding met de database en voert de functies voor het toevoegen van gebruikers, het toevoegen van reserveringen, het bijwerken van reserveringen en het bekijken van reserveringen uit in een oneindige lus.
Deze setup is ideaal voor systemen die continu gebruikers- en reserveringsgegevens moeten beheren en bijwerken, zoals parkeermanagementsystemen of reserveringssystemen voor evenementen.

Bron:
https://www.w3schools.com/python/module_random.asp
https://faker.readthedocs.io/en/master/
tekst verbeteren door: chatgpt
"""

import uuid
import random
from datetime import datetime, timedelta
from faker import Faker
from wachtwoord import *

def gebuiker(connection):
    cursor = connection.cursor()
    sql = """INSERT INTO Gebruiker (GebruikerID, Naam, Auto, Nummerplaat, Email, Telefoonnummer)
             VALUES (%s, %s, %s, %s, %s, %s)"""
    fake = Faker()
    GebruikerID = str(uuid.uuid4())
    Naam = fake.name()
    Auto = fake.word()
    Nummerplaat = fake.word()[:10]
    Email = fake.email()
    Telefoonnummer = fake.phone_number()[:15]  
    val = (GebruikerID, Naam, Auto, Nummerplaat, Email, Telefoonnummer)
    cursor.execute(sql, val)
    print(f"Gebruiker toegevoegd: {val}")
    connection.commit()
    cursor.close()

def insert_reserveren(connection):
    cursor = connection.cursor()
    sql = """INSERT INTO Reservering (ReserveringID, GebruikerID, ParkeerplaatsID, BeginTijd, EindTijd, Reservering_Status)
             VALUES (%s, null, null, %s, %s, %s)"""
    ReserveringID = str(uuid.uuid1())
    BeginTijd = datetime.now()
    EindTijd = BeginTijd + timedelta(minutes=30)
    Reservering_Status = random.choice(['Gereserveerd', 'Voltooid', 'Geannuleerd'])
    val = (ReserveringID, BeginTijd, EindTijd, Reservering_Status)
    cursor.execute(sql, val)
    print(f"Reservering toegevoegd: {val}")
    connection.commit()
    cursor.close()

def update_reserveren(connection):
    cursor = connection.cursor()
    sql = """UPDATE Reservering SET Reservering_Status = %s WHERE ReserveringID = %s"""
    select_query = "SELECT ReserveringID FROM Reservering"
    cursor.execute(select_query)
    reserveringen = cursor.fetchall()

    for reservering_id in reserveringen:
        nieuwe_status = random.choice(['Gereserveerd', 'Voltooid', 'Geannuleerd'])
        print(f"Reservering bijgewerkt: {nieuwe_status}")
        cursor.execute(sql, (nieuwe_status, reservering_id[0]))

    connection.commit()
    print(f"Alle reserveringen zijn bijgewerkt met een nieuwe status.")
    cursor.close()

def view_reserveringen(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Reservering")
    reserveringen = cursor.fetchall()
    for reservering in reserveringen:
        print(reservering)
    cursor.close()

# def main():
#     connection = connect()
#     for i in range(100):
#         print(f"Inserting gebruiker {i+1}")
#         gebuiker(connection)
#     for i in range(100):
#         print(f"Inserting reserveren {i+1}")
#         insert_reserveren(connection)
#     for i in range(100):
#         print(f"Updating reserveren {i+1}")
#         update_reserveren(connection)
#     for i in range(100):
#         print(f"Viewing reserveren {i+1}")
#         view_reserveringen(connection)
#     connection.close()

def main():
    connection = connect()
    while True:
        print("Inserting gebruiker")
        gebuiker(connection)
        print("Inserting reserveren")
        insert_reserveren(connection)
        print("Updating reserveren")
        update_reserveren(connection)
        print("Viewing reserveren")
        view_reserveringen(connection)
        

if __name__ == "__main__":
    main()
