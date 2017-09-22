def gemiddelde():
    zin = input('Vul hier je zin in:')
    zin_split = zin.split(' ')
    aantal_letters = 0
    aantal_woorden = 0
    for woord in zin_split:
        aantal_letters += len(woord)
        aantal_woorden += 1
    print('Het gemiddelde is:',  aantal_letters/aantal_woorden)

gemiddelde()