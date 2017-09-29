uitkomst = 0
aantal = 0
while True:
    invoer =  int(input('Geef een getal:'))
    if invoer == 0:
        print('Er zijn {} getallen ingevoerd, de som is: {}'.format(aantal, uitkomst))
        break
    else:
        uitkomst += invoer
        aantal += 1
