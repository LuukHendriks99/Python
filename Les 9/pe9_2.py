import time
import csv

bestand = 'inloggers.csv'

def inloggen():
    with open(bestand, 'w') as f:
        while True:
            tijd = time.strftime('%a %d %b %Y at %H:%M', time.localtime())
            naam = input('Wat is je achternaam? ')
            voorl = input('Wat zijn je voorletters? ')
            gbdatum = input('Wat is je geboortedatum? ')
            email = input('Wat is je e-mail adres? ')

            gegevens = tijd + naam + voorl + gbdatum + email
            f.write(gegevens)
            f.write('\n')
            if naam == 'einde' or 'Einde':
                break

inloggen()
