from flask import Flask, request, render_template, json, redirect
import uuid
from datetime import datetime, timedelta
import smtplib
from wachtwoord import *

app = Flask(__name__)

@app.route('/parking')
def maps():
    db = get_db_connection()
    cursor = db.cursor()
    sql = """
    SELECT Straatnaam, MAX(north) AS latitude, MAX(east) AS longitude FROM Locatie GROUP BY Straatnaam
    """
    cursor.execute(sql)
    locations = cursor.fetchall()
    locations_list = [{'name': loc[0], 'lat': loc[1], 'lng': loc[2]} for loc in locations]
    cursor.close()
    db.close()
    print(locations_list)
    return render_template('mapstest3.html', locations=locations_list)

@app.route('/ReserveringStatus', methods=['GET'])
def ReserveringStatus():
    db = get_db_connection()
    cursor = db.cursor()
    sql = """SELECT ReserveringID, Reservering_Status FROM Reservering """
    cursor.execute(sql)
    reserveringstatus = cursor.fetchall()
    reservering_data = [{'ReserveringID': row[0], 'Reservering_Status': row[1]} for row in reserveringstatus]
    print(reservering_data)
    cursor.close()
    db.close()
    return reservering_data

@app.route('/parkingstatus', methods=['GET'])
def parkingstatus():
    db = get_db_connection()
    cursor = db.cursor()
    sql = """
    SELECT locatie.north, locatie.south, locatie.east, locatie.west, parkeerplaats.Parkeerplaats_Status, 
    reservering.Reservering_Status FROM Locatie AS locatie JOIN Parkeerplaats AS parkeerplaats ON 
    locatie.LocatieID = parkeerplaats.Locatie JOIN Reservering AS reservering ON parkeerplaats.ParkeerplaatsID = 
    reservering.ParkeerplaatsID
    """
    cursor.execute(sql)
    parkingstatus = cursor.fetchall()
    parking_data = [{'north': row[0], 'south': row[1], 'east': row[2], 'west': row[3], 'parkeerplaatsStatus': row[4], 'reserveringStatus': row[5]} for row in parkingstatus]
    print(parking_data)
    cursor.close()
    db.close()
    return parking_data

@app.route('/Sensor/<sensor_id>/<status>/<afstand>')
def update_sensor_data(sensor_id, status, afstand):
    connection = get_db_connection()
    cursor = connection.cursor()
    sql = "UPDATE Parkeerplaats SET Parkeerplaats_Status = %s, afstand = %s, tijd = %s WHERE ParkeerplaatsID = %s"
    val = (status, afstand, datetime.now(), sensor_id)
    cursor.execute(sql, val)
    connection.commit()
    volledigegeschiedenis(sensor_id, status)
    return f"<p>Sensor {sensor_id} data updated</p>"

@app.route('/info', methods=['GET'])
def info():
    db = get_db_connection()
    cursor = db.cursor()
    sql = """SELECT Locatie.Straatnaam, Locatie.huisnummer, Locatie.parkeertarieven, Locatie.north, Locatie.east, Parkeerplaats.ParkeerplaatsID, Parkeerplaats.TypeParking FROM Locatie JOIN Parkeerplaats ON Locatie.LocatieID = Parkeerplaats.Locatie"""
    cursor.execute(sql)
    info = cursor.fetchall()
    info_data = [{'straatnaam': row[0], 'huisnummer': row[1], 'parkeertarieven': row[2], 'north': row[3], 'east': row[4], 'parkeerplaatsID': row[5], 'typeParking': row[6]} for row in info]
    print(info_data)
    cursor.close()
    db.close()
    return info_data

