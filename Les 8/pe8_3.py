naam = input('Geef hier je naam: ')
bstation = input('Geef hier je beginstation op: ')
estation = input('Geef hier je eindstation op: ')
invoerstring = naam + bstation + estation


def code(invoerstring):
    str = ''
    for item in invoerstring:
        z = ord(item)
        y = z + 3
        q = chr(y)
        str += q
    print(str)


code(invoerstring)
