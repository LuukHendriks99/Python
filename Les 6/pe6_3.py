nummers = "5-9-7-1-7-8-3-2-4-8-7-9"
list = []
for cijfers in nummers:
    if cijfers in '0123456789':
        list.append(int(cijfers))

print('Gesorteerde list van ints:', sorted(list))
print('Grootste getal:', max(list), 'en Kleinste getal:', min(list))
print('Aantal getallen:', len(list), 'en Som van de getallen:', sum(list))
print('Gemiddelde:', sum(list) / len(list))