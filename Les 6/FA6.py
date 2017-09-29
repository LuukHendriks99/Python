def toon_aantal_kluizen_vrij():
    regels = sum(1 for regel in open('Kluizen.txt'))
    print('Het aantal vrije kluizen is:', 12 - regels)


def nieuwe_kluis():
    list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    kluizen = open('Kluizen.txt', 'r')
    kluisjes = kluizen.readlines()
    kluizen.close()
    for kluisje in kluisjes:
        regel = kluisje.split(';')
        list.remove(regel[0])
    if not list == []:
        kluizen = open('Kluizen.txt', 'a')
        code = input('Vul hier je code in:')
        if len(code) >= 4:
            kluizen.write(list[0] + ';' + code + '\n')
            print('Uw kluisnummer is', list[0])
            kluizen.close()
        else:
            print('Dit wachtwoord is te kort.')
            return
    else:
        print('Er zijn geen kluizen meer beschikbaar.')


def kluis_openen():
    nummer = input('Geef uw kluisnummer:')
    code = input('Geef uw code:')
    kluizen = open('Kluizen.txt', 'r')
    f = kluizen.readlines()
    kluizen.close()
    for line in f:
        if line == (nummer + ';' + code + '\n'):
            print('Kluisje is open.')
            return
    print('De code klopt niet.')


def kluis_teruggeven():
    nummer = input('Geef uw kluisnummer:')
    code = input('Geef uw code:')
    kluizen = open('Kluizen.txt', 'r')
    f = kluizen.readlines()
    kluizen.close()
    verwijder = open('Kluizen.txt', 'w')
    for line in f:
        if line == (nummer + ';' + code + '\n'):
            print('Kluisje is verwijderd')

        else:
            verwijder.write(line)


while True:

    print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
    print('2: Ik wil een nieuwe kluis')
    print('3: Ik wil even iets uit mijn kluis halen')
    print('4: Ik geef mijn kluis terug')
    print('5: Ik wil stoppen')
    keuze = input('Geef hier welke keuze je wilt uitvoeren:')

    if keuze == '1':
        toon_aantal_kluizen_vrij()

    elif keuze == '2':
        nieuwe_kluis()

    elif keuze == '3':
        kluis_openen()

    elif keuze == '4':
        kluis_teruggeven()
    elif keuze == '5':
        break
    else:
        print('Dit is geen geldige keuze')
