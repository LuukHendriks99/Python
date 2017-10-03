naam = input('Geef hier je naam: ')
bstation = input('Geef hier je beginstation op: ')
estation = input('Geef hier je eindstation op: ')

invoerstring = naam + bstation + estation


def code(invoerstring):
    print(invoerstring)
    cijfers =  ''.join(str(ord(c) + 3) for c in invoerstring)
    print(cijfers)
    code = ''.join(chr(int(cijfer)) for cijfer in cijfers)
    print(code)
    return


code(invoerstring)

