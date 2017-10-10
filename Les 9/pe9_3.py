import csv

with open('scores.csv') as csvfile:
    x = csv.reader(csvfile, delimiter=';')
    spelers = []
    scores = []
    data = []
    for row in x:
        speler = row[0]
        datum = row [1]
        score = row [2]

        spelers.append(speler)
        data.append(datum)
        scores.append(score)
    print(max(scores))