@app.route('/gebruiker', methods=['POST'])
def gebruiker():
    db = get_db_connection()
    cursor = db.cursor()
    sql = """INSERT INTO Gebruiker (GebruikerID, Naam, Auto, Nummerplaat, Email, Telefoonnummer) VALUES (%s, %s, %s, %s, %s, %s)"""
    GebruikerID = str(uuid.uuid1())
    Naam = request.form['Naam']
    Auto = request.form['Auto']
    Nummerplaat = request.form['Nummerplaat']
    Email = request.form['Email']
    Telefoonnummer = request.form['Telefoonnummer']
    plaatsID = request.form['ParkeerplaatsID']
    val = (GebruikerID, Naam, Auto, Nummerplaat, Email, Telefoonnummer)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    update_reservering(GebruikerID, plaatsID)
    print('Gebruiker toegevoegd')
    print(f"GebruikerID: {GebruikerID}, Naam: {Naam}, Auto: {Auto}, Nummerplaat: {Nummerplaat}, Email: {Email}, Telefoonnummer: {Telefoonnummer}")
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(mijnemail, wachtwoord)
    # message to be sent
    message = f"Geachten, {Naam}\nU heeft een parkeerplaats gereserveerd."
    # sending the mail
    s.sendmail(mijnemail, Email , message)
    # terminating the session
    print("Mail is verstuurd")
    s.quit()
    sql = """SELECT Locatie FROM Parkeerplaats WHERE ParkeerplaatsID = %s"""
    cursor = db.cursor()
    cursor.execute(sql, (plaatsID,))
    locations = cursor.fetchone()
    sql = """INSERT INTO volledigegeschiedenis (GeschiedenisID, ParkeerplaatsID, LocatieID, Status, Timestamp) VALUES (%s, %s, %s, %s, %s)"""
    LocatieID = locations[0]
    Status = 'Bezet'
    Timestamp = datetime.now()
    val = (GebruikerID, plaatsID, LocatieID, Status, Timestamp)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()
    print('Geschiedenis toegevoegd')
    print(f"GebruikerID: {GebruikerID}, ParkeerplaatsID: {plaatsID}, LocatieID: {LocatieID}, Status: {Status}, Timestamp: {Timestamp}")
    return Naam, Email
   
def volledigegeschiedenis(sensor_id, status):
    db = get_db_connection()
    cursor = db.cursor()
    sql = """SELECT Locatie FROM Parkeerplaats WHERE ParkeerplaatsID = %s"""
    cursor.execute(sql, (sensor_id,))
    locations = cursor.fetchone()
    sql = """INSERT INTO volledigegeschiedenis (GeschiedenisID, ParkeerplaatsID, LocatieID, Status, Timestamp) VALUES (%s, %s, %s, %s, %s)"""
    GeschiedenisID = str(uuid.uuid1())
    LocatieID = locations[0]
    Timestamp = datetime.now()
    val = (GeschiedenisID, sensor_id, LocatieID, status, Timestamp)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()
    print('Geschiedenis toegevoegd')
    print(f"GeschiedenisID: {GeschiedenisID}, ParkeerplaatsID: {sensor_id}, LocatieID: {LocatieID}, Status: {status}, Timestamp: {Timestamp}")
    return 'Geschiedenis toegevoegd'

def update_reservering(GebruikerID, plaatsID):
    db = get_db_connection()
    cursor = db.cursor()
    sql = """UPDATE Reservering SET GebruikerID = %s, BeginTijd = %s, EindTijd = %s, Reservering_Status = %s WHERE ParkeerplaatsID = %s"""
    GebruikerID = GebruikerID
    BeginTijd = datetime.now()
    EindTijd = BeginTijd + timedelta(minutes=30)
    Reservering_Status = 'Gereserveerd'
    ParkeerplaatsID = plaatsID
    val = (GebruikerID, BeginTijd, EindTijd, Reservering_Status, ParkeerplaatsID)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()
    print('Reservering geupdate')
    print(f"GebruikerID: {GebruikerID}, BeginTijd: {BeginTijd}, EindTijd: {EindTijd}, Reservering_Status: {Reservering_Status}, ParkeerplaatsID: {ParkeerplaatsID}")
    return 'Reservering geupdate'


