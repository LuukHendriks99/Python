def convert(waarde):
    return waarde * 1.8 + 32


def table(x):
    print('{0:6}{1:10}'.format('     C', '         F'))
    for waarde in x:
        print('{0:6.2f}{1:10}'.format(convert(waarde), waarde))

table(range(-30, 41, 10))
