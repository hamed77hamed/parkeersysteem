"""Deze Python-code beheert het bijwerken en bekijken van parkeertarieven in een database. Hier is een beknopte beschrijving van de functionaliteit:

Module Imports: Gebruikt modules zoals random, datetime, uuid, en een aangepaste module wachtwoord voor databaseconnectiviteit.
Functie update_parkeertarieven: Werkt de parkeertarieven bij voor alle locaties in de database. Voor elke locatie wordt een willekeurig tarief tussen 1 en 100 gegenereerd en bijgewerkt in de database.
Functie view_parkeertarieven: Haalt de parkeertarieven op van alle locaties in de database en print deze naar de console.
Hoofdfunctie (main): Maakt continu verbinding met de database en voert de functies voor het bijwerken en bekijken van parkeertarieven uit in een oneindige lus.
Deze setup is ideaal voor systemen die continu de parkeertarieven moeten beheren en bijwerken, zoals parkeermanagementsystemen in steden of op grote parkeerterreinen.

Bron: https://www.w3schools.com/python/module_random.asp
tekst verbeteren door: chatgpt
"""

import random
from datetime import datetime
import uuid
from wachtwoord import *


def update_parkeertarieven(connection):
    cursor = connection.cursor()
    sql = "UPDATE Locatie SET parkeertarieven = %s WHERE LocatieID = %s"
    select_query = "SELECT LocatieID FROM Locatie"
    cursor.execute(select_query)
    LocatieID = cursor.fetchall()

    for locatie_id in LocatieID:
        val = random.randint(1, 100)
        cursor.execute(sql, (val, locatie_id[0]))
        print(f"Parkeertarieven bijgewerkt voor LocatieID {locatie_id[0]}: {val}")

    connection.commit()
    cursor.close()

def view_parkeertarieven(connection):
    cursor = connection.cursor()
    select_query = "SELECT Parkeertarieven FROM Locatie"
    cursor.execute(select_query)
    locaties = cursor.fetchall()
    for locatie in locaties:
        print(locatie)

    cursor.close()

# def main():
#     connection = connect()
#     for i in range(100):
#         print(f"Parkeertarieven bijwerken voor de {i + 1}e keer")
#         update_parkeertarieven(connection)
#         print("Parkeertarieven bekijken")
#         view_parkeertarieven(connection)
#     connection.close()

def main():
    connection = connect()
    while True:
        print("Parkeertarieven bijwerken")
        update_parkeertarieven(connection)
        print("Parkeertarieven bekijken")
        view_parkeertarieven(connection)

if __name__ == "__main__":
    main()
