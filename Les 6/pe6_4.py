studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    antw = []
    for item in studentencijfers:
           list = sum(item)/len(item)
           antw.append(list)
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    antw = []
    for item in studentencijfers:
        list = sum(item) / len(item)
        antw.append(list)
    antw = sum(antw) / len(antw)
    return antw

print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))