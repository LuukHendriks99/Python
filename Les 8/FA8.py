def inlezen_beginstation(stations):

    while True:
        start = input('Vul hier een beginstation in: ')
        if start in stations:
            print('Uw begin station is', start)
            return
        else:
            print('Vul een ander station in.')




def inlezen_eindstation():
        eind = input('Vul hier uw eindstation in: ')



stations = ['Schagen', 'Heerhugowaard','Alkmaar','Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 's-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond',  'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)




eindstation = inlezen_eindstation(stations, beginstation)
#omroepen_reis(stations, beginstation, eindstation)