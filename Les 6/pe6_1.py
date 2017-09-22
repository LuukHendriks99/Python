maand = eval(input('Vul hier het maandummer in:'))


def functie_seizoen(maand):
    if maand >= 1 and maand <= 2:
        print('winter')
    elif maand >= 3 and maand <= 5:
        print('lente')
    elif maand >= 6 and maand <= 8:
        print('zomer')
    elif maand >= 9 and maand <= 11:
        print('herfst')
    elif maand == 12:
        print('winter')


functie_seizoen(maand)