@app.route('/Reservatie-annuleren')
def Reservatie_annuleren():
    return render_template('1.html')

@app.route('/geannuleerd', methods=['POST'])
def submit_annuleren():
    with get_db_connection() as db:
        cursor = db.cursor()
        voornaam = request.form['voornaam']
        nummerplaat = request.form['nummerplaat']
        print(f"Voornaam: {voornaam}, Nummerplaat: {nummerplaat}")
        sql = "SELECT GebruikerID, Email FROM Gebruiker WHERE Naam = %s AND Nummerplaat = %s"
        val = (voornaam, nummerplaat)
        print(voornaam, nummerplaat)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result:
            original_GebruikerID, Email = result
            print(original_GebruikerID)
            sql = "UPDATE Reservering SET GebruikerID = NULL, Reservering_Status = %s WHERE GebruikerID = %s"
            Reservering_Status = "Geannuleerd"
            val = (Reservering_Status, original_GebruikerID)
            cursor.execute(sql, val)
            sql = "DELETE FROM Gebruiker WHERE GebruikerID = %s"
            val = (original_GebruikerID,)
            cursor.execute(sql, val)
            db.commit()
            print('Reservatie geannuleerd')
            # creates SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)
            # start TLS for security
            s.starttls()
            # Authentication
            s.login(mijnemail, wachtwoord)
            # message to be sent
            message = f"Geachten, {voornaam}\nUw reservatie is geannuleerd."
            # sending the mail
            s.sendmail(mijnemail, Email, message)
            # terminating the session
            print("Mail is verstuurd")
            s.quit()
        else:
            print('Gebruiker niet gevonden')
        return redirect('/parking')

@app.route('/tijd')
def page2():
    return render_template('2.html')

@app.route('/statustijd', methods=['POST'])
def statustijd():
    db = get_db_connection()
    cursor = db.cursor()
    voornaam = request.form['voornaam']
    nummerplaat = request.form['nummerplaat']
    print(f"Voornaam: {voornaam}, Nummerplaat: {nummerplaat}")
    sql = "SELECT GebruikerID FROM Gebruiker WHERE Naam = %s AND Nummerplaat = %s"
    val = (voornaam, nummerplaat)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    if result:
        original_GebruikerID = result[0]
        print(original_GebruikerID)
        sql = "SELECT BeginTijd, EindTijd FROM Reservering WHERE GebruikerID = %s"
        val = (original_GebruikerID,)
        cursor.execute(sql, val)
        result = cursor.fetchall()  # Gebruik fetchall om meerdere rijen te verwerken
        tijdlist = [{'BeginTijd': row[0], 'EindTijd': row[1]} for row in result]
        print(tijdlist)
        cursor.close()
        db.close()
        return render_template('2.html', result=tijdlist)  # Stuur de data naar de template
    else:
        print('Gebruiker niet gevonden')
    cursor.close()
    db.close()
    return redirect('/parking')

        
@app.route('/feedback')
def page3():
    return render_template('3.html')

@app.route('/feedbackstatus', methods=['POST'])
def feedbackstatus():
    db = get_db_connection()
    cursor = db.cursor()
    voornaam = request.form['voornaam']
    Opmerking = request.form['Opmerking']
    print(f"Voornaam: {voornaam}, Opmerking: {Opmerking}")
    sql = "INSERT INTO Feedback (FeedbackID, Naam, Opmerking, DatumTijd) VALUES (%s, %s, %s, %s)"
    FeedbackID = str(uuid.uuid1())
    Naam = voornaam
    DatumTijd = datetime.now()
    val = (FeedbackID, Naam, Opmerking, DatumTijd)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()
    print('Feedback toegevoegd')
    print(f"FeedbackID: {FeedbackID}, Naam: {Naam}, Opmerking: {Opmerking}, DatumTijd: {DatumTijd}")
    return redirect('/parking')



