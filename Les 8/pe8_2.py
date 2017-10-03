import random


def monopolyworp():
    counter = 0
    while True:
        worp1 = random.randrange(1, 7)
        worp2 = random.randrange(1, 7)
        totaal = worp1 + worp2
        if worp1 == worp2:
            if counter == 2:
                print('{} + {} = (direct naar de gevangenis)'.format(worp1, worp2))
                break
            counter += 1
            print('{} + {} = {} (dubbel)'.format(worp1, worp2, totaal))
        else:
            print('{} + {} = {}'.format(worp1, worp2, totaal))
            counter = 0


monopolyworp()
