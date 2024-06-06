"""Deze Python-code verstuurt e-mails via de SMTP-server van Gmail. Hier is een korte beschrijving van wat de code doet:

Beschrijving van de Code
Imports:
Importeert de smtplib module voor het versturen van e-mails.
Importeert mijnemail en wachtwoord uit een module genaamd wachtwoord.
Functie send_email:
Verbindt met de Gmail SMTP-server.
Start TLS voor beveiligde communicatie.
Logt in met de opgegeven e-mail en wachtwoord.
Verstuurt de e-mail van de afzender naar de ontvanger.
Sluit de verbinding en print een bevestigingsbericht.
Functie main:
Definieert het e-mailadres van de ontvanger en het bericht.
In een oneindige while-lus wordt de send_email functie aangeroepen om continu e-mails te versturen.
bronnen: https://www.geeksforgeeks.org/send-mail-gmail-account-using-python/
https://support.google.com/a/answer/176600?hl=en
tekst verbeteren door: chatgpt
"""

import smtplib
from wachtwoord import *

def send_email(sender_email, sender_password, recipient_email, message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, sender_password)
    s.sendmail(sender_email, recipient_email, message)
    s.quit()
    print("Mail is verstuurd")

# def main():
#     ontvanger_email = ""
#     bericht = "hallo, dit is een testmail vanuit Python."

#     for teller in range(100):
#         send_email(mijnemail, wachtwoord, ontvanger_email, bericht)
#         print(f'Dit is de {teller}e mail')

def main():
    ontvanger_email = ""
    bericht = "hallo, dit is een testmail vanuit Python."

    while True:
        send_email(mijnemail, wachtwoord, ontvanger_email, bericht)
        print('Mail is verstuurd')

if __name__ == "__main__":
    main()
