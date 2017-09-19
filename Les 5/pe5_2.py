f = open('kaartnummer.txt','r' )
lines = f.readlines()
f.close()

for line in lines:
    info = line.split(', ')
    print(info[1].strip(), 'Heeft kaartnummer:', info[0], )
