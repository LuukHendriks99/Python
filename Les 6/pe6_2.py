aantal = eval(input('Geef lijst met minimaal 10 strings: '))
list = []
for woord in aantal:
    if len(woord) == 4:
        list.append(woord)

print('De nieuw-gemaakte lijst met alle vier-letter strings is:', list)
