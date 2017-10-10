import csv

with open('scores.csv') as csvfile:
    csv = csv.reader(csvfile, delimiter=';')
    lijst = []
    for row in csv:
        lijst.append(row[2])
print(lijst)
print(max(lijst))